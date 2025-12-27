# Ethical Hacking Mini Projects (Python)

## Overview
This repository contains Python-based ethical hacking and cybersecurity mini projects developed for educational purposes.
The projects focus on system security monitoring and network reconnaissance, which are core concepts in ethical hacking
and intrusion detection systems (IDS).

Disclaimer:
All tools in this repository must be used only on systems you own or have explicit permission to test.

--------------------------------------------------

## Projects Included

--------------------------------------------------
1. File Integrity Monitoring System (Python)
--------------------------------------------------

Overview:
The File Integrity Monitoring System is a Python-based defensive security tool that detects unauthorized file
modifications. It works by calculating and comparing SHA-256 hash values to ensure file integrity.

This concept is widely used in:
- Intrusion Detection Systems (IDS)
- Malware detection
- Server security monitoring

Features:
- Monitors specified files for unauthorized changes
- Uses SHA-256 cryptographic hashing
- Detects file modification, deletion, or tampering
- Continuous real-time monitoring
- Lightweight and easy to configure

Concepts Used:
- Cryptographic hashing (SHA-256)
- File system monitoring
- Integrity verification
- Defensive cybersecurity techniques

Technologies Used:
- Python 3
- hashlib module
- os module
- time module

How to Run:

1. Setup
Create or choose a file to monitor (example: test.txt) and add it inside the script:

FILES_TO_MONITOR = ["test.txt"]

2. Run the Program
python file_integrity_checker.py

--------------------------------------------------
2. Multithreaded Port Scanner (Python)
--------------------------------------------------

Overview:
The Multithreaded Port Scanner is a Python-based network reconnaissance tool designed for ethical hacking
and cybersecurity learning. It scans a target host to identify open TCP ports and optionally performs
basic banner grabbing to detect running services.

This project is intended strictly for educational and authorized security testing purposes.

Features:
- Scans common TCP ports (20–1024)
- Uses multithreading for faster scanning
- Identifies open ports on a target system
- Performs basic service/banner detection
- Simple and lightweight implementation

Concepts Used:
- Socket programming
- Multithreading
- Network reconnaissance
- Timeout handling

Technologies Used:
- Python 3
- socket module
- threading module

How to Run:

1. Run the Program
python port_scanner.py

2. Enter Target Details
- Target IP or hostname
- Port range (default: 20–1024)

--------------------------------------------------

Educational Purpose:
These projects are built to strengthen cybersecurity fundamentals, demonstrate ethical hacking techniques,
and help students understand real-world security tools.

--------------------------------------------------

Legal and Ethical Notice:
Unauthorized scanning or monitoring of systems you do not own is illegal.
Always obtain proper authorization before performing any security testing.
