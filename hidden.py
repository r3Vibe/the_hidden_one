#import necessary librarys
import sys
from termcolor import colored
import os
import platform
import time
from stegano import lsbset
from stegano.lsbset import generators
from stegano import exifHeader
import re
import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet

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
    #reveal message from console -rm image path
    elif uinp[0] == "-rm":
        whole = " "
        whole = whole.join(uinp)
        whole_text = re.split("-rm",whole)
        image_path = whole_text[1]
        image_path = image_path.strip()
        reveal_message_console(theos,image_path)
    #hide message from console -hm message -p image path
    elif uinp[0] == "-hm":
        whole = " "
        whole = whole.join(uinp)
        whole_text =re.split('-hm | -p',whole)
        message_tohide = whole_text[1]
        image_path = whole_text[2]
        hide_message_console(theos,message_tohide,image_path)
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
    print(colored("#             [3] Encryption                                                 #","green"))
    print(colored("#             [4] Reveal File                                                #","green"))
    print(colored("#             [5] Reveal Message                                             #","green"))
    print(colored("#             [6] Decryption                                                 #","green"))
    print(colored("#             [7] Encrypt And Hide                                           #","green"))
    print(colored("#             [8] Reveal And Decrypt                                         #","green"))
    print(colored("#             [9] Exit                                                       #","green"))
    print(colored("#                                                                            #","green"))
    print(colored("##############################################################################","green"))
    user = input(colored("-->> ","green"))
    #call hide file function that hides a file in images
    if(user == "1"):
        hide_file(currentos)
    #call hide message function that will hide message in a image
    elif(user == "2"):
        hide_message(currentos)
    #call function to encrypt message
    elif(user == "3"):
        encrypt(currentos)
    #call function to reveal hidden file
    elif(user == "4"):
        reveal_file(currentos)
    #call a function to reveal message
    elif(user == "5"):
        reveal_message(currentos)    
    #call a function to decrypt message
    elif(user == "6"):
        decrypt(currentos)                         
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
                message = message.decode()
                save_msg = open("./Messages/"+img_ext_arr[0]+".txt","w")
                save_msg.write(message)
                save_msg.close()
                print(colored("Hidden Message Is: "+message,"green"))
                print(colored("Message saved in messages/"+img_ext_arr[0]+".txt file","green"))
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
                print(e)
                #print(colored("We have an error.Quitting...","red"))
                #os.system("cls")
                #os.system("exit")
        #reveal message from png files
        elif img_ext == "png":
            try:
                message = lsbset.reveal(location, generators.eratosthenes())
                save_msg = open("./Messages/hidden_message.txt","w")
                save_msg.write(message)
                save_msg.close()
                print(colored("Hidden Message Is: "+message,"green"))
                print(colored("Message saved in messages/"+img_ext_arr[0]+".txt file","green"))
                todo = input(colored("Type E to exit Or M to Go to Main Menu -->> ","green"))
                if todo.lower() == "e":
                    os.system("cls")
                    os.system("exit")
                elif todo.lower() == "m":
                    banner(currentos)
                else:
                    print(colored("Wrong Input.Quitting...","red"))
            except Exception as e:
                print(e)
                #print(colored("We have an error.Quitting...","red"))
                #os.system("cls")
                #os.system("exit")
                
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
                message = message.decode()
                save_msg = open("./Messages/"+img_ext_arr[0]+".txt","w")
                save_msg.write(message)
                save_msg.close()
                print(colored("Hidden Message Is: "+message,"green"))
                print(colored("Message saved in messages/hidden_message.txt file","green"))
                todo = input(colored("Type E to exit Or M to Go to Main Menu -->> ","green"))
                if todo.lower() == "e":
                    os.system("clear")
                    os.system("exit")
                elif todo.lower() == "m":
                    banner(currentos)
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
                message = message.decode()
                save_msg = open("./Messages/"+img_ext_arr[0]+".txt","w","utf-8")
                save_msg.write(message)
                save_msg.close()
                print(colored("Hidden Message Is: "+message,"green"))
                print(colored("Message saved in messages/hidden_message.txt file","green"))
                todo = input(colored("Type E to exit Or M to Go to Main Menu -->> ","green"))
                if todo.lower() == "e":
                    os.system("clear")
                    os.system("exit")
                elif todo.lower() == "m":
                    banner(currentos)
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
                    exifHeader.hide(img,"./Images/"+img_ext_arr[0]+".jpg", msg)
                    os.system("cls")
                    print(colored("Message Hidden In Image","green"))
                    print(colored("Image Available Under Images Folder","green"))
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
                    hide.save("./Images/"+img_ext_arr[0]+".png")
                    os.system("cls")
                    print(colored("Message Hidden In Image","green"))
                    print(colored("Image Available Under Images Folder","green"))
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
                    exifHeader.hide(img,"./Images/"+img_ext_arr[0]+".jpg", msg)
                    os.system("clear")
                    print(colored("Message Hidden In Image","green"))
                    print(colored("Image Available Under Images Folder","green"))
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
                    hide.save("./Images/"+img_ext_arr[0]+".png")
                    os.system("clear")
                    print(colored("Message Hidden In Image","green"))
                    print(colored("Image Available Under Images Folder","green"))
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
       
