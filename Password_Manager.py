import os
import secrets
import string
import platform
import pyperclip as pc

def Get_Os_Path(OS):
    if OS == "Windows":
        path = f"C:/Users/OneDrive/{username}/Desktop/AUTOPLAY2/"
        if not os.path.isdir(f"C:/Users/OneDrive/{username}/Desktop/AUTOPLAY2"):
            os.mkdirs(path)
    else:
        path = f"/home/{username}/Desktop/AUTOPLAY2/"
    return path

def OpenFile(OS):
    if OS == "Windows":
        os.startfile(path)
    elif OS == "Linux":
        opener = "xdg-open" if os.path.exists("/usr/bin/xdg-open") else "gnome-open"
        os.system(f"{opener} {path}")
    else:
        print("Your operative system cannot be determined")

def Pass_Gen(pass_length):
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation
    abc = letters + digits + string.punctuation
    password = ''

    for i in range(int(pass_length)):
        password += ''.join(secrets.choice(abc))
    return password

OS = platform.uname()[0]
username = os.getlogin()
path = Get_Os_Path(OS)

nombre_archivo = input(str("type the name of the file: (without \".txt\") "))
path = os.path.join(path, f"{nombre_archivo}.txt")
gmail = input("Type your email: ")
Nombre_de_usuario = input("Type your username (If it isn't required press 'ENTER'): ")
pass_length = input("Type how many characters you want your password to be: ")

password = Pass_Gen(pass_length)

with open(path, "w") as f:
    f.write(gmail + "\n\n" + Nombre_de_usuario + "\n\n\n" + password)

OpenFile(OS)
pc.copy(password)