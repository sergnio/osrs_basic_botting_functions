import datetime
import win32gui
from threading import Thread
import core
import yaml
from functions import Image_count, invent_enabled
from functions import image_Rec_clicker
from functions import screen_Image
from functions import release_drop_item
from functions import drop_item
from functions import Image_to_Text
from functions import invent_crop
from functions import resizeImage
from PIL import ImageGrab

from functions import random_combat
from functions import random_quests
from functions import random_skills
from functions import random_inventory
from functions import random_breaks

import numpy as np
import cv2
import time
import random
import pyautogui

global hwnd
global iflag
global icoord
iflag = False
global newTime_break
newTime_break = False
global timer
global timer_break
global ibreak
import slyautomation_title


def click_random(x, y):
    b = random.uniform(0.33, 0.46)
    x = random.randrange(x, x + 11) + 5
    y = random.randrange(y, y + 16) + 5
    d = random.uniform(1.89, 2.97)
    pyautogui.moveTo(x, y, duration=b)
    time.sleep(d)
    pyautogui.click()


def click_western():
    click_random(330, 284)


def click_southern():
    click_random(385, 342)


def click_eastern():
    click_random(433, 286)


def drop_all():
    random_breaks(1.04, 2.15)
    invent_crop()
    drop_item()
    image_Rec_clicker(r'iron_ore.png', 'dropping item', threshold=0.8)
    release_drop_item()

from datetime import datetime

def powermine(times):
    now = datetime.now()
    count = 1
    while count <= times:
        print(f'{now} Mining: {count}/{times}')
        click_western()
        click_southern()
        click_eastern()
        drop_all()
        count += 1


if __name__ == "__main__":
    powermine(3073)