#function to hide message from console window
def hide_message_console(currentos,msg,image):
 #hide message for windows os
    if currentos == "windows":
        os.system("cls")
        #get the image file name and extension
        img = image.replace('"','')
        img = img.strip()
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
                    exifHeader.hide(img,"./Images/"+img_ext_arr[0]+".jpg", msg)
                    os.system("cls")
                    print(colored("Message Hidden In Image","green"))
                    print(colored("Image Available Under Images Folder","green"))
                    os.system("exit")
                except Exception as e:
                    print(colored("We have A Problem. Try Later...","red"))
                    os.system("exit")
            elif confirm.lower() == "x":
               os.system("cls")
               os.system("exit")
        #method if image file is png
        elif img_ext == "png":
            print(colored("Message: "+msg,"green"))
            print(colored("Image: "+img_name,"green"))
            confirm = input(colored("Type Y to confirm X to retry -->> ","green"))
            if(confirm.lower() == "y"):
                #try to hide msg to file
                try:
                    hide = lsbset.hide(img,msg,generators.eratosthenes())
                    hide.save("./Images/"+img_ext_arr[0]+".png")
                    os.system("cls")
                    print(colored("Message Hidden In Image","green"))
                    print(colored("Image Available Under Images Folder","green"))
                    os.system("exit")
                except Exception as e:
                    print(e)
                    print(colored("We have A Problem. Try Later...","red"))
                    os.system("exit")
            elif confirm.lower() == "x":
               os.system("cls")
               os.system("exit")
        #if image file is not supported
        else:
            print(colored("We Recommend using jpg,png Format Images","red"))
            os.system("exit")
    
    elif currentos == "linux":
        os.system("clear")
        #get the image file name and extension
        img = image.replace('"','')
        img = img.strip()
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
                    exifHeader.hide(img,"./Images/"+img_ext_arr[0]+".jpg", msg)
                    os.system("clear")
                    print(colored("Message Hidden In Image","green"))
                    print(colored("Image Available Under Images Folder","green"))
                    os.system("exit")
                except Exception as e:
                    print(e)
                    #print(colored("We have A Problem. Try Later...","red"))
                    #os.system("exit")
            elif confirm.lower() == "x":
               os.system("clear")
               os.system("exit")
        #method if image file is png
        elif img_ext == "png":
            print(colored("Message: "+msg,"green"))
            print(colored("Image: "+img_name,"green"))
            confirm = input(colored("Type Y to confirm X to retry -->> ","green"))
            if(confirm.lower() == "y"):
                #try to hide msg to file
                try:
                    hide = lsbset.hide(img,msg,generators.eratosthenes())
                    hide.save("./Images/"+img_ext_arr[0]+".png")
                    os.system("clear")
                    print(colored("Message Hidden In Image","green"))
                    print(colored("Image Available Under Images Folder","green"))
                    os.system("exit")
                except Exception as e:
                    print(colored("We have A Problem. Try Later...","red"))
                    os.system("exit")
            elif confirm.lower() == "x":
               os.system("clear")
               os.system("exit")
        #if image file is not supported
        else:
            print(colored("We Recommend using jpg,png Format Images","red"))
            os.system("exit")
       
