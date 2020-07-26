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
import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet
import pyAesCrypt

#help menu
def help_menu():
    print(colored("The Hidden One Is A Script Based On Stegnography and Cryptography","green"))
    print("                                                                         ")
    print(colored("-h/--help: Help","green"))
    print(colored("-i/--interactive: Interactive","green"))
    print(colored("-hf: Hide File","green"))
    print(colored("-ht: Hide Text","green"))
    print(colored("-rt: Reveal Text","green"))
    print(colored("-rf: Reveal File","green"))
    print(colored("-et: Encrypt Text","green"))
    print(colored("-dt: Decrypt Text_location","green"))
    print(colored("-ef: Encrypt File","green"))
    print(colored("-df: Decrypt File","green"))
    print("                                                                         ")
    print(colored("########## Help Menu ##########","green"))
    print(colored("Type onehide -h or --help for help menu","green"))
    print(colored("Type onehide -i or --interactive for interactive menu","green"))
    print(colored("Type onehide -hf file_location -i image_location -o output_name to hide a file in image","green"))
    print(colored("Type onehide -ht text_to_hide -i image_location -o output_name to hide a text in image","green"))
    print(colored("Type onehide -rt file_location to reveal text from image","green"))
    print(colored("Type onehide -rf file_location to reveal file from image","green"))
    print(colored("Type onehide -et text_to_encrypt -p password -o output_name to encrypt any text","green"))
    print(colored("Type onehide -dt encrypted_file_location -p password -o output_name to decrypt text from file","green"))
    print(colored("Type onehide -ef file_location -p password -o output_name to encrypt file with aes","green"))
    print(colored("Type onehide -df file_location -p password  to decrypt aes file","green"))
    print(colored("########## End ##########","green"))
    

#pass argument from command line and save it
uinp = sys.argv[1:]

