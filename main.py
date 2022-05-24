# required imports
from ast import arg
from email.mime import base
import os,platform
from Modules.encryption import Cryptography , Generators,Decoders
from Modules.stegano import Stegano
from Modules.aes import EncryptFile
from pathlib import Path
from time import sleep 
import argparse
# # getting system arguments
# cmdargs = sys.argv[1:]

# Initialize parser
parser = argparse.ArgumentParser(description="Cryptography And Steganography Script.",prog='hideme')

# Adding optional argument
parser.add_argument("-i", "--interactive", help = "hideme -i (Starts Script In Interactive Mode.)",action='store_true')
parser.add_argument("-c", "--clean", help = "hideme --clean (Delete Unnecessary Files.)",action='store_true')
parser.add_argument("-p", "--password", help = "hideme -p password (Pass Password For Encryption And Decryption.)")
parser.add_argument("-s", "--salt", help = "hideme -s salt (Pass salt For Decryption.)")
parser.add_argument("-im", "--image", help = "hideme -im image location (Image To Hide Text/File.)")
parser.add_argument("-te", "--textencrypt", help = "hideme -te 'some text' -p password (Encrypt The Text. Dont Forget To Pass The Text Inside Quotation)")
parser.add_argument("-fe", "--fileencrypt", help = "hideme -fe File Location -p password (Encrypt File.)")
parser.add_argument("-td", "--textdecrypt", help = "hideme -td Hash -p password -s Salt (Decrypt Hash To Text.)")
parser.add_argument("-fd", "--filedecrypt", help = "hideme -fd File Location -p password -s Salt (Decrypt File.)")
parser.add_argument("-th", "--texthide", help = "hideme -th 'some text' -im Image Location (Hide Text in Image.Dont Forget To Pass The Text Inside Quotation)")
parser.add_argument("-fh", "--filehide", help = "hideme -fh File Location -im Image Location (Hide File in Image.)")
parser.add_argument("-tr", "--textreveal", help = "hideme -tr File Location(Reveal Text From Image.)")
parser.add_argument("-fr", "--filereveal", help = "hideme -fr File Location(Reveal File From Image.)")
parser.add_argument("-ae", "--aesencrypt", help = "hideme -ae File Location -p password (Encrypt File AES Mode.)")
parser.add_argument("-ad", "--aesdecrypt", help = "hideme -ad File Location -p password (Decrypt File AES Mode.)")
 
# Read arguments from command line
arguments = parser.parse_args()


# app location in system
base_dir = Path(__file__).resolve().parent


def handel_arguments(arguments):
    # interactive mode banner open
    if arguments.interactive:
        banner()
    # clean folders delet all files
    elif arguments.clean:
        clean_folders(cmd=True)
    # start text encryption
    elif arguments.textencrypt:
        if not arguments.password:
            print('Provide Password For Encryption')
        elif not arguments.textencrypt:
            print('Provide Text For Encryption')
        else:
            text_encrypt(text=arguments.textencrypt,password=arguments.password,cmd=True)
    # start text decryption
    elif arguments.textdecrypt:
        if not arguments.password:
            print('Provide Password For Decryption')
        elif not arguments.textdecrypt:
            print("Provide Hash For Decryption")
        elif not arguments.salt:
            print('Provide Salt For Decryption')
        else:
            text_decrypt(hash=arguments.textdecrypt,password=arguments.password,salt=arguments.salt,cmd=True)
    # file encryption
    elif arguments.fileencrypt:
        if not arguments.password:
            print('Provide Password For Encryption')
        elif not arguments.fileencrypt:
            print('Provide File For Encryption')
        else:
            file_encrypt(file=arguments.fileencrypt,password=arguments.password,cmd=True)
    # file decryption
    elif arguments.filedecrypt:
        if not arguments.password:
            print('Provide Password For Decryption')
        elif not arguments.filedecrypt:
            print('Provide File For Decryption')
        elif not arguments.salt:
            print('Provide Salt For Decryption')
        else:
            file_decrypt(file=arguments.filedecrypt,password=arguments.password,salt=arguments.salt,cmd=True)
    # text hide in image
    elif arguments.texthide:
        if not arguments.texthide:
            print("Provide Text For Hiding")
        elif not arguments.image:
            print("Provide Image To Hide Text/File")
        else:
            text_hide(text=arguments.texthide,image=arguments.image,cmd=True)
    # file hide in image
    elif arguments.filehide:
        if not arguments.filehide:
            print("Provide File For Hiding")
        elif not arguments.image:
            print("Provide Image To Hide Text/File")
        else:
            file_hide(file=arguments.filehide,image=arguments.image,cmd=True)
    # text reveal in image
    elif arguments.textreveal:
        if not arguments.textreveal:
            print("Provide File For Revealing")
        else:
            text_reavel(image=arguments.textreveal,cmd=True)
    # file reveal in image
    elif arguments.filereveal:
        if not arguments.filereveal:
            print("Provide File For Revealing")
        else:
            file_reavel(image=arguments.filereveal,cmd=True)
    # aes encryption
    elif arguments.aesencrypt:
        if not arguments.aesencrypt:
            print("Provide File For Encryption")
        if not arguments.password:
            print("Provide Password Encryption")
        else:
            aes_encryption(file=arguments.aesencrypt,password=arguments.password,cmd=True)
    # aes decryption
    elif arguments.aesdecrypt:
        if not arguments.aesdecrypt:
            print("Provide File For Decryption")
        if not arguments.password:
            print("Provide Password Decryption")
        else:
            aes_decryption(file=arguments.aesdecrypt,password=arguments.password,cmd=True)
    else:
        parser.print_help()