#function to reveal message from console window
def reveal_message_console(currentos,path):
    if currentos == "windows":    
        os.system("cls")
        location = path.replace('"','')
        img_name_arr = location.split("\\")
        img_name = img_name_arr[len(img_name_arr)-1]
        img_ext_arr = img_name.split(".")
        img_ext = img_ext_arr[len(img_ext_arr)-1]
        #reveal message from jpg or jpeg file
        if img_ext == "jpg" or img_ext == "jpeg":
            #try to reveal hidden message
            try:
                message = exifHeader.reveal(location)
                message = message.decode()
                save_msg = open("./Messages/"+img_ext_arr[0]+".txt","w")
                save_msg.write(message)
                save_msg.close()
                print(colored("Hidden Message Is: "+message,"green"))
                print(colored("Message saved in messages/"+img_ext_arr[0]+".txt file","green"))
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
                print(e)
                #print(colored("We have an error.Quitting...","red"))
                #os.system("cls")
                #os.system("exit")
        #reveal message from png files
        elif img_ext == "png":
            try:
                message = lsbset.reveal(location, generators.eratosthenes())
                save_msg = open("./Messages/"+img_ext_arr[0]+".txt","w")
                save_msg.write(message)
                save_msg.close()
                print(colored("Hidden Message Is: "+message,"green"))
                print(colored("Message saved in messages/"+img_ext_arr[0]+".txt file","green"))
                todo = input(colored("Type E to exit Or M to Go to Main Menu -->> ","green"))
                if todo.lower() == "e":
                    os.system("cls")
                    os.system("exit")
                elif todo.lower() == "m":
                    banner(currentos)
                else:
                    print(colored("Wrong Input.Quitting...","red"))
            except Exception as e:
                print(e)
                #print(colored("We have an error.Quitting...","red"))
                #os.system("cls")
                #os.system("exit")
                
    elif currentos == "linux":
        os.system("clear")
        location = path.replace('"','')
        img_name_arr = location.split("/")
        img_name = img_name_arr[len(img_name_arr)-1]
        img_ext_arr = img_name.split(".")
        img_ext = img_ext_arr[len(img_ext_arr)-1]
        #show if jpg image
        if img_ext == "jpg" or img_ext == "jpeg":
            try:
                message = exifHeader.reveal(location)
                message = message.decode()
                save_msg = open("./Messages/"+img_ext_arr[0]+".txt","w")
                save_msg.write(message)
                save_msg.close()
                print(colored("Hidden Message Is: "+message,"green"))
                print(colored("Message saved in messages/"+img_ext_arr[0]+".txt file","green"))
                todo = input(colored("Type E to exit Or M to Go to Main Menu -->> ","green"))
                if todo.lower() == "e":
                    os.system("clear")
                    os.system("exit")
                elif todo.lower() == "m":
                    banner(currentos)
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
                message = message.decode()
                save_msg = open("./Messages/"+img_ext_arr[0]+".txt","w","utf-8")
                save_msg.write(message)
                save_msg.close()
                print(colored("Hidden Message Is: "+message,"green"))
                print(colored("Message saved in messages/"+img_ext_arr[0]+".txt file","green"))
                todo = input(colored("Type E to exit Or M to Go to Main Menu -->> ","green"))
                if todo.lower() == "e":
                    os.system("clear")
                    os.system("exit")
                elif todo.lower() == "m":
                    banner(currentos)
                else:
                    print(colored("Wrong Input.Quitting...","red"))
            except Exception as e:
                print(colored("We have an error.Quitting...","red"))
                os.system("clear")
                os.system("exit")