####################################################################
################# Check Arguments Given In Terminal ################
####################################################################
def check_args(uinp):
    #find os
    myoss = platform.platform()
    myoss = myoss.lower()   
    #open help menu if no arguments given
    if uinp == []:
        help_menu()
    #interactive menu
    elif uinp[0] == "-i" or uinp[0] == "--interactive":
        check_os("interactive")
    #help menu
    elif uinp[0] == "-h" or uinp[0] == "--help":
        help_menu()
    #command line hide file
    elif uinp[0] == "-hf":
        whole = " "
        whole = whole.join(uinp)
        whole_text =re.split('-hf | -i | -o',whole)
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
    #command line text hide
    elif uinp[0] == "-ht":
        whole = " "
        whole = whole.join(uinp)
        whole_text =re.split('-ht | -i | -o',whole)
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
                finally:
                    #call function based on os
                    if "windows" in myoss:
                        pass
                    elif "linux" in myoss:
                        hiding_linux_text(file,image,ext,saveas,'c')
            except Exception as e:
                help_menu()
        except Exception as e:
            help_menu()
    #command line text reveal
    elif uinp[0] == "-rt":
        whole = " "
        whole = whole.join(uinp)
        whole_text =re.split('-rt',whole)
        #file to hide
        try:
            image = whole_text[1]
            #get image extinsion
            img = image.replace('"','')
            img = img.strip()
            img_name_arr = img.split("/")
            img_name = img_name_arr[len(img_name_arr)-1]
            img_ext_arr = img_name.split(".")
            ext = img_ext_arr[len(img_ext_arr)-1]
            nm = img_ext_arr[len(img_ext_arr)-2]
            #call function based on os
            if "windows" in myoss:
                pass
            elif "linux" in myoss:
                revealing_linux_text(img,ext,nm,'c')
        except Exception as e:
            help_menu()
    #command line file reveal
    elif uinp[0] == "-rf":
        whole = " "
        whole = whole.join(uinp)
        whole_text =re.split('-rf',whole)
        #file to hide
        try:
            image = whole_text[1]
            #get image extinsion
            img = image.replace('"','')
            img = img.strip()
            img_name_arr = img.split("/")
            img_name = img_name_arr[len(img_name_arr)-1]
            img_ext_arr = img_name.split(".")
            ext = img_ext_arr[len(img_ext_arr)-1]
            nm = img_ext_arr[len(img_ext_arr)-2]
            #call function based on os
            if "windows" in myoss:
                pass
            elif "linux" in myoss:
                revealing_linux_file(img,ext,'c')
        except Exception as e:
            help_menu()
    #command line text encrypt
    elif uinp[0] == "-et":
        whole = " "
        whole = whole.join(uinp)
        whole_text =re.split('-et | -p | -o',whole)
        #file to hide
        try:
            text = whole_text[1]
            text = text.replace('"','')
            text = text.strip()
            #image
            try:
                password = whole_text[2]
                #get image extinsion
                img = password.replace('"','')
                img = img.strip()
                #save name
                try:
                    saveas = whole_text[3]
                    saveas = saveas.strip()
                except Exception as e:
                    saveas = "encrypt"
                #call function based on os
                if "windows" in myoss:
                    pass
                elif "linux" in myoss:
                    terminal_encrypt_linux(text,password,saveas)
            except:
                help_menu()
        except:
            help_menu()
    #command line text decrypt
    elif uinp[0] == "-dt":
        whole = " "
        whole = whole.join(uinp)
        whole_text =re.split('-dt | -p | -o',whole)
        #file to hide
        try:
            file = whole_text[1]
            file = file.replace('"','')
            file = file.strip()
            #image
            try:
                password = whole_text[2]
                #get image extinsion
                password = password.replace('"','')
                password = password.strip()
                #save name
                try:
                    saveas = whole_text[3]
                    saveas = saveas.strip()
                except Exception as e:
                    saveas = "decrypt"
                #call function based on os
                if "windows" in myoss:
                    pass
                elif "linux" in myoss:
                    terminal_decrypt_linux(file,password,saveas)
            except:
                help_menu()
        except:
            help_menu()
    #command line file encrypt
    elif uinp[0] == "-ef":
        #buffer
        bufferSize = 64 * 1024
        #password
        whole = " "
        whole = whole.join(uinp)
        whole_text =re.split('-ef | -p',whole)
        #file to hide
        try:
            file = whole_text[1]
            file = file.replace('"','')
            file = file.strip()
            try:
                password = whole_text[2]
                password = password.replace('"','')
                password = password.strip()
            except Exception as e:
                help_menu()
        except Exception as e:
            help_menu()
        finally:
            terminal_encrypt_file(file,password,bufferSize) 
    #commmand line file decrypt
    elif uinp[0] == "-df":
        #buffer
        bufferSize = 64 * 1024
        #password
        whole = " "
        whole = whole.join(uinp)
        whole_text =re.split('-df | -p',whole)
        #file to hide
        try:
            file = whole_text[1]
            file = file.replace('"','')
            file = file.strip()
            try:
                password = whole_text[2]
                password = password.replace('"','')
                password = password.strip()
            except Exception as e:
                help_menu()
        except Exception as e:
            help_menu()
        finally:
            terminal_decrypt_file(file,password,bufferSize)   
    else:
        help_menu()
####################################################################
############# Os Based Codes For Interactive Menu ################## 
####################################################################
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

####################################################################
########################### codes for Windows ######################
####################################################################
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

#####################################################################
############################# codes for linux #######################
#####################################################################

##################### Banner For Linux Os ####################
def banner_linux(day,times):
    os.system("clear")
    #ascii menu
    print(colored("########################################################################","green"))                                                               
    print(colored("#  _____  _           _____  _    _    _              _____            #","green"))
    print(colored("# |_   _|| |_  ___   |  |  ||_| _| | _| | ___  ___   |     | ___  ___  #","green"))
    print(colored("#   | |  |   || -_|  |     || || . || . || -_||   |  |  |  ||   || -_| #","green"))
    print(colored("#   |_|  |_|_||___|  |__|__||_||___||___||___||_|_|  |_____||_|_||___| #","green"))
    print(colored("#                                                                      #","green"))
    print(colored("# by r3Vibe                                                       V0.1 #","green")) 
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
        
##################### stagnography menu ######################
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

################# Hiding ################
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
        
################# hide file in image get variables ##################
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

