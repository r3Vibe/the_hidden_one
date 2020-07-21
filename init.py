#all imports
import os
import platform
from termcolor import colored
from datetime import date ,datetime
import time
from stegano import lsbset
from stegano.lsbset import generators
from stegano import exifHeader
from pynput.keyboard import Listener
from pynput import keyboard
import sys
import re


#help menu
def help_menu():
    print("help")


#pass argument from command line and save it
uinp = sys.argv[1:]

#check arguments
def check_args(uinp):
    #find os
    myoss = platform.platform()
    myoss = myoss.lower()
    
    if uinp == []:
        print("error")
    elif uinp[0] == "-i" or uinp[0] == "--interactive":
        check_os("interactive")
    elif uinp[0] == "-hf":
        whole = " "
        whole = whole.join(uinp)
        whole_text =re.split('-hf | -p | -o',whole)
        #file to hide
        try:
            file = whole_text[1]
            file = file.replace('"','')
            file = file.strip()
            #image
            try:
                image = whole_text[2]
                #get image extinsion
                img = image.replace('"','')
                img = img.strip()
                img_name_arr = img.split("/")
                img_name = img_name_arr[len(img_name_arr)-1]
                img_ext_arr = img_name.split(".")
                ext = img_ext_arr[len(img_ext_arr)-1]
                #save name
                try:
                    saveas = whole_text[3]
                    saveas = saveas.strip()
                except Exception as e:
                    saveas = "Hidden"
                #call function based on os
                if "windows" in myoss:
                    pass
                elif "linux" in myoss:
                    hiding_linux(file,image,ext,saveas,'c')
            except:
                help_menu()
        except:
            help_menu()
   
#check the current os 
def check_os(mode):
    global day
    global times
    today = date.today()
    now = datetime.now()
    times = now.strftime("%H:%M")
    day = today.strftime("%d/%m/%Y")
    myos = platform.platform()
    if mode == "interactive":
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
    user = input(colored("-->> ","green")).strip()
    if 'm' in user:
        user = user.replace('m','')
        user = user.strip()
    if user == "1":
        stagno_linux()
    elif user == "2":
        crypto_linux()
    elif user == "3":
        os.system("exit")
    else:
        print(colored("Wrong Input...","red"))
        time.sleep(1)
        banner_linux(day,times)
        
#stagnography menu
def stagno_linux():
    os.system("clear")
    print(colored("Stagnography","green"))
    print(colored("############","green"))
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
        time.sleep(1)
        stagno_linux()

#code to hide 
def hide_linux():
    os.system("clear")
    print(colored("Stagnography Hide","green"))
    print(colored("#################","green"))
    print(colored("Choose One:","green"))
    print(colored("[1] File","green"))
    print(colored("[2] Text","green"))
    print(colored("[3] Back","green"))
    user = input(colored("-->> ","green"))
    if user == "1":
        file_hide_linux()
    elif user == "2":
        text_hide_linux()
    elif user == "3":
        stagno_linux()
    else:
        print(colored("Wrong Input...","red"))
        time.sleep(1)
        hide_linux()
        
#hide file in image
def file_hide_linux():
    os.system("clear")
    print(colored("Stagnography File Hide","green"))
    print(colored("######################","green"))
    #get the file
    the_file = input(colored("Location Of File To Hide: ","green"))
    #filter everything
    the_file = the_file.replace('"','')
    the_file = the_file.strip()
    #get the image
    the_img = input(colored("Location Of Image: ","green"))
    #filter image location
    the_img = the_img.replace('"','')
    the_img = the_img.strip()
    #get image extension
    img_ext = the_img.split(".")
    ext = img_ext[len(img_ext)-1]
    #save name
    name_to_save = input(colored("Enter Name For The Image After Process: ","green"))
    hiding_linux(the_file,the_img,ext,name_to_save,'i')

#hide the file
def hiding_linux(file,image,extension,saveas,type):
    os.system("clear")
    save_name = saveas+"."+extension
    print(colored("Processing...","green"))
    time.sleep(1)
    if extension == "jpg" or extension == "jpeg" or extension == "tiff":
        try:
            with open(file,"rb") as f:
                data = f.read()
            data = data + save_name.encode()
            exifHeader.hide(image,"./Hidden/%s"%save_name,data)
        except Exception as e:
            print(colored(e,"red"))
            time.sleep(1)
            file_hide_linux()
        finally:
            dire = os.getcwd()
            if type == 'i':
                os.system("clear")
                print(colored("Successfully Hidden File In Image","green"))
                print(colored("Location: %s/%s"%(dire+"/Hidden",save_name),"green"))
                print(colored("Press E(exit) Or M(Main Menu)","green"))
                def go_to(key):
                    if key == keyboard.KeyCode(char='e'):
                        return False
                    elif key == keyboard.KeyCode(char='m'):
                        banner_linux(day,times)
                        return False
                with Listener(on_release=go_to) as l:
                    l.join()
            elif type == 'c':
                os.system("clear")
                print(colored("Successfully Hidden File In Image","green"))
                print(colored("Location: %s/%s"%(dire+"/Hidden",save_name),"green"))
                
    elif extension == "png":
        pass
    else:
        print(colored("%s Is Not Supported By This Script Try Other Image..."%extension,"red"))
        time.sleep(1)
        file_hide_linux()

#hide text in image
def text_hide_linux():
    pass

#code to reveal
def reveal_linux():
    os.system("clear")
    print(colored("Stagnography Reveal","green"))
    print(colored("###################","green"))
    print(colored("Choose One:","green"))
    print(colored("[1] File","green"))
    print(colored("[2] Text","green"))
    print(colored("[3] Back","green"))
    user = input(colored("-->> ","green"))
    if user == "1":
        file_reveal_linux()
    elif user == "2":
        text_reveal_linux()
    elif user == "3":
        stagno_linux()
    else:
        print(colored("Wrong Input...","red"))
        time.sleep(1)
        reveal_linux()

#cryptography menu
def crypto_linux():
    os.system("clear")
    print(colored("Cryptography","green"))
    print(colored("############","green"))
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
        time.sleep(1)
        crypto_linux()

#code for encryption
def encrypt_linux():
    os.system("clear")
    print(colored("Cryptography Encryption","green"))
    print(colored("#######################","green"))
    print(colored("Choose One:","green"))
    print(colored("[1] File","green"))
    print(colored("[2] Text","green"))
    print(colored("[3] Back","green"))
    user = input(colored("-->> ","green"))
    if user == "1":
        file_encrypt_linux()
    elif user == "2":
        text_encrypt_linux()
    elif user == "3":
        crypto_linux()
    else:
        print(colored("Wrong Input...","red"))
        time.sleep(1)
        encrypt_linux()

#code for decryption
def decrypt_linux():
    os.system("clear")
    print(colored("Cryptography Decryption","green"))
    print(colored("#######################","green"))
    print(colored("Choose One:","green"))
    print(colored("[1] File","green"))
    print(colored("[2] Text","green"))
    print(colored("[3] Back","green"))
    user = input(colored("-->> ","green"))
    if user == "1":
        file_decrypt_linux()
    elif user == "2":
        text_decrypt_linux()
    elif user == "3":
        crypto_linux()
    else:
        print(colored("Wrong Input...","red"))
        time.sleep(1)
        decrypt_linux()


#call the function to determine os
check_args(uinp)