#shows encryption menu
def encrypt(currentos):
    if currentos == "windows":
        os.system("cls")
        print(colored("[1] File Encypt","green"))
        print(colored("[2] Message Encypt","green"))
        user_choice = input(colored("Choose One -->> ","green"))
        if user_choice == "1":
            file_encrypt(currentos)
        elif user_choice == "2":
            message_encrypt(currentos)    
        else:
            print(colored("Wrong Input.Try Again In 2s...","red"))
            time.sleep(2)
            os.system("cls")
            encrypt(currentos)
    elif currentos == "linux":
        os.system("clear")
        print(colored("[1] File Encypt","green"))
        print(colored("[2] Message Encypt","green"))
        user_choice = input(colored("Choose One -->> ","green"))
        if user_choice == "1":
            file_encrypt(currentos)
        elif user_choice == "2":
            message_encrypt(currentos)
        else:
            print(colored("Wrong Input.Try Again In 2s...","red"))
            time.sleep(2)
            os.system("clear")
            encrypt(currentos)

#encrypt any file
def file_encrypt(currentos):
    #code for windows
    if currentos == "windows":
        os.system("cls")
        #file to encrypt
        file = input(colored("File Location -->> ","green"))
        #password for encryption
        passw = input(colored("Password -->> ","green"))
        #encode password
        passw = passw.encode()
        #remove white space
        file = file.replace('"','')
        file = file.strip()
        #get file name
        file_location_arr = file.split("/")
        file_name_ext = file_location_arr[len(file_location_arr)-1]
        file_name_arr = file_name_ext.split(".")
        file_name = file_name_arr[0]
        file_ext = file_name_arr[1]        
        #read file
        with open(file,'rb') as file2:
            file3 = file2.read()
            
        #get the key generated from password
        key = gen_key(passw)
        
        #make cipher from key
        cipher = Fernet(key)
        
        #encrypt file
        encrypt_file = cipher.encrypt(file3)
        
        #save encrypted
        with open("./Encrypted/"+file_name+"."+file_ext+"_encrypted","wb") as ef:
            ef.write(encrypt_file)    
        
        print(colored("Encrypted File Can be found under Encrypted Folder","green"))
        
        #main menu or exit
        whreto = input(colored("Type E(exit) M(Main menu)","green"))
        if whreto.lower() == "e":
            os.system("exit")
        elif whreto.lower() == "m":
            banner(currentos)
        else:
            print(colored("Wrong Input...","red"))
            os.system("exit")
    #code for linux
    elif currentos == "linux":
        os.system("clear")
        #file to encrypt
        file = input(colored("File Location -->> ","green"))
        #password for encryption
        passw = input(colored("Password -->> ","green"))
        #encode password
        passw = passw.encode()
        #remove white space
        file = file.replace('"','')
        file = file.strip()
        #get file name
        file_location_arr = file.split("/")
        file_name_ext = file_location_arr[len(file_location_arr)-1]
        file_name_arr = file_name_ext.split(".")
        file_name = file_name_arr[0]     
        file_ext = file_name_arr[1]   
        #read file
        with open(file,'rb') as file2:
            file3 = file2.read()
            
        #get the key generated from password
        key = gen_key(passw)
        
        #make cipher from key
        cipher = Fernet(key)
        
        #encrypt file
        encrypt_file = cipher.encrypt(file3)
        
        #save encrypted
        with open("./Encrypted/"+file_name+"."+file_ext+"_encrypted","wb") as ef:
            ef.write(encrypt_file)    
        
        print(colored("Encrypted File Can be found under Encrypted Folder","green"))
        
        #main menu or exit
        whreto = input(colored("Type E(exit) M(Main menu)","green"))
        if whreto.lower() == "e":
            os.system("exit")
        elif whreto.lower() == "m":
            banner(currentos)
        else:
            print(colored("Wrong Input...","red"))
            os.system("exit")    
 
