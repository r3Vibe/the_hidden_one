# required imports
import base64,os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import platform
from pathlib import Path

base_dir = Path(__file__).resolve().parent.parent

# split to get file name depending on os
def split_f(file,param):
    if "windows" in check_platform().lower():
        if param.lower() == 'dot':
            return file.split(".")
        elif param.lower() == 'slash':
            return file.split("\\")
    elif 'linux' in check_platform().lower():
        if param.lower() == 'dot':
            return file.split(".")
        elif param.lower() == 'slash':
            return file.split("/")

# cehck which platform we are using then return it
def check_platform():
    plt = platform.platform()
    return plt

def get_actual_file(file):
    if "windows" in check_platform().lower():
        file_name = file.split("\\")[-1].split("_encrypted")[0]
    elif 'linux' in check_platform().lower():
        file_name = file.split("/")[-1].split("_encrypted")[0]
    
    return file_name


# entaire cryptography code here
class Cryptography:

    # initialize class with faw required items as password and salt
    def __init__(self,password,salt,file=None,text=None):
        self.password = bytes(password,'utf-8')
        self.salt = salt
        if text != None:
            self.text = bytes(text,'utf-8')
        self.file = file
        
    #genereate key
    def __gen_key(self):
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=self.salt,
            iterations=390000,
        )

        try:
            key = base64.urlsafe_b64encode(kdf.derive(self.password))
        except Exception as e:
            raise e
        else:
            return key

    # encrypting files
    def file_encrypt(self):

        # location of file
        file_loc = self.file

        # file name with extension
        file = split_f(file_loc,'slash')[-1]

        if len(split_f(file,'dot'))  == 1:
            # file name
            file_name = split_f(file,'dot')[0]
            # file extension
            file_ext = ""
            full_name  = f"{file_name}"
        else:
            file_name   = split_f(file,'dot')[0]
            file_ext    = split_f(file,'dot')[1]
            full_name  = f"{file_name}.{file_ext}"
        # open the file and read binary of that file
        try:
            with open(file_loc,'rb') as fb:
                all_lines = fb.read()
        except Exception as e:
            raise e
        else:
            # generate key and cipher
            key = self.__gen_key()
            cipher = Fernet(key=key)
            try:
                # encrypt the file binary
                encrypt_file = cipher.encrypt(all_lines)
            except Exception as e:
                raise e
            else:
                try:
                    # save the hash
                    path_to_save = os.path.join(base_dir,'encrypted',f"{full_name}_encrypted")
                    with open(path_to_save,"wb") as ef:
                        ef.write(encrypt_file)
                except Exception as e:
                    raise e
                else:
                    # remove original file
                    os.remove(file_loc)
                    return f"{full_name}_encrypted"


    def text_encrypt(self):
        # generate key for encryption
        key = self.__gen_key()

        f = Fernet(key)

        #encrypt text and return hash in text form
        try:
            token = f.encrypt(self.text)
        except Exception as e:
            raise e
        else:
            token = token.decode('utf-8')
            return token

    def text_decrypt(self):
        # generate key
        key = self.__gen_key()

        f = Fernet(key)

        # decrypt hash to text and return the text
        try:
            token = f.decrypt(self.text)
        except Exception as e:
            raise e
        else:
            token = token.decode('utf-8')
            return token

    # decrypt files
    def file_decrypt(self):
        # get file location
        file_loc = self.file
        # try to open the encrypted file
        try:
            with open(file_loc,'rb') as ef:
                all_lines = ef.read()
        except Exception as e:
            raise e
        else:
            key = self.__gen_key()

            cipher = Fernet(key)
            try:
                decrypt = cipher.decrypt(all_lines)
            except Exception as e:
                raise e
            else:
                file = get_actual_file(file_loc)
                location = os.path.join(base_dir,"decrypted",file)
                try:
                    with open(location,'w') as af:
                        af.write(decrypt.decode('utf-8'))
                except Exception as e:
                    raise e
                else:
                    os.remove(file_loc)
                    return file
                



class Generators:
    # generate salt for encryption
    def gen_salt(self):
        return os.urandom(16)

class Decoders:
    # decode salt to plain text
    def decode_salt(self,salt):
        return base64.b64encode(salt).decode('utf-8')
    # plain text salt to bytes
    def make_decode_salt(self,salt):
        return base64.b64decode(salt)