################# hide the file #####################################
def hiding_linux(file,image,extension,saveas,type):
    os.system("clear")
    #file extinsion
    file_addr = file.split("/")
    file_name = file_addr[len(file_addr)-1]
    #file name
    filename = file_name.encode()
    #image name
    save_name = saveas+"."+extension
    print(colored("Processing...","green"))
    time.sleep(1)
    if extension == "jpg" or extension == "jpeg" or extension == "tiff":
        try:
            with open(file,"rb") as f:
                data = f.read()
            data = data + filename
            exifHeader.hide(image,"./Hidden/%s"%save_name,data)
        except Exception as e:
            print(colored(e,"red"))
            time.sleep(1)
            if type == "i":
                file_hide_linux()
            elif type == "c":
                os.system("exit")
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
    
    #problem with png need testing
    #elif extension == "png":
    #    try:
    #        with open(file,"rb") as f:
    #            data = f.read()
    #        data = data + filename
    #        hide = lsbset.hide(image,data,generators.eratosthenes())
    #        hide.save("./Hidden/%s"%save_name)
    #    except Exception as e:
    #        print(colored(e,"red"))
    #        time.sleep(1)
    #        file_hide_linux()
    #    finally:
    #        dire = os.getcwd()
    #        if type == 'i':
    #            os.system("clear")
    #            print(colored("Successfully Hidden File In Image","green"))
    #            print(colored("Location: %s/%s"%(dire+"/Hidden",save_name),"green"))
    #            print(colored("Press E(exit) Or M(Main Menu)","green"))
    #            def go_to(key):
    #                if key == keyboard.KeyCode(char='e'):
    #                    return False
    #                elif key == keyboard.KeyCode(char='m'):
    #                    banner_linux(day,times)
    #                    return False
    #            with Listener(on_release=go_to) as l:
    #                l.join()
    #        elif type == 'c':
    #            os.system("clear")
    #            print(colored("Successfully Hidden File In Image","green"))
    #            print(colored("Location: %s/%s"%(dire+"/Hidden",save_name),"green"))
    else:
        print(colored("%s Is Not Supported By This Script Try Other Image..."%extension,"red"))
        time.sleep(1)
        file_hide_linux()

################# hide text in image get variables ##################
def text_hide_linux():
    os.system("clear")
    print(colored("Stagnography Text Hide","green"))
    print(colored("######################","green"))
    #get the file
    the_text = input(colored("Enter Text: ","green"))
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
    hiding_linux_text(the_text,the_img,ext,name_to_save,'i')
    
#hide the text
def hiding_linux_text(file,image,extension,saveas,type):
    os.system("clear")
    save_name = saveas+"."+extension
    print(colored("Processing...","green"))
    time.sleep(1)
    if extension == "jpg" or extension == "jpeg" or extension == "tiff":
        try:
            data = file.encode()
            exifHeader.hide(image,"./Hidden/%s"%save_name,data)
        except Exception as e:
            print(colored(e,"red"))
            time.sleep(2)
            if type == "i":
                text_hide_linux()
            elif type == "c":
                os.system("exit")
        finally:
            dire = os.getcwd()
            if type == 'i':
                os.system("clear")
                print(colored("Successfully Hidden Text In Image","green"))
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
                print(colored("Successfully Hidden Text In Image","green"))
                print(colored("Location: %s/%s"%(dire+"/Hidden",save_name),"green"))
                
    elif extension == "png":
        try:
            data = file
            hide = lsbset.hide(image,data,generators.eratosthenes())
            hide.save("./Hidden/%s"%save_name)
        except Exception as e:
            print(colored(e,"red"))
            time.sleep(1)
            if type  == "i":
                text_hide_linux()
            elif type == "c":
                os.system("exit")
        finally:
            dire = os.getcwd()
            if type == 'i':
                os.system("clear")
                print(colored("Successfully Hidden Text In Image","green"))
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
                print(colored("Successfully Hidden Text In Image","green"))
                print(colored("Location: %s/%s"%(dire+"/Hidden",save_name),"green"))
    else:
        print(colored("%s Is Not Supported By This Script Try Other Image..."%extension,"red"))
        time.sleep(2)
        file_hide_linux()

################# Hiding ################

################# Reveal ################
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

#file reveal get variables
def file_reveal_linux():
    os.system("clear")
    print(colored("Stagnography File Reveal","green"))
    print(colored("########################","green"))
    #get the image
    the_img = input(colored("Location Of Image: ","green"))
    #filter image location
    the_img = the_img.replace('"','')
    the_img = the_img.strip()
    #get image extension
    img_ext = the_img.split(".")
    ext = img_ext[len(img_ext)-1]
    #call function
    revealing_linux_file(the_img,ext,'i')

