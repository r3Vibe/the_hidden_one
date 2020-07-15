#import necessary librarys
import sys
from termcolor import colored
import os
import platform
import time
from stegano import lsbset
from stegano.lsbset import generators
from stegano import exifHeader

#pass argument from command line and save it
uinp = sys.argv[1:]


#check for given arguments by user
def check_args(uinp,theos):
    #if no arguments passed the help menu will show
    if uinp == []:
        print(colored("type menu -h or --help to show help menu","green"))
    #if -h or --help is passed the help menu will show
    elif uinp[0] == "-h" or uinp[0] == "--help":
        print(colored("this is a help menu to help new users","green"))
    #if -i or --interactive is passed then interactive mode will run
    elif uinp[0] == "-i" or uinp[0] == "--interactive":
        banner(theos)
    #if wrong arguments are passed help menu will show
    else:
        print(colored("thi is a help menu","green"))


#check the user operating system
def check_os():
    myos = platform.platform()
    #for windows
    if "windows" in myos.lower():
        os.system("cls")
        cos = "windows"
        check_args(uinp,cos)
    #for linux
    elif "linux" in myos.lower():
        os.system("clear")
        cos = "linux"
        check_args(uinp,cos)
    #for unsupported os
    else:
        print("Only Linux And Windows Support")
        os.system("exit")
  
  
  
#interactive banner for the script
def banner(currentos):
    #clear screen depending on operating system
    if currentos ==  "windows":
        os.system("cls")
    elif currentos == "linux":
        os.system("clear")
    #ascii menu
    print(colored("##############################################################################","green"))
    print(colored("#  _______ _            _    _ _     _     _               ____              #","green") )
    print(colored("# |__   __| |          | |  | (_)   | |   | |             / __ \             #","green") )
    print(colored("#    | |  | |__   ___  | |__| |_  __| | __| | ___ _ __   | |  | |_ __   ___  #","green") )
    print(colored("#    | |  | '_ \ / _ \ |  __  | |/ _` |/ _` |/ _ \ '_ \  | |  | | '_ \ / _ \\ #","green") )
    print(colored("#    | |  | | | |  __/ | |  | | | (_| | (_| |  __/ | | | | |__| | | | |  __/ #","green") )
    print(colored("#    |_|  |_| |_|\___| |_|  |_|_|\__,_|\__,_|\___|_| |_|  \____/|_| |_|\___| #","green") )
    print(colored("#                                                                            #","green"))
    print(colored("##############################################################################","green"))
    print(colored("#                                                                            #","green"))
    print(colored("#             [1] Hide File                                                  #","green"))
    print(colored("#             [2] Hide Message                                               #","green"))
    print(colored("#             [3] Encrypt Message                                            #","green"))
    print(colored("#             [4] Reveal File                                                #","green"))
    print(colored("#             [5] Reveal Message                                             #","green"))
    print(colored("#             [6] Decrypt Message                                            #","green"))
    print(colored("#             [7] Encrypt And Hide                                           #","green"))
    print(colored("#             [8] Reveal And Decrypt                                         #","green"))
    print(colored("#             [9] Exit                                                       #","green"))
    print(colored("#                                                                            #","green"))
    print(colored("##############################################################################","green"))
    user = input(colored("-->> ","green"))
    #call hide file function that hides a file in images
    if(user == "1"):
        pass
    #call hide message function that will hide message in a image
    elif(user == "2"):
        hide_message(currentos)
    #call function to encrypt message
    elif(user == "3"):
        pass
    #call function to reveal hidden file
    elif(user == "4"):
        pass
    #call a function to reveal message
    elif(user == "5"):
        reveal_message(currentos)    
    #call a function to decrypt message
    elif(user == "6"):
        pass                           
    #call a function to encrypt and hide message in image                    
    elif(user == "7"):
        pass
    #call a function to reveal and decrypt message
    elif(user == "8"):
        pass
    #clear screen and exit shell
    elif(user == "9"):
        if currentos ==  "windows":
            os.system("cls")
            os.system("exit")
        elif currentos == "linux":
            os.system("clear")
            os.system("exit")
    #restart the menu after 2 second if wrong input
    else:
        print(colored("Wrong Input.Try Again In 2s...","red"))
        time.sleep(2)
        banner(currentos)
        
