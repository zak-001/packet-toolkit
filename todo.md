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
- [x] Attack Implementation
	- [x] syn_flood.py
	- [x] icmp_flood.py
	- [x] land.py
	- [x] smurf.py
	- [x] fraggle.py
	- [x] tcp_reset.py
	- [x] arp_poisoning.py
	- [x] dns_spoof.py
- [x] Tests
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
- [ ] Refactoring
- [ ] Final tests
- [ ] correct requirements
###Extra
- [ ] Add threads
- [ ] Add nmap
- [ ] Add phone detection
###Note
arp poison detected in wireshark and others (dup detected)
