# from pynput.keyboard import Listener
# from pynput import keyboard
# import os

# # def some(e):
    
# #     print("Well Well You have accessed another function...")
# # def go_quit():
# #     os.system("exit")

# # def test(key):
# #     if key == keyboard.KeyCode(char='q'):
# #         go_quit()
# #         return False
# #     elif key == keyboard.KeyCode(char='e'):
# # #         some('e')
# # #         return False
# # #     else:
# # #         print(key)
# # # with Listener(on_release=test) as l:
# # #     l.join()


# # dire = os.getcwd()

# # print(dire+"/test/jojlo/")


# while True:
#     if msvcrt.kbhit():
#         key = msvcrt.getch()
#         print(key)

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

file = "./Hidden/file.png"
msg = lsbset.reveal(file,generators.eratosthenes())
message = msg.decode()
msg = exifHeader.reveal("./Hidden/file.jpg")
msg = msg.decode()

#with open("tmp",'w') as f:
#    f.write(message)
#get the file
with open("tmp","r") as r:
    lines = r.read()
    lines = lines.encode().decode()
    lines = lines.splitlines()
    content = lines[:-1]
    lines = lines[-1]
    for x in content:
        print(x)
        # with open(lines,'a') as f:
        #     f.write("%s\n"%x)