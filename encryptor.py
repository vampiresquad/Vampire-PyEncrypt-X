#!/usr/bin/env python3 import os import sys import time import shutil import subprocess from pathlib import Path from termcolor import cprint, colored

OUTPUT_DIR = "output"

Ensure output directory exists

Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)

def banner(): os.system("clear") cprint(""" ██    ██  █████  ███    ███ ██████  ██ ██████  ███████ ██████   █████  ██   ██ ██    ██ ██   ██ ████  ████ ██   ██ ██ ██   ██ ██      ██   ██ ██   ██ ██  ██ ██    ██ ███████ ██ ████ ██ ██████  ██ ██████  █████   ██████  ███████ █████
██  ██  ██   ██ ██  ██  ██ ██   ██ ██ ██      ██      ██   ██ ██   ██ ██  ██ ████   ██   ██ ██      ██ ██████  ██ ██      ███████ ██   ██ ██   ██ ██   ██

Advanced Python Encryptor | Coded by: Muhammad Shourov (VAMPIRE)

""", "magenta")

def wait(msg): print(colored(f"[*] {msg}", "yellow")) time.sleep(1)

def encrypt_with_pyarmor(filepath): wait("Encrypting with PyArmor...") encrypted_dir = os.path.join(OUTPUT_DIR, "pyarmor") os.makedirs(encrypted_dir, exist_ok=True) try: subprocess.run(["pyarmor", "gen", "--output", encrypted_dir, filepath], check=True) print(colored("[+] PyArmor encryption done! File saved in output/pyarmor/", "green")) except subprocess.CalledProcessError: print(colored("[!] PyArmor encryption failed. Is pyarmor installed?", "red"))

def encrypt_with_cython(filepath): wait("Encrypting to Binary with Cython...") try: from Cython.Build import cythonize import setuptools import distutils.core

temp_dir = "cy_build"
    os.makedirs(temp_dir, exist_ok=True)

    with open(os.path.join(temp_dir, "setup.py"), "w") as f:
        f.write(f"""

from setuptools import setup from Cython.Build import cythonize

setup( ext_modules = cythonize('{filepath}') ) """)

subprocess.run(["python3", "setup.py", "build_ext", "--inplace"], cwd=temp_dir, check=True)
    for file in os.listdir(temp_dir):
        if file.endswith(".so") or file.endswith(".pyd"):
            shutil.move(os.path.join(temp_dir, file), OUTPUT_DIR)
    print(colored("[+] Cython encryption done! Output saved in output/", "green"))
except Exception as e:
    print(colored(f"[!] Cython encryption failed: {e}", "red"))

def obfuscate_with_base64(filepath): wait("Obfuscating with Base64...") try: import base64 with open(filepath, "rb") as f: encoded = base64.b64encode(f.read()).decode("utf-8")

output_file = os.path.join(OUTPUT_DIR, Path(filepath).stem + "_obf.py")
    with open(output_file, "w") as f:
        f.write("import base64\nexec(base64.b64decode('" + encoded + "'))")
    print(colored("[+] Base64 obfuscation done! File saved in output/", "green"))
except Exception as e:
    print(colored(f"[!] Base64 obfuscation failed: {e}", "red"))

def main(): banner() print("[1] Encrypt with PyArmor (Recommended)") print("[2] Encrypt to Binary (Cython)") print("[3] Obfuscate with Base64") print("[4] Exit")

choice = input(colored("\nSelect an option: ", "cyan"))
if choice not in ["1", "2", "3"]:
    print(colored("[!] Exiting...", "red"))
    return

filepath = input(colored("Enter your Python file path: ", "yellow"))
if not os.path.isfile(filepath):
    print(colored("[!] Invalid file path.", "red"))
    return

if choice == "1":
    encrypt_with_pyarmor(filepath)
elif choice == "2":
    encrypt_with_cython(filepath)
elif choice == "3":
    obfuscate_with_base64(filepath)

input(colored("\nPress Enter to continue...", "blue"))

if name == "main": try: main() except KeyboardInterrupt: print(colored("\n[!] Interrupted by user. Exiting...", "red"))