#encrypt user message 
def message_encrypt(currentos):
    #code for windows
    if currentos == "windows":
        os.system("cls")
        #file to encrypt
        message = input(colored("Type Your Message -->> ","green"))
        #password for encryption
        passw = input(colored("Password -->> ","green"))
        #encode password and message
        passw = passw.encode()
        message = message.encode() 
            
        #get the key generated from password
        key = gen_key(passw)
        
        #make cipher from key
        cipher = Fernet(key)
        
        #encrypt message
        encrypt_message = cipher.encrypt(message)
        
        #save encrypted
        with open("./Encrypted/encrypted_msg","wb") as ef:
            ef.write(encrypt_message)    
        
        print(colored("Encrypted File Can be found under Encrypted Folder","green"))
        
        #main menu or exit
        whreto = input(colored("Type E(exit) M(Main menu)","green"))
        if whreto.lower() == "e":
            os.system("exit")
        elif whtrto.lower() == "m":
            banner(currentos)
        else:
            print(colored("Wrong Input...","red"))
            os.system("exit")
    #code for linux
    elif currentos == "linux":
        os.system("clear")
        #file to encrypt
        message = input(colored("Type Your Message -->> ","green"))
        #password for encryption
        passw = input(colored("Password -->> ","green"))
        #encode password and message
        passw = passw.encode()
        message = message.encode() 
            
        #get the key generated from password
        key = gen_key(passw)
        
        #make cipher from key
        cipher = Fernet(key)
        
        #encrypt message
        encrypt_message = cipher.encrypt(message)
        
        #save encrypted
        with open("./Encrypted/encrypted_msg","wb") as ef:
            ef.write(encrypt_message)    
        
        print(colored("Encrypted File Can be found under Encrypted Folder","green"))
        
        #main menu or exit
        whreto = input(colored("Type E(exit) M(Main menu)","green"))
        if whreto.lower() == "e":
            os.system("exit")
        elif whtrto.lower() == "m":
            banner(currentos)
        else:
            print(colored("Wrong Input...","red"))
            os.system("exit")
     

#generates key for encryption with a password
def gen_key(password):
    #salt to make password strong
    salt = b'\xf4\x0e\xfd^\xc3!\x1a\x1f\xf3\xb5\xd7!\xe42|q'

    kdf = PBKDF2HMAC (
        algorithm=hashes.SHA256,
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )

    #key to encrypt
    key = base64.urlsafe_b64encode(kdf.derive(password))

    return key

#show decryption menu
def decrypt(currentos):
    if currentos == "windows":
        os.system("cls")
    elif currentos == "linux":
        os.system("clear")
    
    print(colored("[1] File Decryption","green"))
    print(colored("[2] Message Decryption","green"))
    usr_choice = input(colored("Choose One -->> ","green"))
    if usr_choice == "1":
        file_decrypt(currentos)
    elif usr_choice == "2":
        message_decrypt(currentos)
    else:
        print(colored("Wrong Input...","red"))
        os.system("exit")

