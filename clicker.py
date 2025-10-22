import time
import mouse
import keyboard

isClicking= False

def on_click():
    global isClicking
    if isClicking:
        isClicking = False
        print('Clicker off')
    else:
        isClicking = True
        print('Clicker on')

keyboard.add_hotkey('Alt + Z', on_click)

while True:
    if isClicking:
        mouse.double_click(button='left')
    time.sleep(0.01)