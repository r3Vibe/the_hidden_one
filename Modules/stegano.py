from stegano import lsbset
from stegano.lsbset import generators
from stegano import exifHeader
import platform,os
from pathlib import Path
from .encryption import Cryptography

base_dir  = Path(__file__).resolve().parent.parent


def get_file_name(file):
    if "windows" in platform.platform().lower():
        return file.split("\\")[-1]
    else:
        return file.split("/")[-1]

def get_image_ext(img):
    if "windows" in platform.platform().lower():
        return img.split("\\")[-1].split(".")[-1]
    else:
        return img.split("/")[-1].split(".")[-1] 


class Stegano():
    def __init__(self,text=None,file=None,image=None):
        if image is not None:
            self.image = image
        if file is not None:
            self.file = file
        if text is not None:
            self.text = text

    def file_hide(self):
        # file name only
        the_file = get_file_name(self.file)
        # image extension only
        the_img = get_image_ext(self.image)
        #full image name
        img_name = get_file_name(self.image)

        try:
            with open(self.file,'rb') as fb:
                data = fb.read()
        except Exception as e:
            raise e
        else:
            data = data + ":".encode('utf-8') + the_file.encode('utf-8')
            if the_img.lower() == "png":
                try:
                    hideme = lsbset.hide(self.image,data,generators.eratosthenes())               
                except Exception as e:
                    raise e
                else:
                    hideme.save(os.path.join(base_dir,'hidden',img_name))
                    return os.path.join(base_dir,'hidden',img_name)

            elif the_img.lower() == "jpg" or the_img.lower() == "jpeg":
                try:
                    exifHeader.hide(self.image,os.path.join(base_dir,'hidden',img_name),data)
                except Exception as e:
                    raise e
                else:
                    os.remove(self.file)
                    return os.path.join(base_dir,'hidden',img_name)
    
    def text_hide(self):
        # image extension only
        the_img = get_image_ext(self.image)
        #full image name
        img_name = get_file_name(self.image)

        if the_img.lower() == "png":
            try:
                hideme = lsbset.hide(self.image,self.text,generators.eratosthenes())               
            except Exception as e:
                raise e
            else:
                hideme.save(os.path.join(base_dir,'hidden',img_name))
                return os.path.join(base_dir,'hidden',img_name)
        elif the_img.lower() == "jpg" or the_img.lower() == "jpeg":
            try:
                exifHeader.hide(self.image,os.path.join(base_dir,'hidden',img_name),self.text)
            except Exception as e:
                raise e
            else:
                return os.path.join(base_dir,'hidden',img_name)    
    
    def text_reveal(self):
        # image extension only
        the_img = get_image_ext(self.image)
        #full image name
        img_name = get_file_name(self.image)

        if the_img.lower() == "png":
            try:
                msg = lsbset.reveal(self.image,generators.fibonacci())     
            except Exception as e:
                raise e
            else:
                return msg
        elif the_img.lower() == "jpg" or the_img.lower() == "jpeg":
            try:
                msg = exifHeader.reveal(self.image)
            except Exception as e:
                raise e
            else:
                return msg.decode('utf-8')  

    def file_reveal(self):
        # image extension only
        the_img = get_image_ext(self.image)
        #full image name
        img_name = get_file_name(self.image)
            
        if the_img.lower() == "png":
            try:
                hideme = lsbset.reveal(self.image,generators.fibonacci())           
            except Exception as e:
                raise e
            else:
                return hideme

        elif the_img.lower() == "jpg" or the_img.lower() == "jpeg":
            try:
                hideme = exifHeader.reveal(self.image)
            except Exception as e:
                raise e
            else:
                return hideme