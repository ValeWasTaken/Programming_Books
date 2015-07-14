# Automate the Boring Stuff - Ch. 18 Practice Project: Looking Busy
# Python 2.7
# Move the mouse cursor very slightly every 10 seconds to avoid idle status.

import pyautogui
import time
import random

def anti_idle():
    while True:
        mouse_position = pyautogui.position()
        random_x = random.randint(-1,1)
        random_y = random.randint(-1,1)
        time.sleep(10)
        if pyautogui.position() == mouse_position:
            pyautogui.moveRel(random_x, random_y)
anti_idle()
