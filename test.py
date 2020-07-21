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
# #         some('e')
# #         return False
# #     else:
# #         print(key)
# # with Listener(on_release=test) as l:
# #     l.join()


# dire = os.getcwd()

# print(dire+"/test/jojlo/")


while True:
    if msvcrt.kbhit():
        key = msvcrt.getch()
        print(key)