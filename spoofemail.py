# coding: utf-8
import os 
import sys
import time


print(""" \033[1;36m
┌══════════════════════════════════════════════════════════════┐
█                                                              █
█                     	SPOOFING THE EMAIL                     █
                   Created By Rikon and @skynight	  		
└══════════════════════════════════════════════════════════════┘     \033[1;m""")


print("\033[1;34m\n[++] Spoofing email ... \033[1;m")
time.sleep(2)
apache=os.system("sendemail -f (spoof email) -t (victim email) -u (subject of massage) -m (massage) -s mail.smtp2go.com:2525 -xu (smtp2go user email) -xp(smtp2go user password)")
time.sleep(5)

print("\033[1;34m\n[++] Email sent ... \033[1;m")