#file decryption
def file_decrypt(currentos):
    if currentos == "windows":
        os.system("cls")
        
        #file location
        file = input(colored("FIle Location -->> ","green"))
        
        #password to decrypt
        passw = input(colored("Password -->> ","green"))
        
        #encode password
        passw = passw.encode()
        
        #replace whiteplace
        file = file.replace('"','')
        file = file.strip()
        
        #get file name and extinsion
        file_location_arr = file.split("/")
        file_name_ext = file_location_arr[len(file_location_arr)-1]
        file_name_arr = file_name_ext.split(".")
        file_name = file_name_arr[0]     
        file_ext = file_name_arr[1]
        file_extinsion = file_ext.split("_")
        extnsn = file_extinsion[0]
        
        #read file
        with open(file,'rb') as file2:
            file3 = file2.read()
            
        #get the key generated from password
        key = gen_key(passw)
        
        #make cipher from key
        cipher = Fernet(key)
        
        #encrypt file
        decrypt_file = cipher.decrypt(file3)
        
        message = decrypt_file.decode()
        
        #save decrypted
        with open("./Decrypted/"+file_name+"."+extnsn,"w") as ef:
            ef.write(message)
        
        print(colored("Decrypted File Can be Found under Decrypted Folder "+file_name+"."+extnsn))
        
        #main menu or exit
        whreto = input(colored("Type E(exit) M(Main menu)","green"))
        if whreto.lower() == "e":
            os.system("exit")
        elif whreto.lower() == "m":
            banner(currentos)
        else:
            print(colored("Wrong Input...","red"))
            os.system("exit")   
            
    elif currentos == "linux":
        os.system("clear")
        
        #file location
        file = input(colored("FIle Location -->> ","green"))
        
        #password to decrypt
        passw = input(colored("Password -->> ","green"))
        
        #encode password
        passw = passw.encode()
        
        #replace whiteplace
        file = file.replace('"','')
        file = file.strip()
        
        #get file name and extinsion
        file_location_arr = file.split("/")
        file_name_ext = file_location_arr[len(file_location_arr)-1]
        file_name_arr = file_name_ext.split(".")
        file_name = file_name_arr[0]     
        file_ext = file_name_arr[1]
        file_extinsion = file_ext.split("_")
        extnsn = file_extinsion[0]
        
        #read file
        with open(file,'rb') as file2:
            file3 = file2.read()
            
        #get the key generated from password
        key = gen_key(passw)
        
        #make cipher from key
        cipher = Fernet(key)
        
        #encrypt file
        decrypt_file = cipher.decrypt(file3)
        
        message = decrypt_file.decode()
        
        #save decrypted
        with open("./Decrypted/"+file_name+"."+extnsn,"w") as ef:
            ef.write(message)

        print(colored("Decrypted File Can be Found under Decrypted Folder "+file_name+"."+extnsn))
        
        #main menu or exit
        whreto = input(colored("Type E(exit) M(Main menu)","green"))
        if whreto.lower() == "e":
            os.system("exit")
        elif whreto.lower() == "m":
            banner(currentos)
        else:
            print(colored("Wrong Input...","red"))
            os.system("exit")
            
#message decryption
def message_decrypt(currentos):
    if currentos == "windows":
        os.system("cls")
        
        #file location
        file = input(colored("File Location -->> ","green"))
        
        #password to decrypt
        passw = input(colored("Password -->> ","green"))
        
        #encode password
        passw = passw.encode()
        
        #replace whiteplace
        file = file.replace('"','')
        file = file.strip()
        
        #read file
        with open(file,'rb') as file2:
            file3 = file2.read()
            
        #get the key generated from password
        key = gen_key(passw)
        
        #make cipher from key
        cipher = Fernet(key)
        
        #encrypt file
        decrypt_file = cipher.decrypt(file3)
        
        message = decrypt_file.decode()
        
        #save decrypted
        with open("./Decrypted/message.txt","w") as ef:
            ef.write(message)
            
        print(colored("Decrypted Message: "+message,"green"))
        print(colored("Decrypted File Can be Found under Decrypted Folder message.txt","green"))
        
        #main menu or exit
        whreto = input(colored("Type E(exit) M(Main menu)","green"))
        if whreto.lower() == "e":
            os.system("exit")
        elif whreto.lower() == "m":
            banner(currentos)
        else:
            print(colored("Wrong Input...","red"))
            os.system("exit")
    elif currentos == "linux":
        os.system("clear")
        
        #file location
        file = input(colored("File Location -->> ","green"))
        
        #password to decrypt
        passw = input(colored("Password -->> ","green"))
        
        #encode password
        passw = passw.encode()
        
        #replace whiteplace
        file = file.replace('"','')
        file = file.strip()
        
        #read file
        with open(file,'rb') as file2:
            file3 = file2.read()
            
        #get the key generated from password
        key = gen_key(passw)
        
        #make cipher from key
        cipher = Fernet(key)
        
        #encrypt file
        decrypt_file = cipher.decrypt(file3)
        
        message = decrypt_file.decode()
        
        #save decrypted
        with open("./Decrypted/message.txt","w") as ef:
            ef.write(message)
            
        print(colored("Decrypted Message: "+message,"green"))
        print(colored("Decrypted File Can be Found under Decrypted Folder message.txt","green"))
        
        #main menu or exit
        whreto = input(colored("Type E(exit) M(Main menu)","green"))
        if whreto.lower() == "e":
            os.system("exit")
        elif whreto.lower() == "m":
            banner(currentos)
        else:
            print(colored("Wrong Input...","red"))
            os.system("exit")

