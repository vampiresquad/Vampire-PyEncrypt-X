#!/usr/bin/env python3

import os
import sys
import time
import shutil
import subprocess
from pathlib import Path
from termcolor import cprint, colored

OUTPUT_DIR = "output"
Path(OUTPUT_DIR).mkdir(parents=True, exist_ok=True)


def banner():
    os.system("clear" if os.name == "posix" else "cls")
    cprint(r"""
 ██    ██  █████  ███    ███ ██████  ██ ██████  ███████ ██████   █████  
 ██  ██  ██   ██ ██  ██  ██ ██   ██ ██ ██      ██      ██   ██ ██   ██ 
 █████   ███████ ██  ██  ██ ██   ██ ██ ██      █████   ██████  ███████ 
 ██  ██  ██   ██ ██  ██  ██ ██   ██ ██ ██      ██      ██   ██ ██   ██ 
 ██    ██ ██   ██ ████  ████ ██████  ██ ██████ ███████ ██   ██ ██   ██

   Advanced Python Encryptor | Coded by: Muhammad Shourov (VAMPIRE)
""", "magenta")


def wait(msg):
    print(colored(f"[*] {msg}", "yellow"))
    time.sleep(0.8)


def encrypt_with_pyarmor(filepath):
    wait("Encrypting with PyArmor...")
    encrypted_dir = os.path.join(OUTPUT_DIR, "pyarmor")
    os.makedirs(encrypted_dir, exist_ok=True)
    try:
        subprocess.run(["pyarmor", "gen", "--output", encrypted_dir, filepath], check=True)
        print(colored("[+] PyArmor encryption done! File saved in output/pyarmor/", "green"))
    except subprocess.CalledProcessError:
        print(colored("[!] PyArmor encryption failed. Is pyarmor installed?", "red"))


def encrypt_with_cython(filepath):
    wait("Encrypting to Binary with Cython...")
    try:
        from Cython.Build import cythonize
        import setuptools
        import distutils.core

        temp_dir = "cy_build"
        os.makedirs(temp_dir, exist_ok=True)

        setup_code = f"""
from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize("{filepath}")
)
"""
        with open(os.path.join(temp_dir, "setup.py"), "w") as f:
            f.write(setup_code)

        subprocess.run(["python3", "setup.py", "build_ext", "--inplace"], cwd=temp_dir, check=True)

        for file in os.listdir(temp_dir):
            if file.endswith(".so") or file.endswith(".pyd"):
                shutil.move(os.path.join(temp_dir, file), OUTPUT_DIR)

        print(colored("[+] Cython encryption done! Output saved in output/", "green"))
    except Exception as e:
        print(colored(f"[!] Cython encryption failed: {e}", "red"))


def obfuscate_with_base64(filepath):
    wait("Obfuscating with Base64...")
    try:
        import base64
        with open(filepath, "rb") as f:
            encoded = base64.b64encode(f.read()).decode("utf-8")

        output_file = os.path.join(OUTPUT_DIR, Path(filepath).stem + "_obf.py")
        with open(output_file, "w") as f:
            f.write(f"import base64\nexec(base64.b64decode('{encoded}'))\n")

        print(colored("[+] Base64 obfuscation done! File saved in output/", "green"))
    except Exception as e:
        print(colored(f"[!] Base64 obfuscation failed: {e}", "red"))


def main():
    banner()
    print(colored("[1] Encrypt with PyArmor (Recommended)", "cyan"))
    print(colored("[2] Encrypt to Binary (Cython)", "cyan"))
    print(colored("[3] Obfuscate with Base64", "cyan"))
    print(colored("[4] Exit", "cyan"))

    choice = input(colored("\nSelect an option: ", "yellow")).strip()

    if choice not in ["1", "2", "3"]:
        print(colored("[!] Exiting...", "red"))
        return

    filepath = input(colored("Enter your Python file path: ", "yellow")).strip()

    if not os.path.isfile(filepath):
        print(colored("[!] Invalid file path.", "red"))
        return

    if choice == "1":
        encrypt_with_pyarmor(filepath)
    elif choice == "2":
        encrypt_with_cython(filepath)
    elif choice == "3":
        obfuscate_with_base64(filepath)

    input(colored("\n[+] Press Enter to return to menu...", "blue"))
    main()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(colored("\n[!] Interrupted by user. Exiting...", "red"))
