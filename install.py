# coding: utf-8
import os 
import sys
import time


print(""" \033[1;36m
┌══════════════════════════════════════════════════════════════┐
█                                                              █
█                     INSTALLING THE TOOLS                     █
                   Created By Rikon and @skynight	  		
└══════════════════════════════════════════════════════════════┘     \033[1;m""")


print("\033[1;34m\n[++] Installing apache2 ... \033[1;m")
time.sleep(2)
apache=os.system("apt-get install  apache2")
time.sleep(1)

print("\033[1;34m\n[++] Installing python3 ... \033[1;m")
time.sleep(2)
apache=os.system("apt-get install  python3")
time.sleep(1)

print("\033[1;34m\n[++] Installing php ... \033[1;m")
time.sleep(2)
php=os.system("apt-get install  php")
time.sleep(1)

print("\033[1;34m\n[++] Installing mysql ... \033[1;m")
time.sleep(2)
mdb=os.system("apt-get install mariadb-server")
time.sleep(1)

print("\033[1;34m\n[++] Install Wget ... \033[1;m")
time.sleep(2)
mdb=os.system("apt-get install  wget")
time.sleep(1)

print("\033[1;34m\n[++] Downloading Ngrok for amd ... \033[1;m")
time.sleep(2)
wget=os.system("wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip")
time.sleep(1)

print("\033[1;34m\n[++] Unzipping Ngrok amd64 ... \033[1;m")
time.sleep(3)
mdb=os.system("unzip ngrok*")
time.sleep(1);

print("\033[1;34m\n[++] Instalation Completed ... \033[1;m")
