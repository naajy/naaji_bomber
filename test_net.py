import requests
import os

import time

print("1 ((nĕt))")
print("2 ((bot))")
print("3 ((atash))")
naaji = int(input("gozine ⇉"))

if naaji == 1:
    os.system("clear")
    os.system("pip install speedtest-cli")
    os.system("speedtest-cli")
    

if naaji == 2:
    try:
        os.system('git clone https://github.com/hosein-naaji/naaji-bobm')
        os.system('cd naaji-bobm')
    except:
        os.system('cd | cd naaji-bobm')
    os.system('pkg install python')
    os.system('pkg install git')
    os.system('python naajibom.py')

if naaji == 3:
	os.system("pkg install libcaca")
	os.system("cacafire")