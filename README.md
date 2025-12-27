# Ethical Hacking Mini Projects (Python)

## 📌 Overview
This repository contains Python-based ethical hacking and cybersecurity mini projects developed for educational purposes. The projects focus on **system security monitoring** and **network reconnaissance**, which are core concepts in ethical hacking and intrusion detection systems.

All tools in this repository are intended to be used **only on systems with proper authorization**.

---

## 🛠️ Projects Included

# 1. File Integrity Monitoring System (Python)

## 📌 Overview
The File Integrity Monitoring System is a Python-based security tool designed to detect unauthorized changes in files. It works by calculating and comparing cryptographic hash values to ensure file integrity. This concept is widely used in intrusion detection systems (IDS) and malware detection.

This project is intended strictly for educational and authorized security monitoring purposes.

---

## ⚙️ Features
- Monitors specified files for unauthorized modifications
- Uses SHA-256 hashing to verify file integrity
- Detects changes and raises alerts instantly
- Continuously monitors files in real time
- Lightweight and easy to configure

---

## 🧠 Concepts Used
- Cryptographic hashing (SHA-256)
- File system monitoring
- Intrusion detection fundamentals
- Defensive cybersecurity techniques

---

## 🛠️ Technologies Used
- Python 3
- hashlib module
- os module
- time module

---

## ▶️ How to Run

### 1️⃣ Setup
Create or choose a file to monitor (example: `test.txt`) and add it to the script:
```python
FILES_TO_MONITOR = ["test.txt"]


# 2.Multithreaded Port Scanner (Python)

## 📌 Overview
The Multithreaded Port Scanner is a Python-based network reconnaissance tool designed for ethical hacking and cybersecurity learning. It scans a target system to identify open TCP ports and optionally performs basic banner grabbing to detect running services.

This project is intended strictly for educational purposes and authorized security testing.

---

## ⚙️ Features
- Scans common TCP ports (20–1024)
- Uses multithreading for faster scanning
- Detects open ports on a target system
- Attempts basic service/banner detection
- Lightweight and easy to use

---

## 🧠 Concepts Used
- Socket programming
- Multithreading
- Network reconnaissance
- Timeout handling

---

## 🛠️ Technologies Used
- Python 3
- socket module
- threading module

---

## ▶️ How to Run

### 1️⃣ Run the Program
```bash
python port_scanner.py