#hide file in image
def hide_file(currentos):
    if currentos == "windows":
        os.system("cls")
        #get file to hide
        file = input(colored("File Location -->> ","green"))
        #remove " and whitespace
        file = file.replace('"','')
        file = file.strip()
        #file extinsion
        file_addr = file.split("\\")
        file_name = file_addr[len(file_addr)-1]
        file_ext = file_name.split(".")
        ext = file_ext[len(file_ext)-1]
        #get image t hide file
        image = input(colored("Image To Hide File -->> ","green"))
        #get the image file name and extension
        img = image.replace('"','')
        img = img.strip()
        img_name_arr = img.split("/")
        img_name = img_name_arr[len(img_name_arr)-1]
        img_ext_arr = img_name.split(".")
        img_ext = img_ext_arr[len(img_ext_arr)-1]
        os.system("clear")
        if img_ext == "jpg" or img_ext == "jpeg":
            #try to hide message to file
            try:
                with open(file,'rb') as f:
                    data = f.read()
                data = data + file_name.encode()
                exifHeader.hide(img,"./Images/"+img_ext_arr[0]+".jpg", data)
            except Exception as e:
                print(colored(e,"red"))
            finally:
                print(colored("Filed Hidden In the Image...","green"))
                print(colored("File Is Under Images Folder "+img_ext_arr[0]+".jpg","yellow"))
                goto = input(colored("Type E(exit) M(main menu)"))
                if goto.lower() == "e":
                    os.system("exit")
                elif goto.lower() == "m":
                    banner(currentos)
                else:
                    print(colored("Wrong Input...","red"))
                    os.system("exit")

        elif img_ext == "png":
            try:
                with open(file,'rb') as f:
                    data = f.read()
                data = data + file_name.encode()
                hide = lsbset.hide(img,msg,generators.eratosthenes())
                hide.save("./Images/"+img_ext_arr[0]+".png")
            except Exception as e:
                print(colored(e,"red"))
            finally:
                print(colored("File Hidden In the Image...","green"))
                print(colored("File Is Under Images Folder "+img_ext_arr[0]+".jpg","yellow"))
                goto = input(colored("Type E(exit) M(main menu)"))
                if goto.lower() == "e":
                    os.system("exit")
                elif goto.lower() == "m":
                    banner(currentos)
                else:
                    print(colored("Wrong Input...","red"))
                    os.system("exit")
        #if image file is not supported
        else:
            print(colored("We Recommend using jpg,png Format Images","red"))
            os.system("exit")  
            
    elif currentos == "linux":
        os.system("clear")
        #get file to hide
        file = input(colored("File Location -->> ","green"))
        #remove " and whitespace
        file = file.replace('"','')
        file = file.strip()
        #file extinsion
        file_addr = file.split("/")
        file_name = file_addr[len(file_addr)-1]
        file_ext = file_name.split(".")
        ext = file_ext[len(file_ext)-1]
        #get image t hide file
        image = input(colored("Image To Hide File -->> ","green"))
        #get the image file name and extension
        img = image.replace('"','')
        img = img.strip()
        img_name_arr = img.split("/")
        img_name = img_name_arr[len(img_name_arr)-1]
        img_ext_arr = img_name.split(".")
        img_ext = img_ext_arr[len(img_ext_arr)-1]
        os.system("clear")
        if img_ext == "jpg" or img_ext == "jpeg":
            #try to hide message to file
            try:
                with open(file,'rb') as f:
                    data = f.read()
                data = data + file_name.encode()
                exifHeader.hide(img,"./Images/"+img_ext_arr[0]+".jpg", data)
            except Exception as e:
                print(colored(e,"red"))
            finally:
                print(colored("Filed Hidden In the Image...","green"))
                print(colored("File Is Under Images Folder "+img_ext_arr[0]+".jpg","yellow"))
                goto = input(colored("Type E(exit) M(main menu)"))
                if goto.lower() == "e":
                    os.system("exit")
                elif goto.lower() == "m":
                    banner(currentos)
                else:
                    print(colored("Wrong Input...","red"))
                    os.system("exit")

        elif img_ext == "png":
            try:
                with open(file,'rb') as f:
                    data = f.read()
                data = data + file_name.encode()
                hide = lsbset.hide(img,msg,generators.eratosthenes())
                hide.save("./Images/"+img_ext_arr[0]+".png")
            except Exception as e:
                print(colored(e,"red"))
            finally:
                print(colored("File Hidden In the Image...","green"))
                print(colored("File Is Under Images Folder "+img_ext_arr[0]+".jpg","yellow"))
                goto = input(colored("Type E(exit) M(main menu)"))
                if goto.lower() == "e":
                    os.system("exit")
                elif goto.lower() == "m":
                    banner(currentos)
                else:
                    print(colored("Wrong Input...","red"))
                    os.system("exit")
        #if image file is not supported
        else:
            print(colored("We Recommend using jpg,png Format Images","red"))
            os.system("exit")  