#text reveal get variables
def text_reveal_linux():
    os.system("clear")
    print(colored("Stagnography Text Reveal","green"))
    print(colored("########################","green"))
    #get the image
    the_img = input(colored("Location Of Image: ","green"))
    #filter image location
    the_img = the_img.replace('"','')
    the_img = the_img.strip()
    #get image extension
    img_ext = the_img.split("/")
    img_nm = img_ext[len(img_ext)-1]
    all_ext = img_nm.split(".")
    ext = all_ext[len(all_ext)-1]
    nm = all_ext[len(all_ext)-2]
    #call function
    revealing_linux_text(the_img,ext,nm,'i')   

#reveal text
def revealing_linux_text(image,ext,name,mode):
    os.system("clear")
    print(colored("Processing...","green"))
    if ext == "jpg" or ext == "jpeg" or ext == "tiff":
        try:
            message = exifHeader.reveal(image)
            message = message.decode()
            #save in tmp file
            with open("./Revealed/%s.txt"%name,'w') as f:
                f.write(message)
        except Exception as e:
            print(colored(e,"red"))
            time.sleep(1)
            if mode == "i":
                text_reveal_linux()
            elif mode == "c":
                os.system("exit")
        finally:
            dire = os.getcwd()
            if mode == 'i':
                os.system("clear")
                print(colored("Text has been revealed","green"))
                print(colored("Text: %s"%message,"green"))
                print(colored("Location: %s/Revealed/%s.txt"%(dire,name),"green"))
                print(colored("Press E(exit) Or M(Main Menu)","green"))
                def go_to(key):
                    if key == keyboard.KeyCode(char='e'):
                        return False
                    elif key == keyboard.KeyCode(char='m'):
                        banner_linux(day,times)
                        return False
                with Listener(on_release=go_to) as l:
                    l.join()
            elif mode == 'c':
                os.system("clear")
                print(colored("Successfully Revealed Text From Image","green"))
                print(colored("Text: %s"%message,"green"))
                print(colored("Location: %s/Revealed/%s.txt"%(dire,name),"green"))
    elif ext == "png":
        try:
            message = lsbset.reveal(image,generators.eratosthenes())
            message = message.decode()
            #save in tmp file
            with open("./Revealed/%s.txt"%name,'w') as f:
                f.write(message)
        except Exception as e:
            print(colored(e,"red"))
            time.sleep(1)
            if mode == "i":
                text_reveal_linux()
            elif mode == "c":
                os.system("exit")
        finally:
            dire = os.getcwd()
            if mode == 'i':
                os.system("clear")
                print(colored("Text has been revealed","green"))
                print(colored("Text: %s"%message,"green"))
                print(colored("Location: %s/Revealed/%s.txt"%(dire,name),"green"))
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
                print(colored("Successfully Revealed Text From Image","green"))
                print(colored("Location: %s/Revealed/%s.txt"%(dire,name),"green"))
    else:
        print(colored("%s Is Not Supported By This Script Try Other Image..."%ext,"red"))
        time.sleep(1)
        text_reveal_linux()  