# aes encryption
def aes_encryption(file=None,password=None,cmd=False):
    if file is None:
        file = input("File Location=> ")
    if password is None:
        password = input("Enter Password=> ")
    
    f = EncryptFile(file=file,password=password).encrypt_now()
    loc = os.path.join(base_dir,'encrypted',f)
    print(f"File Location Is {loc}")
    if cmd:
        exit()
    else:
        userinput = input("Would You Like To Go To Main Menu Or Exit(Y or N) ?")
        if userinput.lower() == 'y':
            banner()
        elif userinput.lower() == 'n':
            exit()
        else:
            print('Wrong Input!')
            sleep(5)
            banner()

# aes decryption
def aes_decryption(file=None,password=None,cmd=False):
    if file is None:
        file = input("File Location=> ")
    if password is None:
        password = input("Enter Password=> ")
    
    f = EncryptFile(file=file,password=password).decrypt_now()
    loc = os.path.join(base_dir,'decrypted',f)
    print(f"File Location Is {loc}")
    if cmd:
        exit()
    else:
        userinput = input("Would You Like To Go To Main Menu Or Exit(Y or N) ?")
        if userinput.lower() == 'y':
            banner()
        elif userinput.lower() == 'n':
            exit()
        else:
            print('Wrong Input!')
            sleep(5)
            banner()

# section cryptography
# encrypt file 
def file_encrypt(file=None,password=None,cmd=False):
    if file is None:
        file = input("Enter File Location=> ")
    if password is None:
        password = input("Enter Password=> ")
    # generates new salt
    salt = Generators().gen_salt()
    # decode salt for printinmg
    salt_print = Decoders().decode_salt(salt)
    try:
        the_file = Cryptography(password=password,salt=salt,file=file).file_encrypt()
    except Exception as e:
        raise e
    else:
        show_loc = os.path.join(base_dir,'encrypted',f'{the_file}')
        print(f"Save The Salt For Decryption Later: {salt_print}")
        print(f"Encrypted File Location: {show_loc}")
        userinput = input("Would You Like To Save The Salt In A File(Y or N) ?")
        if userinput.lower() == 'y':
            location = os.path.join(base_dir,'info','file_encrypt_data.txt')
            f = open(location,"w")
            f.write(f"Salt: {salt_print}")
            f.close()
            print(f"Salt Saved In {location}")
            if cmd:
                exit()
            else:
                sleep(5)
                banner()
        elif userinput.lower() == 'n':
            if cmd:
                exit()
            else:
                banner()
        else:
            print('Wrong Input!')
            if cmd:
                exit()
            else:
                sleep(5)
                banner()

# encrypt text to hash
def text_encrypt(password=None,text=None,cmd=False):
    if password is None:
        password = input("Enter Password=>> ")
    if text is None:
        text = input("Enter Text=>> ")
    # generate salt
    salt = Generators().gen_salt()
    salt_print = Decoders().decode_salt(salt)
    try:
        enc_text = Cryptography(password=password,text=text,salt=salt).text_encrypt()
    except Exception as e:
        raise e
    else:
        print(f"Save The Salt For Decryption Later: {salt_print}")
        print(f"Your Hash Is: {enc_text}")
        userinput = input("Would You Like To Save Details On A File(Y or N) ?")
        if userinput.lower() == 'y':
            location = os.path.join(base_dir,'info','text_encrypt_data.txt')
            f = open(location,"w")
            f.write(f"Salt: {salt_print}\nHash: {enc_text}")
            f.close()
            print(f"Details Saved In {location}")
            if cmd:
                exit()
            else:
                sleep(5)
                banner()
        elif userinput.lower() == 'n':
            if cmd:
                exit()
            else:
                banner()
        else:
            print('Wrong Input!')
            if cmd:
                exit()
            else:
                sleep(5)
                banner()

