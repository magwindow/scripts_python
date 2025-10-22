import time

import mouse
import keyboard
from win11toast import toast

isClicking= False

def on_click():
    global isClicking
    if isClicking:
        isClicking = False
        toast('Clicker off')
    else:
        isClicking = True
        toast('Clicker on')

keyboard.add_hotkey('Alt + Z', on_click)

while True:
    if isClicking:
        mouse.double_click(button='left')
    time.sleep(0.01)