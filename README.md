
# 🦈 S-PUP (SHARK PUP)


![S-PUP Logo](S-PUP.png)

**By Anas Labrini**  
_"From nothing we make everything."_

---

## 📜 Overview

**S-PUP (SHARK PUP)** is an advanced surveillance and persistence Python-based tool designed for **red team** operations, combining powerful keylogging, system reconnaissance, stealth, and dynamic encryption mechanisms. It includes both encryption utilities and a full persistence-enabled logger that can also perform system information harvesting and evade analysis.

---

## 📁 Project Structure

```
S-PUP/
├── en.py               # AES encryptor with self-rebuilding script capabilities
└── tool/
    └── S-PUP.py        # Main keylogger and persistence tool
```

---

## 🔐 `en.py` - AES Encryptor

### 🔧 Features
- Encrypts any Python script using AES (CBC mode) with a dynamically generated key.
- Creates a self-decrypting script (`S-PUP_AES.py`).
- Option to convert the final encrypted script into a `.exe` using PyInstaller.
- Uses system details (hostname, OS, CPU) to generate encryption key.
- For example, guards monitor their leader, and if they can't find him or he dies, one of the guards takes over and revives him.

### ▶️ Usage
```bash
python3 en.py
```
You will be prompted to enter the path to the target Python script.

---

## 🧠 `S-PUP.py` - Surveillance & Persistence

### 🎯 Capabilities
- **Keylogger**: Logs keystrokes in real-time and sends logs via email.
- **Email Integration**: Sends logs, system details, and browser credential files.
- **System Reconnaissance**:
  - OS version, architecture, user info
  - Internal/external IP, MAC address
  - Installed programs, active processes
  - Desktop/Downloads file listing
  - Wi-Fi networks (Linux)
- **Browser Data**:
  - Copies Chrome and Firefox login/password files
- **Stealth & Evasion**:
  - Anti-debugging & anti-analysis (kills tools like Wireshark, GDB, etc.)
  - Deletes known reverse engineering tools if permissions allow
- **Persistence**:
  - Auto-start via systemd on Linux, Startup folder on Windows, and LaunchAgent on macOS
  - Creates multiple hidden backups
  - Watchdog mode to restore if main script is deleted
- **Self-Updating**:
  - Auto-checks GitHub for updates hourly

### ▶️ Usage
```bash
python3 S-PUP.py
```

> On first run, it installs itself as a persistent background service depending on the OS.

---

## ⚙️ Configuration

Edit the following in `S-PUP.py`:
```python
EMAIL_ADDRESS = "default_email"
EMAIL_PASSWORD = "default_password"
TO_EMAIL = "default_receiver"
```

Update the GitHub auto-update link:
```python
update_url = "https://raw.githubusercontent.com/anaslabrini/S-PUP/refs/heads/main/tool/S-PUP.py"
```

---

## 🛡 Anti-Analysis Features

- Process scan and kill:
  - e.g., `wireshark`, `gdb`, `IDA`, `ghidra`, `sandboxie`, `vboxservice`, `frida`
- Deletes apps from known paths if permissions allow

---

## 📤 Email Report Example

- `keylogs_TIMESTAMP.txt` with recorded keystrokes
- System info report body
- Attached files from browser paths (Login Data, logins.json, etc.)

---

## 🚀 Persistence Details

| OS        | Method                      |
|-----------|-----------------------------|
| **Linux** | `systemd --user` service    |
| **Windows** | Startup `.bat` file       |
| **macOS** | `LaunchAgent` plist         |

Backups are created in:
- `~/.config/.cache/`
- `~/.local/share/.logs/`
- etc.

---

## 🧪 Watcher Mode

If the main script is deleted, the watchers upgrade themselves to the base system and restore service.

### Run Watcher:
```bash
python3 S-PUP.py --watcher
```

---

## 🧩 Dependencies

- `pynput`
- `psutil`
- `smtplib`
- `requests`
- `pycryptodome`
- `PyInstaller` (optional)

Install with:
```bash
pip install pynput psutil requests pycryptodome
```

---
## ⚖️ License

This project is licensed under the **Red Team Research License (RTR-License)**.

You are permitted to:
- Use, modify, and extend this tool **for educational purposes, ethical hacking, and Red Team simulation, provided you acknowledge the source**.
- Share the code with credit to the original author.

You are strictly prohibited from:
- Use this tool for any illegal activity, real-world surveillance, or unauthorized access to systems.
- Sell or distribute this tool for malicious purposes.

Any violation of these terms voids the license and gives the author the right to take legal action or publicly disclose any misuse.

---

## ⚠️ Legal Disclaimer

> ⚠ **WARNING: FOR AUTHORIZED USE ONLY**

This software is provided exclusively for the following purposes:
- **Educational Purposes**
- **Cybersecurity Research**
- **Forcing recruitment and penetration testing on systems you own or expressly authorize**

**Unauthorized dissemination**, use against third-party infrastructure, espionage, or malicious espionage:
- Is a **criminal offense**
- Reported to the relevant authorities
- May result in **serious legal consequences**

The author (**Anass Labriny**) assumes **no responsibility** for any misuse, damages, or legal claims arising from the use of this tool.

**You have been warned.**

This tool is intended exclusively for **educational** and **forcing** authorized purposes.
**Unauthorized use is illegal.** The author is not responsible for misuse. ---

## 🧠 Author

**Anas Labrini**  
18 years old | Red Team Cybersecurity Researcher  
Salé, Morocco 🇲🇦  
GitHub: [anaslabrini](https://github.com/anaslabrini)
Instagram: [anasans005](https://www.instagram.com/anasans005?igsh=dzNsOXN3Nm9INmVk)
WebSite: [anaslabrini](https://anaslabrini.netlify.app)