#reveal hidden file
def reveal_file(currentos):
    if currentos == "windows":
        os.system("cls")
        #get image with hidden file
        img = input(colored("Image File Location -->> ","green"))
        #whitespace
        img = img.replace('"','')
        img = img.strip()
        #get message out
        message = exifHeader.reveal(img)
        message = message.decode()
        #save in tmp file
        with open("tmp",'w') as f:
            f.write(message)
        #get the file
        with open("tmp","r") as r:
            lines = r.read()
            lines = lines.splitlines()
            content = lines[:-1]
            lines = lines[-1]
            for x in content:
                with open("./Messages/"+lines,'a') as f:
                    f.write(x+"\n")
        print(colored("File Unhidden...","green"))
        print(colored("File Can Be Found Under Messages Folder "+lines,"green"))
        goto = input(colored("Type E(exit) M(Main menu) -->> ","green"))
        if goto.lower() == "e":
            os.system("exit")
        elif goto.lower() == "m":
            banner(currentos)
        else:
            print(colored("Wrong Input","red"))
            os.system("exit")  
    elif currentos == "linux":
        os.system("clear")
        #get image with hidden file
        img = input(colored("Image File Location -->> ","green"))
        #whitespace
        img = img.replace('"','')
        img = img.strip()
        #get message out
        message = exifHeader.reveal(img)
        message = message.decode()
        #save in tmp file
        with open("tmp",'w') as f:
            f.write(message)
        #get the file
        with open("tmp","r") as r:
            lines = r.read()
            lines = lines.splitlines()
            content = lines[:-1]
            lines = lines[-1]
            for x in content:
                with open("./Messages/"+lines,'a') as f:
                    f.write(x+"\n")
        print(colored("File Unhidden...","green"))
        print(colored("File Can Be Found Under Messages Folder "+lines,"green"))
        goto = input(colored("Type E(exit) M(Main menu) -->> ","green"))
        if goto.lower() == "e":
            os.system("exit")
        elif goto.lower() == "m":
            banner(currentos)
        else:
            print(colored("Wrong Input","red"))
            os.system("exit")

#call the function to start the script
check_os()