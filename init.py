#all imports
import os
import platform
from termcolor import colored
from datetime import date ,datetime
import time

#check the current os 
def check_os():
    global day
    global times
    today = date.today()
    now = datetime.now()
    times = now.strftime("%H:%M")
    day = today.strftime("%d/%m/%Y")
    myos = platform.platform()
    if "windows" in myos.lower():
        banner_win(day,times)
    elif "linux" in myos.lower():
        banner_linux(day,times)
    else:
        print(colored("You Are using %s Which Is Not Supported By The Script..."%myos,"red"))
        os.system("exit")

#codes for windows
def banner_win(day,times):
    os.system("cls")
    #ascii menu
    print(colored("########################################################################","green"))                                                               
    print(colored("#  _____  _           _____  _    _    _              _____            #","green"))
    print(colored("# |_   _|| |_  ___   |  |  ||_| _| | _| | ___  ___   |     | ___  ___  #","green"))
    print(colored("#   | |  |   || -_|  |     || || . || . || -_||   |  |  |  ||   || -_| #","green"))
    print(colored("#   |_|  |_|_||___|  |__|__||_||___||___||___||_|_|  |_____||_|_||___| #","green"))
    print(colored("#                                                                      #","green")) 
    print(colored("########################################################################","green"))
    print(colored("# Date: %s                                         Time: %s #"%(day,times),"green"))
    print(colored("#                          [1] Stagnography                            #","green"))
    print(colored("#                          [2] Cryptography                            #","green"))
    print(colored("#                          [3] Exit                                    #","green"))
    print(colored("#                                                                      #","green"))
    print(colored("########################################################################","green"))
    user = input(colored("-->> ","green"))
    if user == "1":
        stagno_linux()
    elif user == "2":
        crypto_linux()
    elif user == "3":
        os.system("exit")
    else:
        print(colored("Wrong Input...","red"))
        banner_linux(day,times)

#codes for linux
def banner_linux(day,times):
    os.system("clear")
    #ascii menu
    print(colored("########################################################################","green"))                                                               
    print(colored("#  _____  _           _____  _    _    _              _____            #","green"))
    print(colored("# |_   _|| |_  ___   |  |  ||_| _| | _| | ___  ___   |     | ___  ___  #","green"))
    print(colored("#   | |  |   || -_|  |     || || . || . || -_||   |  |  |  ||   || -_| #","green"))
    print(colored("#   |_|  |_|_||___|  |__|__||_||___||___||___||_|_|  |_____||_|_||___| #","green"))
    print(colored("#                                                                      #","green")) 
    print(colored("########################################################################","green"))
    print(colored("# Date: %s                                         Time: %s #"%(day,times),"green"))
    print(colored("#                          [1] Stagnography                            #","green"))
    print(colored("#                          [2] Cryptography                            #","green"))
    print(colored("#                          [3] Exit                                    #","green"))
    print(colored("#                                                                      #","green"))
    print(colored("########################################################################","green"))
    user = input(colored("-->> ","green"))
    if user == "1":
        stagno_linux()
    elif user == "2":
        crypto_linux()
    elif user == "3":
        os.system("exit")
    else:
        print(colored("Wrong Input...","red"))
        time.sleep(2)
        banner_linux(day,times)
        
#stagnography menu
def stagno_linux():
    os.system("clear")
    print(colored("What Would You Like To Do ?","green"))
    print(colored("[1] Hide","green"))
    print(colored("[2] Reveal","green"))
    print(colored("[3] Back","green"))
    user = input(colored("-->> ","green"))
    if user == "1":
        hide_linux()
    elif user == "2":
        reveal_linux()
    elif user == "3":
        banner_linux(day,times)
    else:
        print(colored("Wrong Input...","red"))
        time.sleep(2)
        stagno_linux()
        
    

#cryptography menu
def crypto_linux():
    os.system("clear")
    print(colored("What Would You Like To Do ?","green"))
    print(colored("[1] Encrypt","green"))
    print(colored("[2] Decrypt","green"))
    print(colored("[3] Back","green"))
    user = input(colored("-->> ","green"))
    if user == "1":
        encrypt_linux()
    elif user == "2":
        decrypt_linux()
    elif user == "3":
        banner_linux(day,times)
    else:
        print(colored("Wrong Input...","red"))
        time.sleep(2)
        crypto_linux()
    
#call the function to determine os
check_os()