#function to reveal mesages
def reveal_message(currentos):
    if currentos == "windows":    
        os.system("cls")
        #get image file with hidden message
        location = input(colored('Location Of Image With Hidden Message -->> ',"green"))
        #get image name and extinsion
        location = location.replace('"','')
        img_name_arr = location.split("\\")
        img_name = img_name_arr[len(img_name_arr)-1]
        img_ext_arr = img_name.split(".")
        img_ext = img_ext_arr[len(img_ext_arr)-1]
        #reveal message from jpg or jpeg file
        if img_ext == "jpg" or img_ext == "jpeg":
            #try to reveal hidden message
            try:
                message = exifHeader.reveal(location)
                print(colored("Hidden Message Is: "+message.decode(),"green"))
                todo = input(colored("Type E to exit Or M to Go to Main Menu -->> ","green"))
                if todo.lower() == "e":
                    os.system("cls")
                    os.system("exit")
                elif todo.lower() == "m":
                    banner(currentos)
                else:
                    print(colored("Wrong Input.Quitting...","red"))
            #exit if error happnes
            except Exception as e:
                print(colored("We have an error.Quitting...","red"))
                os.system("cls")
                os.system("exit")
        #reveal message from png files
        elif img_ext == "png":
            try:
                message = lsbset.reveal(location, generators.eratosthenes())
                print(colored("Hidden Message Is: "+message,"green"))
                todo = input(colored("Type E to exit Or M to Go to Main Menu -->> ","green"))
                if todo.lower() == "e":
                    os.system("cls")
                    os.system("exit")
                elif todo.lower() == "m":
                    banner()
                else:
                    print(colored("Wrong Input.Quitting...","red"))
            except Exception as e:
                print(colored("We have an error.Quitting...","red"))
                os.system("cls")
                os.system("exit")
                
    elif currentos == "linux":
        os.system("clear")
        #png image location with message
        location = input(colored('Location Of Image With Hidden Message -->> ',"green"))
        #get image name and extinsion
        location = location.replace('"','')
        img_name_arr = location.split("/")
        img_name = img_name_arr[len(img_name_arr)-1]
        img_ext_arr = img_name.split(".")
        img_ext = img_ext_arr[len(img_ext_arr)-1]
        #show if jpg image
        if img_ext == "jpg" or img_ext == "jpeg":
            try:
                message = exifHeader.reveal(location)
                print(colored("Hidden Message Is: "+message.decode(),"green"))
                todo = input(colored("Type E to exit Or M to Go to Main Menu -->> ","green"))
                if todo.lower() == "e":
                    os.system("clear")
                    os.system("exit")
                elif todo.lower() == "m":
                    banner()
                else:
                    print(colored("Wrong Input.Quitting...","red"))
            except Exception as e:
                print(colored("We have an error.Quitting...","red"))
                os.system("clear")
                os.system("exit")
        #show if png image 
        elif img_ext == "png":
            try:
                message = lsbset.reveal(location, generators.eratosthenes())
                print(colored("Hidden Message Is: "+message,"green"))
                todo = input(colored("Type E to exit Or M to Go to Main Menu -->> ","green"))
                if todo.lower() == "e":
                    os.system("clear")
                    os.system("exit")
                elif todo.lower() == "m":
                    banner()
                else:
                    print(colored("Wrong Input.Quitting...","red"))
            except Exception as e:
                print(colored("We have an error.Quitting...","red"))
                os.system("clear")
                os.system("exit")
        