#reveal file code
def revealing_linux_file(location,ext,mode):
    os.system("clear")
    print(colored("Processing...","green"))
    if ext == "jpg" or ext == "jpeg" or ext == "tiff":
        try:
            message = exifHeader.reveal(location)
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
                    with open("./Revealed/%s"%lines,'a') as f:
                        f.write("%s\n"%x)
                f.close()
            os.system("rm tmp")
        except Exception as e:
            print(colored(e,"red"))
            time.sleep(1)
            if mode == "i":
                file_reveal_linux()
            elif mode == "c":
                os.system("exit")
        finally:
            dire = os.getcwd()
            if mode == 'i':
                os.system("clear")
                print(colored("File has been revealed","green"))
                print(colored("Location: %s/Revealed/%s"%(dire,lines),"green"))
                print(colored("Press E(exit) Or M(Main Menu)","green"))
                def go_to(key):
                    if key == keyboard.KeyCode(char='e'):
                        return False
                    elif key == keyboard.KeyCode(char='m'):
                        banner_linux(day,times)
                        return False
                with Listener(on_release=go_to) as l:
                    l.join()
            elif mode == 'c':
                os.system("clear")
                print(colored("Successfully Revealed File From Image","green"))
                print(colored("Location: %s/Revealed/%s"%(dire,lines),"green"))
    #elif ext == "png":
    #    try:
    #        message = lsbset.reveal(location,generators.eratosthenes())
    #        #save in tmp file
    #        with open("tmp",'w') as f:
    #            f.write(message)
    #        #get the file
    #        with open("tmp","r") as r:
    #            lines = r.read()
    #            lines = lines.splitlines()
    #            content = lines[:-1]
    #            lines = lines[-1]
    #            #for x in content:
    #            #    with open("./Revealed/%s"%lines,'a') as f:
    #            #        f.write(x+"\n")
    #            #f.close()
    #        os.system("rm tmp")
    #    except Exception as e:
    #        print(colored(e,"red"))
    #        time.sleep(1)
    #        file_reveal_linux()
    #    finally:
    #        dire = os.getcwd()
    #        if mode == 'i':
    #            os.system("clear")
    #            print(colored("File has been revealed","green"))
    #            print(colored("Location: %s/Revealed/%s"%(dire,lines),"green"))
    #            print(colored("Press E(exit) Or M(Main Menu)","green"))
    #            def go_to(key):
    #                if key == keyboard.KeyCode(char='e'):
    #                    return False
    #                elif key == keyboard.KeyCode(char='m'):
    #                    banner_linux(day,times)
    #                    return False
    #            with Listener(on_release=go_to) as l:
    #                l.join()
    #        elif type == 'c':
    #            os.system("clear")
    #            print(colored("Successfully Revealed File From Image","green"))
    #            print(colored("Location: %s/%s"%(dire+"/Revealed",lines),"green"))
    else:
        print(colored("%s Is Not Supported By This Script Try Other Image..."%ext,"red"))
        time.sleep(1)
        file_reveal_linux()
        
################# Reveal ################
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

########## Encryption ##########

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
        file_encrypt_linux('i')
    elif user == "2":
        text_encrypt_linux('i')
    elif user == "3":
        crypto_linux()
    else:
        print(colored("Wrong Input...","red"))
        time.sleep(1)
        encrypt_linux()

#file encrypt variables
def file_encrypt_linux(mode):
    os.system("clear")
    #get file location
    file = input(colored("Enter File Location: ","green"))
    #remove " " from file
    file = file.replace('"','')
    file = file.strip()
    #get file name
    file_name_arr = file.split("/")
    file_name = file_name_arr[len(file_name_arr)-1]
    user_pass = input(colored("Passwword: ","green"))
    #buffer size for encryption
    bufferSize = 64 * 1024
    dire = os.getcwd()
    os.system("clear")
    print(colored("Processiong....","green"))
    try:
        pyAesCrypt.encryptFile(file, "./Encrypted/%s.aes"%file_name, user_pass, bufferSize)
    except Exception as e:
        print(colored(e,"red"))
        time.sleep(2)
        if mode == "i":
            file_encrypt_linux("i")
        elif mode == "c":
            file_encrypt_linux("c")
    finally:
        if mode == 'i':
            os.system("clear")
            print(colored("Encryption Completed...","green"))
            print(colored("Location: %s/Encrypted/%s"%(dire,file_name+".aes"),"green"))
            print(colored("Press E(exit) Or M(Main Menu)","green"))
            def go_to(key):
                if key == keyboard.KeyCode(char='e'):
                    return False
                elif key == keyboard.KeyCode(char='m'):
                    banner_linux(day,times)
                    return False
            with Listener(on_release=go_to) as l:
                l.join()
        elif mode == 'c':
            os.system("clear")
            print(colored("Encryption Completed...","green"))
            print(colored("Location: %s/Encrypted/%s"%(dire,file_name+".aes"),"green"))       

#encrypt file in terminal
def terminal_encrypt_file(file,password,bufferSize) :
    dire = os.getcwd()
    os.system("clear")
    files_name = file.split("/")
    file_name = files_name[len(files_name)-1]
    print(colored("Processiong....","green"))
    try:
        pyAesCrypt.encryptFile(file, "./Encrypted/%s.aes"%file_name, password, bufferSize)
    except Exception as e:
        print(colored(e,"red"))
        time.sleep(2)
        if mode == "i":
            file_encrypt_linux("i")
    finally:
        os.system("clear")
        print(colored("Encryption Completed...","green"))
        print(colored("Location: %s/Encrypted/%s"%(dire,file_name+".aes"),"green"))       
    

