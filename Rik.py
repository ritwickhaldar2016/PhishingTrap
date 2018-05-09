# coding: utf-8
import os
import sys
import time



print(""" \033[1;36m
┌══════════════════════════════════════════════════════════════┐
█                                                              █
                       RIK.PY                                 	          		 Created By Rikon and @skynight			
└══════════════════════════════════════════════════════════════┘     \033[1;m""")


print("\033[1;34m\n[++] Starting Mysql ... \033[1;m")
time.sleep(2)
os.system("service mysql start&")
print("\033[1;34m\n[++] Initializing Php ... \033[1;m")
input()
print("\033[1;34m\n[++] Enter The path of the file ... \033[1;m")
path=input()
print("\033[1;34m\n[++] Enter The Address Ex. 127.0.0.1:80 ... \033[1;m")
add=input()
php=os.system("php -t "+path+" -S "+add+" &")
input()
print("\033[1;34m\n[++] Enter The NGROK PORT Ex 80 ... \033[1;m")

port=input()

os.system("./ngrok http "+port+"")

print("\033[1;34m\n[++] Killing Process mysql ... \033[1;m")
time.sleep(1)
os.system("pkill mysql")
print("\033[1;34m\n[++] Killing Process Php ... \033[1;m")
time.sleep(1)
os.system("pkill php*")

print("\033[1;34m\n[++] Done ... \033[1;m")