#function to hide message
def hide_message(currentos):
    #hide message for windows os
    if currentos == "windows":
        os.system("cls")
        #get user message
        msg = input(colored("Type Your Message -->> ","green"))
        os.system("cls")
        #get image file to hide message
        img = input(colored("Image File To Hide Message -->> ","green"))
        os.system("cls")
        #get the image file name and extension
        img = img.replace('"','')
        img_name_arr = img.split("\\")
        img_name = img_name_arr[len(img_name_arr)-1]
        img_ext_arr = img_name.split(".")
        img_ext = img_ext_arr[len(img_ext_arr)-1]
        #method if image file is jpg or jpeg
        if img_ext == "jpg" or img_ext == "jpeg":
            print(colored("Message: "+msg,"green"))
            print(colored("Image: "+img_name,"green"))
            confirm = input(colored("Type Y to confirm X to retry -->> ","green"))
            if(confirm.lower() == "y"):
                #try to hide message to file
                try:
                    exifHeader.hide(img,"./hidden.jpg", msg)
                    os.system("cls")
                    print(colored("Message Hidden In Image","green"))
                    todo = input(colored("Type E(exit) M(main menu) -->> ","green"))
                    if todo.lower() == "e":
                        os.system("exit")
                    elif todo.lower() == "m":
                        banner(currentos)
                    else:
                        print(colored("Wrong Input.Quitting...","red"))
                        os.system("cls")
                        os.system("exit")
                except Exception as e:
                    print(colored("We have A Problem. Try Later...","red"))
                    os.system("exit")
            elif confirm.lower() == "x":
               hide_message(currentos)
        #method if image file is png
        elif img_ext == "png":
            print(colored("Message: "+msg,"green"))
            print(colored("Image: "+img_name,"green"))
            confirm = input(colored("Type Y to confirm X to retry -->> ","green"))
            if(confirm.lower() == "y"):
                #try to hide msg to file
                try:
                    hide = lsbset.hide(img,msg,generators.eratosthenes())
                    hide.save("./hidden.png")
                    os.system("cls")
                    print(colored("Message Hidden In Image","green"))
                    todo = input(colored("Type E to exit M to go to main menu -->> ","green"))
                    if todo.lower() == "e":
                        os.system("exit")
                    elif todo.lower() == "m":
                        banner(currentos)
                    else:
                        print(colored("Wrong Input.Quitting...","red"))
                        os.system("exit")
                except Exception as e:
                    print(colored("We have A Problem. Try Later...","red"))
                    os.system("exit")
            elif confirm.lower() == "x":
               hide_message(currentos)
        #if image file is not supported
        else:
            print(colored("We Recommend using jpg,png Format Images","red"))
            os.system("exit")
    
    elif currentos == "linux":
        os.system("clear")
        #get user message
        msg = input(colored("Type Your Message -->> ","green"))
        os.system("clear")
        #get image file to hide message
        img = input(colored("Image File To Hide Message -->> ","green"))
        os.system("clear")
        #get the image file name and extension
        img = img.replace('"','')
        img_name_arr = img.split("/")
        img_name = img_name_arr[len(img_name_arr)-1]
        img_ext_arr = img_name.split(".")
        img_ext = img_ext_arr[len(img_ext_arr)-1]
        #method if image file is jpg or jpeg
        if img_ext == "jpg" or img_ext == "jpeg":
            print(colored("Message: "+msg,"green"))
            print(colored("Image: "+img_name,"green"))
            confirm = input(colored("Type Y to confirm X to retry -->> ","green"))
            if(confirm.lower() == "y"):
                #try to hide message to file
                try:
                    exifHeader.hide(img,"./hidden.jpg", msg)
                    os.system("clear")
                    print(colored("Message Hidden In Image","green"))
                    todo = input(colored("Type E(exit) M(main menu) -->> ","green"))
                    if todo.lower() == "e":
                        os.system("exit")
                    elif todo.lower() == "m":
                        banner(currentos)
                    else:
                        print(colored("Wrong Input.Quitting...","red"))
                        os.system("clear")
                        os.system("exit")
                except Exception as e:
                    print(colored("We have A Problem. Try Later...","red"))
                    os.system("exit")
            elif confirm.lower() == "x":
               hide_message(currentos)
        #method if image file is png
        elif img_ext == "png":
            print(colored("Message: "+msg,"green"))
            print(colored("Image: "+img_name,"green"))
            confirm = input(colored("Type Y to confirm X to retry -->> ","green"))
            if(confirm.lower() == "y"):
                #try to hide msg to file
                try:
                    hide = lsbset.hide(img,msg,generators.eratosthenes())
                    hide.save("./hidden.png")
                    os.system("clear")
                    print(colored("Message Hidden In Image","green"))
                    todo = input(colored("Type E to exit M to go to main menu -->> ","green"))
                    if todo.lower() == "e":
                        os.system("exit")
                    elif todo.lower() == "m":
                        banner(currentos)
                    else:
                        print(colored("Wrong Input.Quitting...","red"))
                        os.system("exit")
                except Exception as e:
                    print(colored("We have A Problem. Try Later...","red"))
                    os.system("exit")
            elif confirm.lower() == "x":
               hide_message(currentos)
        #if image file is not supported
        else:
            print(colored("We Recommend using jpg,png Format Images","red"))
            os.system("exit")
       
#call the function to start the script
check_os()