#text encrypt variables
def text_encrypt_linux(mode):
    os.system("clear")
    text = input(colored("Enter Text: ","green"))
    user_pass = input(colored("Passwword: ","green"))
    saveas = input(colored("Save As: ","green"))
    os.system("clear")
    print(colored("Processiong....","green"))
    #encode both pass and text
    user_pass = user_pass.encode()
    text = text.encode()
    #get key
    key = gen_key(user_pass)
    #cipher generate
    cipher = Fernet(key)
    #get directory
    dire = os.getcwd()
    #encrypt
    try:
        encrypted = cipher.encrypt(text)
    except Exception as e:
        print(colored(e,"red"))
        time.sleep(2)
        if mode == "i":
            text_encrypt_linux("i")
        elif mode == "c":
            text_encrypt_linux("c")
    finally:
        with open("./Encrypted/%s"%saveas,'wb') as f:
            f.write(encrypted)
        f.close()
        if mode == 'i':
            os.system("clear")
            print(colored("Encryption Completed...","green"))
            print(colored("Encrypted: %s"%encrypted,"green"))
            print(colored("Location: %s/Encrypted/%s"%(dire,saveas),"green"))
            print(colored("Press E(exit) Or M(Main Menu)","green"))
            def go_to(key):
                if key == keyboard.KeyCode(char='e'):
                    return False
                elif key == keyboard.KeyCode(char='m'):
                    banner_linux(day,times)
                    return False
            with Listener(on_release=go_to) as l:
                l.join()
        elif mode == 'c':
            os.system("clear")
            print(colored("Encryption Completed...","green"))
            print(colored("Encrypted: %s"%encrypted,"green"))
            print(colored("Location: %s/Encrypted/%s"%(dire,saveas),"green"))

#encrypt from terminal
def terminal_encrypt_linux(text,password,saveas):
    print(colored("Processiong....","green"))
    #encode both pass and text
    user_pass = password.encode()
    text = text.encode()
    #get key
    key = gen_key(user_pass)
    #cipher generate
    cipher = Fernet(key)
    #get directory
    dire = os.getcwd()
    #encrypt
    try:
        encrypted = cipher.encrypt(text)
    except Exception as e:
        print(colored(e,"red"))
        os.system("exit")
    finally:
        with open("./Encrypted/%s"%saveas,'wb') as f:
            f.write(encrypted)
        f.close()
        os.system("clear")
        print(colored("Encryption Completed...","green"))
        print(colored("Encrypted: %s"%encrypted,"green"))
        print(colored("Location: %s/Encrypted/%s"%(dire,saveas),"green"))

########## Encryption ##########

########## Decryption ##########

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
        file_decrypt_linux("i")
    elif user == "2":
        text_decrypt_linux("i")
    elif user == "3":
        crypto_linux()
    else:
        print(colored("Wrong Input...","red"))
        time.sleep(1)
        decrypt_linux()

#decrypt files
def file_decrypt_linux(mode):
    os.system("clear")
    #get file location
    file = input(colored("Enter File Location: ","green"))
    #remove " " from file
    file = file.replace('"','')
    file = file.strip()
    #get file name
    file_name_arr = file.split("/")
    file_name = file_name_arr[len(file_name_arr)-1]
    file_name = file_name.split(".")
    file_ext = file_name[1]
    file_na = file_name[0]
    file_name = file_na+"."+file_ext
    user_pass = input(colored("Passwword: ","green"))
    #buffer size for encryption
    bufferSize = 64 * 1024
    dire = os.getcwd()
    os.system("clear")
    print(colored("Processiong....","green"))
    try:
        pyAesCrypt.decryptFile(file, "./Decrypted/%s"%file_name, user_pass, bufferSize)
    except Exception as e:
        print(colored(e,"red"))
        time.sleep(2)
        if mode == "i":
            file_decrypt_linux("i")
        elif mode == "c":
            file_decrypt_linux("c")
    finally:
        if mode == 'i':
            os.system("clear")
            print(colored("Decryption Completed...","green"))
            print(colored("Location: %s/Decrypted/%s"%(dire,file_name),"green"))
            print(colored("Press E(exit) Or M(Main Menu)","green"))
            def go_to(key):
                if key == keyboard.KeyCode(char='e'):
                    return False
                elif key == keyboard.KeyCode(char='m'):
                    banner_linux(day,times)
                    return False
            with Listener(on_release=go_to) as l:
                l.join()
        elif mode == 'c':
            os.system("clear")
            print(colored("Decryption Completed...","green"))
            print(colored("Location: %s/Decrypted/%s"%(dire,file_name),"green"))      

