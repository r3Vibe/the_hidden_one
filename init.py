from stegano import lsbset
from stegano.lsbset import generators
from stegano import exifHeader
from termcolor import colored
import os
import platform


def banner():
    os.system("cls");
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
    if(user == "1"):
        pass
    elif(user == "2"):
        hidemsg()
    elif(user == "3"):
        pass
    elif(user == "4"):
        pass
    elif(user == "5"):
        os_name = platform.platform()
        revealmsg(os_name)       
    elif(user == "6"):
        pass                                               
    elif(user == "7"):
        pass
    elif(user == "8"):
        pass
    elif(user == "9"):
        os.system("exit")


# this function hides massages to image
def hidemsg():
    # check operating system
    os_name = platform.platform()
    #for windows
    if "windows" in os_name.lower():
        os.system("cls")
        msg = input(colored("Type Your Message -->> ","green"))
        os.system("cls")
        img = input(colored("Image File To Hide Message -->> ","green"))
        img = img.replace('"','')
        img_name_arr = img.split("\\")
        img_name = img_name_arr[len(img_name_arr)-1]
        img_ext_arr = img_name.split(".")
        img_ext = img_ext_arr[len(img_ext_arr)-1]
        #os.system("cls")
        if img_ext == "jpg" or img_ext == "jpeg":
            print(colored("Message: "+msg,"green"))
            print(colored("Image: "+img_name,"green"))
            confirm = input(colored("Type Y to confirm X to retry -->> ","green"))
            if(confirm.lower() == "y"):
                try:
                    exifHeader.hide(img,"./hidden.jpg", msg)
                    os.system("cls")
                    print(colored("Message Hidden In Image","green"))
                    todo = input(colored("Type E to exit M to go to main menu -->> ","green"))
                    if todo.lower() == "e":
                        os.system("exit")
                    elif todo.lower() == "m":
                        banner()
                    else:
                        print(colored("Wrong Input.Quitting...","red"))
                        os.system("exit")
                except:
                    print(colored("We have A Problem. Try Later...","red"))
                    os.system("exit")
            elif confirm.lower() == "x":
               hidemsg()
        elif img_ext == "png":
            print(colored("Message: "+msg,"green"))
            print(colored("Image: "+img_name,"green"))
            confirm = input(colored("Type Y to confirm X to retry -->> ","green"))
            if(confirm.lower() == "y"):
                try:
                    hide = lsbset.hide(img,msg,generators.eratosthenes())
                    hide.save("./hidden.png")
                    os.system("cls")
                    print(colored("Message Hidden In Image","green"))
                    todo = input(colored("Type E to exit M to go to main menu -->> ","green"))
                    if todo.lower() == "e":
                        os.system("exit")
                    elif todo.lower() == "m":
                        banner()
                    else:
                        print(colored("Wrong Input.Quitting...","red"))
                        os.system("exit")
                except:
                    print(colored("We have A Problem. Try Later...","red"))
                    os.system("exit")
            elif confirm.lower() == "x":
               hidemsg()
        else:
            print(colored("We Recommend using jpg,png Format Images","red"))
            os.system("exit")
            
    #for linux
    elif "linux" in os_name.lower():
        os.system("clear")
        msg = input(colored("Type Your Message -->> ","green"))
        os.system("clear")
        img = input(colored("Image File To Hide Message -->> ","green"))
        img = img.replace('"','')
        img_name_arr = img.split("/")
        img_name = img_name_arr[len(img_name_arr)-1]
        img_ext_arr = img_name.split(".")
        img_ext = img_ext_arr[len(img_ext_arr)-1]
        os.system("clear")
        if(img_ext == "jpg" or img_ext == "jpeg"):
            print(colored("Message: "+msg,"green"))
            print(colored("Image: "+img_name,"green"))
            confirm = input(colored("Type Y to confirm X to retry -->> ","green"))
            if(confirm.lower() == "y"):
                try:
                    exifHeader.hide(img,"./hidden.jpg", msg)
                    os.system("clear")
                    print(colored("Message Hidden In Image","green"))
                    todo = input(colored("Type E to exit M to go to main menu -->> ","green"))
                    if todo.lower() == "e":
                        os.system("exit")
                    elif todo.lower() == "m":
                        banner()
                    else:
                        print(colored("Wrong Input.Quitting...","red"))
                        os.system("exit")
                except:
                    print(colored("We have A Problem. Try Later...","red"))
                    os.system("exit")
            elif confirm.lower() == "x":
               hidemsg()
        elif(img_ext == "png"):
            print(colored("Message: "+msg,"green"))
            print(colored("Image: "+img_name,"green"))
            confirm = input(colored("Type Y to confirm X to retry -->> ","green"))
            if(confirm.lower() == "y"):
                try:
                    hide = lsbset.hide(img,msg,generators.eratosthenes())
                    hide.save("./hidden.png")
                    os.system("clear")
                    print(colored("Message Hidden In Image","green"))
                    todo = input(colored("Type E to exit M to go to main menu -->> ","green"))
                    if todo.lower() == "e":
                        os.system("exit")
                    elif todo.lower() == "m":
                        banner()
                    else:
                        print(colored("Wrong Input.Quitting...","red"))
                        os.system("exit")
                except:
                    print(colored("We have A Problem. Try Later...","red"))
                    os.system("exit")
            elif confirm.lower() == "x":
               hidemsg()
        else:
            print(colored("We Recommend using jpg,png Format Images","red"))
            os.system("exit")
            





def revealmsg(os_name):
    if "windows" in os_name.lower():    
        os.system("cls")
        location = input(colored('Location Of Image With Hidden Message -->> ',"green"))
        location = location.replace('"','')
        img_name_arr = location.split("\\")
        img_name = img_name_arr[len(img_name_arr)-1]
        img_ext_arr = img_name.split(".")
        img_ext = img_ext_arr[len(img_ext_arr)-1]
        if img_ext == "jpg" or img_ext == "jpeg":
            try:
                message = exifHeader.reveal(location)
                print(colored("Hidden Message Is: "+message.decode(),"green"))
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
                print(e)
                #print(colored("We have an error.Quitting...","red"))
                #os.system("cls")
                os.system("exit")
                
    elif "linux" in os_name.lower():
        os.system("clear")
        location = input(colored('Location Of Image With Hidden Message -->> ',"green"))
        location = location.replace('"','')
        img_name_arr = location.split("/")
        img_name = img_name_arr[len(img_name_arr)-1]
        img_ext_arr = img_name.split(".")
        img_ext = img_ext_arr[len(img_ext_arr)-1]
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



















banner()


























# msg = "Test Msg"

# location = "./test.jpg"

# hide = lsbset.hide(location,msg,generators.fibonacci())

# hide.save("./test2.jpg")

# message = lsbset.reveal("./test2.jpg", generators.fibonacci())

# print(message)
# image = input("file ")
# save = image.split("\\")
# extension = save[len(save)-1].split(".")
# print(extension[len(extension)-1])


# secret = exifHeader.hide("./test.jpg","./image.jpg", secret_message="Total Fuck")
# msg = exifHeader.reveal("./image.jpg")

# print(msg)