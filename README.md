# Vampire-PyEncrypt-X

**Advanced Python Code Encryption Tool for Termux & Linux**  
Secure any `.py` file using 3-layered encryption: PyArmor, Cython, and Base64.  
Coded with love by [Muhammad Shourov (VAMPIRE)](https://www.facebook.com/Junior.Writer.SHourov) | [Vampire Squad](https://github.com/vampiresquad)

---

## Features

- [x] **PyArmor encryption** – Professional-level script protection
- [x] **Cython compile to binary** – Turn .py into compiled binary (.elf)
- [x] **Base64 obfuscation** – Lightweight protection
- [x] **Interactive CLI menu**
- [x] **Auto output folder**
- [x] **Fully compatible with Termux and Linux**
- [x] **Colored banner & auto-fix installer**

---

## Installation

```bash
pkg update && pkg upgrade -y
pkg install git python clang -y
pip install pyarmor cython
git clone https://github.com/vampiresquad/Vampire-PyEncrypt-X.git
cd Vampire-PyEncrypt-X
python encryptor.py
