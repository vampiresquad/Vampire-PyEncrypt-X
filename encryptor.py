#!/usr/bin/env python3

import os
import time
import shutil
import sys

RED, GRN, YLW, BLU, RST = '\033[91m', '\033[92m', '\033[93m', '\033[94m', '\033[0m'

def banner():
    os.system("clear")
    print(f"""{RED}
██    ██  █████  ███    ███ ██████  ██ ██████  ███████ ██████   █████  ██   ██
██    ██ ██   ██ ████  ████ ██   ██ ██ ██   ██ ██      ██   ██ ██   ██ ██  ██ 
██    ██ ███████ ██ ████ ██ ██████  ██ ██   ██ █████   ██████  ███████ █████  
 ██  ██  ██   ██ ██  ██  ██ ██   ██ ██ ██   ██ ██      ██   ██ ██   ██ ██  ██ 
  ████   ██   ██ ██      ██ ██████  ██ ██████  ███████ ██   ██ ██   ██ ██   ██
{RST}             {BLU}Advanced Python Encryptor | Coded by: Muhammad Shourov (VAMPIRE){RST}
    """)

def setup():
    os.system("pip install pyarmor cython > /dev/null 2>&1")

def choose_file():
    try:
        path = input(f"{YLW}Enter your Python file path: {RST}")
        if not os.path.isfile(path):
            print(f"{RED}File not found!{RST}")
            return None
        return path
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit()

def encrypt_with_pyarmor(script_path):
    os.makedirs("output/pyarmor", exist_ok=True)
    os.system(f"pyarmor gen --entry {script_path} --output output/pyarmor")
    print(f"{GRN}PyArmor encryption done! File saved in output/pyarmor/{RST}")

def encrypt_with_cython(script_path):
    os.makedirs("output/cython", exist_ok=True)
    name = os.path.basename(script_path).replace('.py', '')
    c_file = f"{name}.c"
    os.system(f"cython --embed -o {c_file} {script_path}")
    os.system(f"gcc -o output/cython/{name} {c_file} $(python3-config --cflags --ldflags)")
    os.remove(c_file)
    print(f"{GRN}Cython Binary encryption done! File saved in output/cython/{name}{RST}")

def encrypt_with_base64(script_path):
    os.makedirs("output/base64", exist_ok=True)
    out_file = f"output/base64/encoded_{os.path.basename(script_path)}"
    with open(script_path, 'r') as f:
        content = f.read()
    encoded = content.encode('utf-8')
    import base64
    encoded_text = base64.b64encode(encoded).decode('utf-8')
    with open(out_file, 'w') as f:
        f.write(f"import base64\nexec(base64.b64decode('{encoded_text}').decode('utf-8'))")
    print(f"{GRN}Base64 obfuscation done! File saved in {out_file}{RST}")

def main():
    banner()
    setup()
    while True:
        print(f"""{BLU}
[1] Encrypt with PyArmor (Recommended)
[2] Encrypt to Binary (Cython)
[3] Obfuscate with Base64
[4] Exit
{RST}""")
        choice = input(f"{YLW}Select an option: {RST}")
        if choice in ['1', '2', '3']:
            file = choose_file()
            if file:
                if choice == '1':
                    encrypt_with_pyarmor(file)
                elif choice == '2':
                    encrypt_with_cython(file)
                elif choice == '3':
                    encrypt_with_base64(file)
        elif choice == '4':
            print(f"{GRN}Goodbye!{RST}")
            break
        else:
            print(f"{RED}Invalid choice! Try again.{RST}")
        input(f"{YLW}Press Enter to continue...{RST}")
        banner()

if __name__ == "__main__":
    main()
