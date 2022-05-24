import pyAesCrypt,os
from .encryption import split_f,base_dir

bufferSize = 64 * 2048

class EncryptFile:
    def __init__(self,file,password):
        self.file = file
        self.password = password

    def encrypt_now(self):
        file_name = split_f(self.file,"slash")[-1]
        try:
            pyAesCrypt.encryptFile(self.file,os.path.join(base_dir,"encrypted",f"{file_name}.aes"),passw=self.password,bufferSize=bufferSize)
        except Exception as e:
            raise e
        else:
            os.remove(self.file)
            return f"{file_name}.aes"
    
    def decrypt_now(self):
        file_name = split_f(self.file,"slash")[-1]
        file_name = file_name.split(".aes")[0]
        try:
            pyAesCrypt.decryptFile(self.file,os.path.join(base_dir,"decrypted",f"{file_name}"),passw=self.password,bufferSize=bufferSize)
        except Exception as e:
            raise e
        else:
            os.remove(self.file)
            return f"{file_name}"
