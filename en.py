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
from Crypto.Cipher import AES
import base64
import os
import subprocess
from hashlib import sha256
import platform

royal_purple = "\033[1;38;2;128;0;128m" 
royal_blue = "\033[1;34m"
red_bold="\033[1;31m"
crimson = "\033[1;38;2;220;20;60m"          
turquoise = "\033[1;38;2;64;224;208m"
blue_bold = "\033[1;38;2;0;0;139m"
reset = "\033[0m"
def clear_screen():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "nt":
        os.system("cls")
clear_screen()

print(f"""{royal_blue}                                                              
                                                                                                    
                                        .^^::..                                                    
                                        :77777!!^:.                                                
                                          .!!!!!7777!^. 
                                           :7!!!!!!!777!:                                           
                                           .7!!!!!!!!!!77!^^^^::...                                
            :~^:.                         .~7!!!!!!!!!!!!7777777777!!!~^:..                         
             .!77!^.                  .:^!77!!!!!!!!!!!!!!!!!!!!!!!!7777777!!~:..                  
               ~7777!:           .:^~!7777!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!77777!^:.               
                ^77!77!:    ..^~!77777!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!7777!^.          
                 ^777777!!!!77777!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!777!.        
                  !777777777!!!!!!!!!{crimson}From nothing we make everything{reset}{royal_blue}!!!!!!!!!!!!!!!!!!!777^{reset}           
                  ^77777777777!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!77!^.            
                  !777777!~~~!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!777!~:               
                 :77777!:      .:~7!77777777!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!7777!!^.                 
                .7777!^             !~::^~!!77777777!!!!!!!!7!77777777777!!~^.                    
               .77!~:                       ...::^^!7!!!!!!!7!~~~~~~^^:..                          
              .!~:                                .!!!!!!77!^                                     
                                                 :77!!777!:                                        
                                                ^77777!^.                                          
                                              .!77!~:.                                             
                                              ::..                                                 
                                                                                                    
                                                             {reset}                                       
{royal_blue}           __       {reset}__          __  
{royal_blue}	  (    __  /__{reset})  /  /  /__) 
{royal_blue}	 __)      /     {reset}(__/  /                          

{royal_blue}      SHARK PUP Tool by Anas Labrini - v1.7{reset}
{royal_blue}      WebSite:{reset}{crimson}  www.anaslabrini.netlify.app{reset}
{royal_blue}      Github:{reset}{crimson}   https://github.com/anaslabrini{reset}
{royal_blue}      Instagram:{reset}{crimson}anasans005{reset}
""")

file_path = input(f"{royal_blue} Enter path your script :{reset} ")
# اسم السكربت المشفر
output_file = "S-PUP_AES.py"
def pad(data):
    return data + b"\0" * (AES.block_size - len(data) % AES.block_size)
def encrypt(raw, password):
    raw = pad(raw)
    key = sha256(password.encode()).digest()
    iv = os.urandom(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted = cipher.encrypt(raw)
    return base64.b64encode(iv + encrypted).decode()
# اقرأ سكربت S-PUP الأصلي
with open(file_path, "rb") as f:
    script_data = f.read()
# توليد كلمة السر ديناميكيًا (مثال: باستخدام خصائص الجهاز)
def generate_dynamic_key():
    base = platform.node() + platform.system() + platform.processor()
    return sha256(base.encode()).hexdigest()[:32]  # 256-bit key (as hex string)
password = generate_dynamic_key()
# شفر السكربت
encrypted_code = encrypt(script_data, password)
# أنشئ سكربت مشفر
with open("S-PUP_AES.py", "w") as f:
    f.write(f'''
import base64
from Crypto.Cipher import AES
from hashlib import sha256
import platform

def unpad(data):
    return data.rstrip(b"\\0")

def generate_dynamic_key():
    base = platform.node() + platform.system() + platform.processor()
    return sha256(base.encode()).hexdigest()[:32]

def decrypt(enc, password):
    enc = base64.b64decode(enc)
    key = sha256(password.encode()).digest()
    iv = enc[:16]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = cipher.decrypt(enc[16:])
    return unpad(decrypted)

enc_code = """{encrypted_code}"""
password = generate_dynamic_key()
exec(compile(decrypt(enc_code, password), "<string>", "exec"))
''')
print(f"\n{royal_blue} An encrypted script has been created:{reset} {crimson}{output_file}{reset}")
# اسأل المستخدم إذا كان يريد تحويله إلى EXE
to_exe = input(f"\n{royal_blue} Do you want to convert the file to .exe? (y/n):{reset} ").lower()
if to_exe == 'y':
    try:
        new_name = input(f"\n{royal_blue} Enter name for your final EXE file (without .py):{reset} ").strip()
        if not new_name.endswith(".py"):
            new_name += ".py"
    # إعادة تسمية الملف المشفر إلى الاسم الجديد
        os.rename(output_file, new_name)
        print(f"\n{crimson} Converting to EXE using PyInstaller...{reset}")
        subprocess.run(["pyinstaller", "--noconfirm", "--onefile", "--noconsole", new_name])
        print(f"\n{crimson} The executable file was created successfully in the dist/ directory.{reset}")
    except Exception as e:
        print(f"\n{red_bold} Error converting to exe:{reset} {crimson}{e}{reset}")
else:
    print(f"\n{royal_blue} The conversion to .exe has been cancelled.{reset}")
