# Remote Access Trojan (RAT)

Remote Access Trojan is a lightweight **Remote Access Tool (RAT)** built in Python, enabling command-and-control communication between a client and a server over a TCP connection. It allows secure remote file access, shell command execution, directory browsing, system information retrieval, screenshot capture, and more.

> ⚠️ This project is for **educational** and **authorized** use only.

![Picture of application](https://github.com/user-attachments/assets/9c5068ea-d897-469e-983d-233aaefd8555)

---

## 🚀 Features

- 📁 **Directory Listing** — Remotely list files in the target directory.
- 💻 **Shell Access** — Execute shell commands remotely, with directory change support.
- 📤 **File Download** — Download files from the client to the server.
- 📥 **File Upload** — Upload files to the client machine.
- ❌ **File Deletion** — Delete unwanted files remotely.
- 🖥️ **Screenshot Capture** — Take real-time screenshots of the client’s desktop.
- 🧠 **System Info** — Get platform, user, hostname, and working directory.
- 🔒 **Stealth Mode** — Fails silently if the server isn't available.

---

## 🛠️ Technologies Used

- **Python** — Cross-platform scripting and automation.
- **Sockets** — For TCP client-server communication.
- **Subprocess & OS** — Shell interaction and file system operations.
- **PyAutoGUI** — Capture client screenshots.

---

## 📦 Installation

### Clone the repository:
bash
```
git clone https://github.com/YourUsername/Remote-Access-Trojan.git
cd Remote-Access-Trojan
```
Create EXE
```
pyinstaller --noconsole --onefile client.py
```
💡 Use --noconsole to hide the command prompt (on Windows only).
Make sure PyInstaller is installed:
pip install pyinstaller

## ▶️ Usage
Server:
You’ll need a separate server implementation that listens for connections and issues commands like LIST_DIR, GET_INFO, SHELL, etc.

This repo currently focuses on the client.

Client:
You can run the client in two ways:

Run via Python:

```
python client.py
```
Run compiled executable:
```
./client.exe
```
Once launched, the client connects to the specified server IP/port and waits for incoming commands.

## ⚠️ Legal Disclaimer
This software is created strictly for educational purposes and ethical penetration testing.
Do not use this tool on any system without explicit written permission.

Unauthorized use may be illegal and could result in criminal charges.

## 🛡️ Defense & Detection
To protect systems from RATs like this, follow cybersecurity best practices:

Antivirus & EDR — Use up-to-date security tools to detect behavior like reverse shells and file exfiltration.

Firewall Rules — Block suspicious outbound traffic and restrict high-risk ports.

User Awareness — Train users not to run unknown .exe or .py files.

Process Monitoring — Watch for hidden background scripts with no UI.

Network Monitoring — Set up IDS/IPS to detect unauthorized TCP connections.

Script Blocking — Use AppLocker or Group Policy to block interpreters like Python on non-dev machines.

Email Filtering — Sandboxing and attachment scanning help stop malware at the gate.

## 📘 Why This Exists
This project was created to learn more about Remote Access Trojans — and how to defend against them.
Use it responsibly, and only in environments where you have permission.
