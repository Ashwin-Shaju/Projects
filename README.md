# Ethical Hacking Mini Projects (Python)

## 📌 Overview
This repository contains Python-based ethical hacking and cybersecurity mini projects developed for educational purposes. The projects focus on **system security monitoring** and **network reconnaissance**, which are core concepts in ethical hacking and intrusion detection systems.

All tools in this repository are intended to be used **only on systems with proper authorization**.

---

## 🛠️ Projects Included

---

### 🛡️ 1. File Integrity Monitoring System
The File Integrity Monitoring System is a defensive security tool that monitors specified files for unauthorized modifications using cryptographic hashing (SHA-256). This technique is commonly used in intrusion detection systems (IDS) to detect malware activity or unauthorized access.

**Key Features**
- Monitors selected files for unauthorized changes
- Uses SHA-256 hashing for integrity verification
- Detects and alerts on file modification
- Continuous real-time monitoring

**Concepts Used**
- Cryptographic hashing
- File system monitoring
- Intrusion detection fundamentals

**How to Run**
```bash
python file_integrity_monitor.py


**🔐 2. Multithreaded Port Scanner**

The Multithreaded Port Scanner is a network reconnaissance tool that scans a target system to identify open TCP ports. It uses multithreading to improve scanning speed and optionally performs basic banner grabbing to identify running services.

**Key Features**

Scans common TCP ports (20–1024)

Uses multithreading for faster execution

Detects open ports

Performs basic service/banner detection

**Concepts Used**

Socket programming

Multithreading

Network reconnaissance

**How to Run**

python port_scanner.py
