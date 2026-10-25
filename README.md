# Network Port Checker

A beginner-friendly Python TCP port checker that checks a small list of ports **on the local computer only** (`127.0.0.1`).

This project is part of my hands-on IT and cybersecurity learning portfolio.

## What it does
- Tests TCP connectivity to ports **21, 22, 53, 80, 443, 3389, and 8080** on localhost
- Prints `OPEN` if a TCP connection succeeds
- Prints `Not open or unreachable` if a connection does not succeed within one second

**Important:** This is not a vulnerability scanner. It does not identify which service is running or whether the system is secure. A TCP connect check also cannot accurately assess UDP services.

## Requirements
- Python 3
- No third-party packages

## Run it

Open PowerShell or a terminal in the repository folder:

```powershell
python scanner.py
```

On Windows, `py scanner.py` may also work.

## Example output

```text
Local Network Port Checker
Scanning 127.0.0.1
-----------------------------------
Port 21: Not open or unreachable
Port 22: Not open or unreachable
Port 53: Not open or unreachable
Port 80: OPEN
Port 443: Not open or unreachable
Port 3389: Not open or unreachable
Port 8080: Not open or unreachable
-----------------------------------
Scan complete!
```

This output is **illustrative**, not an actual scan result. Results depend on what is running on your computer.

## What I practiced
- Python loops and lists
- Python's built-in `socket` module
- TCP ports and the loopback address
- Timeouts and basic troubleshooting
- Documenting a reproducible technical project

## Responsible use
The target is hard-coded to `127.0.0.1`. Only test computers and networks you own or have explicit authorization to assess.

## Next steps
- Add command-line options while maintaining safe target restrictions
- Add unit tests
- Record a sample run and explain the results
- Compare TCP and UDP concepts

## Author
**James Gamache** — BSIT student with a cybersecurity focus.

[Portfolio](https://jimmyg1983.github.io/) · [GitHub](https://github.com/Jimmyg1983)