# decrypt any file
def file_decrypt(file=None,password=None,salt=None,cmd=False):
    if file is None:
        file = input("Enter File Location=> ")
    if password is None:
        password = input("Enter Password=> ")
    if salt is None:
        salt = input("Enter The Salt=>> ")
    salt = Decoders().make_decode_salt(salt)
    try:
        the_file = Cryptography(password=password,salt=salt,file=file).file_decrypt()
    except Exception as e:
        raise e
    else:
        location = os.path.join(base_dir,'decrypted',the_file)
        print(f"Decrypted File Location: {location}")
        if cmd:
            exit()
        else:
            userinput = input("Would You Like To Go To Main Menu Or Exit(Y or N) ?")
            if userinput.lower() == 'y':
                banner()
            elif userinput.lower() == 'n':
                exit()
            else:
                print('Wrong Input!')
                sleep(5)
                banner()

# decrypt hash to text
def text_decrypt(hash = None,password=None,salt=None,cmd=False):
    if hash is None:
        hash = input("Enter Hash To Decrypt=>> ")
    if password is None:
        password = input("Enter The Password=>> ")
    if salt is None:
        salt = input("Enter The Salt=>> ")
    # encode the salt in bytes
    salt = Decoders().make_decode_salt(salt)
    try:
        decrypt_val = Cryptography(password=password,text=hash,salt=salt).text_decrypt()
    except Exception as e:
        raise e
    else:
        print(f"The Encrypted Message Is: {decrypt_val}")
        userinput = input("Would You Like To Save The Message In A File(Y or N) ?")
        if userinput.lower() == 'y':
            location = os.path.join(base_dir,'info','text_decrypt_data.txt')
            f = open(location,"w")
            f.write(f"Message: {decrypt_val}")
            f.close()
            print(f"Data Available In {location}")
            if cmd:
                exit()
            else:
                sleep(5)
                banner()
        elif userinput.lower() == 'n':
            if cmd:
                exit()
            else:
                banner()
        else:
            print('Wrong Input!')
            if cmd:
                exit()
            else:
                sleep(5)
                banner()

# section cryptography ends


# section steganography
# hide file in an image
def file_hide(file=None,image=None,cmd=False):
    if file is None:
        file = input("Enter File Location=> ")
    if image is None:
        image = input("Enter Image Location(JPG/JPEG/PNG)=> ")

    loc = Stegano(file=file,image=image).file_hide()

    print(f"File Location: {loc}")
    if cmd:
        exit()
    else:
        userinput = input("Would You Like To Go To Main Menu(Y or N) ?")
        if userinput.lower() == 'y':
            banner()
        elif userinput.lower() == 'n':
            exit()
        else:
            print('Wrong Input!')
            sleep(5)
            banner()   

# hide text in image
def text_hide(text=None,image=None,cmd=False):
    if text is None:
        text = input("Enter Yout Text=> ")
    if image is None:
        image = input("Enter Image Location(JPG/JPEG/PNG)=> ")

    loc = Stegano(text=text,image=image).text_hide()

    print(f"File Location: {loc}")

    if cmd:
        exit()
    else:
        userinput = input("Would You Like To Go To Main Menu(Y or N) ?")
        if userinput.lower() == 'y':
            banner()
        elif userinput.lower() == 'n':
            exit()
        else:
            print('Wrong Input!')
            sleep(5)
            banner()   

# reveal file from image
def file_reavel(image=None,cmd=False):
    if image is None:
        image = input("Enter Image Location(JPG/JPEG/PNG)=> ")

    loc = Stegano(image=image).file_reveal().decode('utf-8')

    file_name = loc.split(":")[-1]
    data = loc.split(f":{file_name}")[0]

    location = os.path.join(base_dir,"reaveled",file_name)

    try:
        with open(location,'w') as f:
            f.write(data)
        f.close()
    except Exception as e:
        raise e
    else:
        print(f"File Is At {location}")
        if cmd:
            exit()
        else:
            userinput = input("Would You Like To Go To Main Menu(Y or N) ?")
            if userinput.lower() == 'y':
                banner()
            elif userinput.lower() == 'n':
                exit()
            else:
                print('Wrong Input!')
                sleep(5)
                banner()   

