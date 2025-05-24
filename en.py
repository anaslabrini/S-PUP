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


file_path = input("Enter path your script : ")
# اسم السكربت المشفر
output_file = "S-PUP_AES.py"

def clear_screen():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "nt":
        os.system("cls")

clear_screen()

print("                     From nothing we make everything")
print("""\033[91m			       vdfji\033[0m#*$pp
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
\033[91m	                Anas 45?68$7W\033[0m$9$999488 Labrini
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

print(f"\n An encrypted script has been created: {output_file}")

# اسأل المستخدم إذا كان يريد تحويله إلى EXE
to_exe = input(" Do you want to convert the file to .exe? (y/n): ").lower()
if to_exe == 'y':
    try:
        new_name = input(" Enter name for your final EXE file (without .py): ").strip()
        if not new_name.endswith(".py"):
            new_name += ".py"

    # إعادة تسمية الملف المشفر إلى الاسم الجديد
        os.rename(output_file, new_name)

        print(" Converting to EXE using PyInstaller...")
        subprocess.run(["pyinstaller", "--noconfirm", "--onefile", "--noconsole", new_name])
        print("\n The executable file was created successfully in the dist/ directory.")
    except Exception as e:
        print(f" Error converting to exe: {e}")
else:
    print(" The conversion to .exe has been cancelled.")