#text decrypt text
def text_decrypt_linux(mode):
    os.system("clear")
    text = input(colored("Enter File Location: ","green"))
    user_pass = input(colored("Passwword: ","green"))
    name = input(colored("Enter File Name After Decryption: ","green"))
    os.system("clear")
    print(colored("Processiong....","green"))
    #encode both pass and text
    text = text.replace('"','')
    text = text.strip()
    user_pass = user_pass.encode()
    name = name.replace('"','')
    name  = name.strip()
    #get key
    key = gen_key(user_pass)
    #cipher generate
    cipher = Fernet(key)
    #get directory
    dire = os.getcwd()
    #encrypt
    try:
        with open(text,"rb") as r:
            text = r.read()
        decrypted = cipher.decrypt(text)
        with open("./Decrypted/%s.txt"%name,"w") as f:
            f.write(decrypted.decode())
            f.close()
    except Exception as e:
        print(colored(e,"red"))
        time.sleep(2)
        if mode == "i":
            text_decrypt_linux("i")
        elif mode == "c":
            os.system("exit")
    finally:
        os.system("clear")
        print(colored("Decryption Completed...","green"))
        print(colored("Text: %s"%decrypted.decode(),"green"))
        print(colored("Location: %s/Decrypted/%s.txt"%(dire,name),"green"))
        print(colored("Press E(exit) Or M(Main Menu)","green"))
        def go_to(key):
            if key == keyboard.KeyCode(char='e'):
                return False
            elif key == keyboard.KeyCode(char='m'):
                banner_linux(day,times)
                return False
        with Listener(on_release=go_to) as l:
            l.join()

#text decryption from terminal
def terminal_decrypt_linux(file,password,fname):
    os.system("clear")
    print(colored("Processing....","green"))
    #encode  password
    user_pass = password.encode()
    #get key
    key = gen_key(user_pass)
    #cipher generate
    cipher = Fernet(key)
    #get directory
    dire = os.getcwd()
    #encrypt
    try:
        with open(file,"rb") as r:
            content = r.read()
        decrypted = cipher.decrypt(content)
        with open("./Decrypted/%s.txt"%fname,"w") as f:
            f.write(decrypted.decode())
            f.close()
    except Exception as e:
        print(colored(e,"red"))
        os.system("exit")
    finally:
        os.system("clear")
        print(colored("Decryption Completed...","green"))
        print(colored("Text: %s"%decrypted.decode(),"green"))
        print(colored("Location: %s/Decrypted/%s.txt"%(dire,fname),"green"))

#file decrypt linux
def terminal_decrypt_file(file,password,bufferSize):
    #remove " " from file
    file = file.replace('"','')
    file = file.strip()
    #get file name
    file_name_arr = file.split("/")
    file_name = file_name_arr[len(file_name_arr)-1]
    file_name = file_name.split(".")
    file_ext = file_name[1]
    file_na = file_name[0]
    file_name = file_na+"."+file_ext
    #current directory
    dire = os.getcwd()
    os.system("clear")
    print(colored("Processiong....","green"))
    try:
        pyAesCrypt.decryptFile(file, "./Decrypted/%s"%file_name, password, bufferSize)
    except Exception as e:
        print(colored(e,"red"))
        time.sleep(2)
        if mode == "i":
            file_decrypt_linux("i")
        elif mode == "c":
            file_decrypt_linux("c")
    finally:
        os.system("clear")
        print(colored("Decryption Completed...","green"))
        print(colored("Location: %s/Decrypted/%s"%(dire,file_name),"green"))      
########## Decryption ##########

#################################################
########### Generate Key With Password ##########
#################################################
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


#call the function to determine os
check_args(uinp)
