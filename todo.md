## Goals:
- [ ] Build a Python tool (using Scapy) to craft and inject custom packets (TCP, UDP, ICMP).

- [ ] Implement features like session hijacking, SYN flood simulation, and protocol fuzzing.

- [ ] Learn how IDS/IPS detect such attacks.

## Tasks:
### Week 1:
- [x] Get the development environment ready.
	- [x] Github repo
	- [x] python3 and requirements

- [x] Learn scapy

- [x] Establish structure

- [x] Implement core recon tools
	- [x] arp_scan.py
	- [x] ping_sweep.py
	- [x] tcp_syn_scan.py
	- [x] tcp_connect_scan.py
	- [x] udp_scan.py
	- [x] os_fingerprint.py
	- [x] traceroute.py
- [x] Tests
### Week 2:
- [ ] Attack Implementation
	- [ ] syn_flood.py
	- [ ] icmp_flood.py
	- [ ] land.py
	- [ ] smurf.py
	- [ ] fraggle.py
	- [ ] tcp_reset.py
	- [ ] arp_poisoning.py
	- [ ] dns_spoof.py
- [ ] Tests
- [ ] Evasion techniques
	- [ ] fragmentation.py
	- [ ] ttl_manipulation.py
	- [ ] checksum_evasion.py
	- [ ] timing_delay.py
	- [ ] decoy_scan.py
	- [ ] tcp_flags.py
- [ ] Tests
### Week 3:
- [ ] Build CLI structure with Click, add commands for each recon tool
- [ ] Add attack and evasion subcommands with options
- [ ] Rich Logging & Output
	- [ ] Color-coded statuses (success, info, error)
	- [ ] Progress bars or live panels if useful
	- [ ] Output tables or trees for results
- [ ] Final tests
###Extra
- [ ] Add threads
- [ ] Add nmap
- [ ] Add phone detection
