import os
import platform
import shutil
import subprocess
import sys
import zipfile

from sys import platform as _platform
from os import system

print('You are Running on a', platform.system(), 'System')
#path1="1.sh"
#path2="Secret.png"

def clear():
    if _platform == "linux" or _platform == "linux2" or _platform == "darwin":
        system('clear')
    if _platform == "win32":
        system('cls')

clear()
path1 = input("Enter the path to the File/Files to be hidden: ")
path2 = input("Enter the path to the file in which you want to hide the files:")
filename, file_extension = os.path.splitext(path2)
clear()

def writesh():
    print('Creating Custom Command')
    try:
        file = open('command.sh', 'w')
        file.close()
    except:
        print('Something Went Wrong!')
        sys.exit(0)
def zippp():
    secretfiles = zipfile.ZipFile('secret.zip', mode='w')
    # os.chdir(path1)

    try:
        print('Zipping File ', path1)
        secretfiles.write(path1)

    finally:
        print('Closing')
        secretfiles.close()



if os.path.isdir(path1):
    print("\n Directory Found")
    print("\n Zipping Directory")
    #zippp()
    shutil.make_archive('secret', 'zip', path1)
    if _platform == "linux" or _platform == "linux2" or _platform == "darwin":
        print('Linux/Unix System Found')
        #subprocess.call([ "echo", path2, "secret.zip > output"+file_extension])
        writesh()
        file = open("command.sh","w")
        file.write("#!/bin/bash")
        com = "\n cat " + path2 + " secret.zip "+ " > output"+file_extension
        file.write(com)
        file.close()
        subprocess.call(["bash","command.sh"])
        print("output"+file_extension + " Contains your hidden flies :)")
        exit

    if _platform == "win32":
        exit
        #os.system('echo $path2')


elif os.path.isfile(path1):
    print("\n File Found")
    if _platform == "linux" or _platform == "linux2" or _platform == "darwin":
        print('Linux/Unix System found')
        #subprocess.call(["cat", path2, path1, "output"+file_extension])
        writesh()
        file = open("command.sh","w")
        file.write("#!/bin/bash")
        com = "\n cat " + path2 + " " + path1 + " > output"+file_extension
        file.write(com)
        file.close()
        subprocess.call(["bash","command.sh"])
        print("output"+file_extension + " Contains your hidden flies :)")

        exit

    if _platform == "win32":
        exit
else:
    print("\nSomehow the input was neither a file or path.\nIs the path correct?")
