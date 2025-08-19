What it is: Send multiple copies of a pac
ket (or segments that overlap slightly) s
o the sensor and endpoint might assemble 
different byte streams.

Why it can work: If the IDS and endpoint 
make different choices on which duplicate
/overlap “wins,” the IDS may see something benign while the host
 sees the intended bytes (or vice versa).

Where it works: Mixed OS environments, heterogeneous middleboxes, or sensors that skip strict reassembly for performance.

Defensive counters: Normalizers that collapse duplicates/overlaps deterministically, OS-aware reassembly policies, and al
erts on overlap anomalies.


🔹 The idea

IDS/IPS (Intrusion Detection/Prevention Systems) and firewalls often reassemble or analyze traffic differently from how the target machine’s TCP/IP stack does.
If you send two or more packets with the same sequence number (TCP) or overlapping fragments (IP), the IDS might:

Drop one copy and only analyze the other (possibly missing your real malicious payload).

Reassemble incorrectly, depending on its implementation.

Raise false positives, which can be used to distract defenders.

Meanwhile, the target host’s TCP/IP stack may accept one of the duplicates (usually the first or last one, depending on OS).

🔹 Example (TCP duplicate packet evasion)

Suppose you want to send a payload to port 80:

You craft a normal TCP packet with sequence number X, ACK Y, payload = benign text (e.g., "GET / HTTP/1.1").

You then craft a second TCP packet with the exact same sequence number X, ACK Y, but with payload = malicious code or scan marker.

Depending on how the IDS is written:

It may see only the first packet (thinks it’s harmless).

The target machine may instead accept the second one, executing the malicious intent.

This desynchronizes IDS and real target behavior → evasion achieved.