# reveal text from image
def text_reavel(image=None,cmd=False):
    if image is None:
        image = input("Enter Image Location(JPG/JPEG/PNG)=> ")

    msg = Stegano(image=image).text_reveal()

    print(f"You Hidden Message Id: {msg}")

    userinput = input("Would You Like To Save The Message(Y or N) ?")
    if userinput.lower() == 'y':
        paths = os.path.join(base_dir,'info',"msg_reavel.txt")
        with open(paths,"w") as f:
            f.write(msg)
        f.close()
        print(f"File Saved In {paths}")
        if cmd:
            exit()
        else:
            sleep(5)
            banner()
    elif userinput.lower() == 'n':
        if cmd:
            exit()
        else:
            banner()
    else:
        print('Wrong Input!')
        if cmd:
            exit()
        else:
            sleep(5)
            banner() 

# section steganography ends


# different banners
# banner for encryption options
def encrypt():
    clear_screen()
    print("  Encrypt")
    print("  1. File")
    print("  2. Text")
    print("  3. Back")
    userinput = input("Choose:>> ")
    if userinput == '1':
        file_encrypt()
    elif userinput == '2':
        text_encrypt()
    elif userinput == '3':
        crypto_banner()
    else:
        print("wrong input")

# banner for decryption options
def decrypt():
    clear_screen()
    print("  Decrypt")
    print("  1. File")
    print("  2. Text")
    print("  3. Back")
    userinput = input("Choose:>> ")
    if userinput == '1':
        file_decrypt()
    elif userinput == '2':
        text_decrypt()
    elif userinput == '3':
        crypto_banner()
    else:
        print("wrong input")

# banner for hiding items
def hide():
    clear_screen()
    print("  Hide")
    print("  1. File")
    print("  2. Text")
    print("  3. Back")
    userinput = input("Choose:>> ")
    if userinput == '1':
        file_hide()
    elif userinput == '2':
        text_hide()
    elif userinput == '3':
        stegano_banner()
    else:
        print("wrong input")

# banner for reaveling items
def reavel():
    clear_screen()
    print("  Reavel")
    print("  1. File")
    print("  2. Text")
    print("  3. Back")
    userinput = input("Choose:>> ")
    if userinput == '1':
        file_reavel()
    elif userinput == '2':
        text_reavel()
    elif userinput == '3':
        stegano_banner()
    else:
        print("wrong input")

# banner for cryptography
def crypto_banner():
    clear_screen()
    print("  Cryptography")
    print("  1. Encrypt")
    print("  2. Decrypt")
    print("  3. Back")
    userinput = input("Choose:>> ")
    if userinput == '1':
        encrypt()
    elif userinput == '2':
        decrypt()
    elif userinput == '3':
        banner()
    else:
        print("wrong input")

# banner for steganography
def stegano_banner():
    clear_screen()
    print("  Steganography")
    print("  1. Hide")
    print("  2. Reavel")
    print("  3. Back")
    userinput = input("Choose:>> ")
    if userinput == '1':
        hide()
    elif userinput == '2':
        reavel()
    elif userinput == '3':
        banner()
    else:
        print("wrong input")

# main menu banner
def banner():
    clear_screen()
    # print the banner with options
    print("  The Hidden One")
    print("  1. Cryptography")
    print("  2. Steganography")
    print("  3. AES Encryption")
    print("  4. AES Decryption")
    print("  5. Clean")
    print("  6. Exit")
    userinput = input("Choose:>> ")
    if userinput == '1':
        crypto_banner()
    elif userinput == '2':
        stegano_banner()
    elif userinput == "3":
        aes_encryption()
    elif userinput == "5":
        clean_folders()
    elif userinput == "4":
        aes_decryption()
    elif userinput == "6":
        exit()
    else:
        print("wrong input")
# different banners end

# clear console screen depending on os 
def clear_screen():
    if "windows" in check_platform().lower():
        os.system("cls")
    else:
        os.system("clear")

# cehck which platform we are using
def check_platform():
    plt = platform.platform()
    return plt

# remove all files in all folders of this project
def clean_folders(cmd=False):
    encrypted = os.path.join(base_dir,'encrypted')
    decrypted = os.path.join(base_dir,'decrypted')
    info = os.path.join(base_dir,'info')
    hidden = os.path.join(base_dir,'hidden')
    reaveled = os.path.join(base_dir,'reaveled')

    for f in os.listdir(reaveled):
        os.remove(os.path.join(reaveled, f))
 
    for f in os.listdir(encrypted):
        os.remove(os.path.join(encrypted, f))

    for f in os.listdir(decrypted):
        os.remove(os.path.join(decrypted, f))


    for f in os.listdir(info):
        os.remove(os.path.join(info, f))

    for f in os.listdir(hidden):
        os.remove(os.path.join(hidden, f))

    if cmd:
        exit()
    else:
        banner()

# run this script this file is called directly 
if __name__ == "__main__":
    handel_arguments(arguments=arguments)