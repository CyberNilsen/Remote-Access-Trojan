# Remote Access Trojan (RAT)

Remote Access Trojan is a lightweight Remote Access Tool (RAT) built in Python, enabling command-and-control communication between a client and a server over a TCP connection. It allows secure, remote file access, shell command execution, directory browsing, system information retrieval, screenshots, and more. This project is for **educational and authorized use only**.

![Picture of application](https://github.com/user-attachments/assets/9c5068ea-d897-469e-983d-233aaefd8555)


---

## Features

- 📁 **Directory Listing**: Remotely list files in the target directory.
- 💻 **Shell Access**: Execute shell commands remotely, with directory change support.
- 📤 **File Download**: Download files from the client to the server.
- 📥 **File Upload**: Upload files to the client machine.
- ❌ **File Deletion**: Delete unwanted files remotely.
- 🖥️ **Screenshot Capture**: Take real-time screenshots of the client’s desktop.
- 🧠 **System Info**: Get platform, user, hostname, and working directory.
- 🔒 **Stealth Mode**: Fails silently if the server isn't available.

---

## Technologies

- **Python**: Cross-platform scripting and socket programming.
- **Sockets**: For TCP client-server communication.
- **Subprocess & OS**: Execute commands and interact with the file system.
- **PyAutoGUI**: Capture screenshots from the client machine.

---

## Installation

### Clone the repository:
```bash
git clone https://github.com/YourUsername/Remote-Access-Trojan.git
cd Remote-Access-Trojan```

##⚠️ Legal Disclaimer
This software is created strictly for educational purposes and ethical penetration testing.
Do not use this tool on any system without explicit written permission.

Unauthorized use may be illegal and could result in criminal charges.

🛡️ Defense & Detection
To protect against Remote Access Trojans like this one, consider the following practices:

Antivirus & Endpoint Detection: Use modern antivirus software and EDR (Endpoint Detection & Response) tools that detect suspicious behavior like reverse shells or file exfiltration.

Firewall Rules: Restrict outbound connections and monitor traffic for unusual IPs or ports.

User Awareness: Educate users to avoid running unknown .exe files or Python scripts, especially those from email attachments or downloads.

Process Monitoring: Look for hidden or suspicious processes (e.g., Python scripts running in background with no GUI).

Network Monitoring: Set up IDS/IPS systems to flag unusual or unauthorized TCP connections from internal hosts.

Software Restriction Policies: Block script interpreters (e.g., Python) in non-dev environments using Group Policy or AppLocker.

Email Filtering & Sandboxing: Detect and quarantine potential malware before it reaches the user.
