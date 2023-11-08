import math
import random
import time

import numpy as np
import pyautogui
import win32gui
import core
import yaml
from functions import pick_item
from functions import random_combat
from functions import random_quests
from functions import random_skills
from functions import random_inventory
from functions import random_breaks

from functions import find_Object
from functions import exit_bank
from functions import Image_Rec_single
from functions import deposit_secondItem

import functions
from utils.common_functions import random_plus_minus_100

global hwnd
global iflag
global icoord
iflag = False
global newTime_break
newTime_break = False
global timer
global timer_break
global ibreak

pyautogui.FAILSAFE = False
def gfindWindow(data):  # find window name returns PID of the window
    global hwnd
    hwnd = win32gui.FindWindow(None, data)
    # hwnd = win32gui.GetForegroundWindow()860
    #print('findWindow:', hwnd)
    win32gui.SetActiveWindow(hwnd)
    # win32gui.ShowWindow(hwnd)
    win32gui.MoveWindow(hwnd, 0, 0, 865, 830, True)


with open("pybot-config.yaml", "r") as yamlfile:
    data = yaml.load(yamlfile, Loader=yaml.FullLoader)

try:
    gfindWindow(data[0]['Config']['client_title'])
except BaseException:
    print("Unable to find window:", data[0]['Config']['client_title'], "| Please see list of window names below:")
    core.printWindows()
    pass

try:
    x_win, y_win, w_win, h_win = core.getWindow(data[0]['Config']['client_title'])
except BaseException:
    print("Unable to find window:", data[0]['Config']['client_title'], "| Please see list of window names below:")
    core.printWindows()
    pass

def random_break(start, c):
    global newTime_break
    startTime = time.time()
    # 1200 = 20 minutes
    a = random.randrange(0, 4)
    if startTime - start > c:
        options[a]()
        newTime_break = True


def randomizer(timer_breaks, ibreaks):
    global newTime_break
    global timer_break
    global ibreak
    random_break(timer_breaks, ibreaks)
    if newTime_break == True:
        timer_break = timer()
        ibreak = random.randrange(600, 2000)
        newTime_break = False

    # b = random.uniform(4, 5)


def timer():
    startTime = time.time()
    return startTime


def random_pause():
    b = random.uniform(20, 250)
    print('pausing for ' + str(b) + ' seconds')
    time.sleep(b)
    newTime_break = True


iflag = False

options = {0: random_inventory,
           1: random_combat,
           2: random_skills,
           3: random_quests,
           4: random_pause}

def high_alch_third_spot():
    # 3rd item
    b = random.uniform(0.33, 0.46)
    c = random.uniform(1, 1.5)
    x = random.randrange(730, 750)
    print('x: ', x)
    y = random.randrange(490, 515) + 5
    print('y: ', y)
    d = random.uniform(0.11, 0.18)
    pyautogui.moveTo(x, y, duration=b)
    time.sleep(d)
    pyautogui.click()

    print('alching item')





import time

def takeRandomBreak():
    timeInSeconds = time.time()
    # Convert the number to a string
    num_str = str(timeInSeconds)

    # Extract the last two characters
    last_two_chars = num_str[-2:]
    print(f'taking break: {timeInSeconds}')
    # Check if the last two characters are between '00' and '15'
    return '00' <= last_two_chars <= '15'

def pick_iron_items():
    pick_item(1510 - 1280, 123)
    random_breaks(0.5, 1.5)


def pick_bronze_items():
    pick_item(1560 - 1280, 123)
    random_breaks(0.5, 1.5)
    pick_item(1607 - 1280, 123)
    random_breaks(0.1, 0.5)


def bank_spot_varrock():
    find_Object(2)  # amber


def cast_superheat():
    pick_item(2029 - 1280, 573)


def pick_ore(type):
    Image_Rec_single(type, 'pick ores', 5, 5, 0.8, 'left', 20, 620, 480, False)


def superheat_items(num, bar):
    vol = [13, 27]
    j = round(num / vol[bar])
    pick_options = {0: pick_bronze_items,
                    1: pick_iron_items}
    orelist = ['copper.png', 'iron_ore.png']
    while j > 0:
        bank_spot_varrock()
        random_breaks(0.3, 0.5)
        deposit_secondItem()
        random_breaks(0.3, 0.5)
        pick_options[bar]()
        exit_bank()
        random_breaks(0.05, 0.2)
        inv = 27
        while inv != 0:
            cast_superheat()
            random_breaks(0.2, 0.4)
            pick_ore(orelist[bar])
            random_breaks(0.1, 0.2)
            inv -= 1
            print(inv)
        j -= 1
        random_breaks(0.4, 0.8)


randXStart = 710
randXStop = randXStart + 5 # 9
randYStart = 328
randYStop = randYStart + 9 # 10
def high_alch_command():
    # 3rd item
    b = random.uniform(0.33, 0.46)
    x = random.randrange(randXStart, randXStop) + 5
    y = random.randrange(randYStart, randYStop) + 5
    d = random.uniform(0.11, 0.18)
    pyautogui.moveTo(x, y, duration=b)
    time.sleep(d)
    pyautogui.click()

from datetime import datetime

def high_alch_loop(vol, bool):
    print(f'alching {vol} times')
    t = 1
    exp = bool
    while t <= vol:
        now = datetime.now()
        # takeRandomBreak()
        print(f'{now}: Alch {t}/{vol}')
        high_alch_command()
        # time.sleep(delay)
        high_alch_command()  # alchs same spot as alch spell location
        #high_alch() alchs 3rd inventory spot
        delay = random.uniform(1.4, 1.9)
        if exp:
            print('expensive')
            expensive_delay = random.uniform(0.8, 1.2)
            time.sleep(expensive_delay)
            expensive_delay = random.uniform(0.8, 1.2)
            pyautogui.press('space')
            time.sleep(expensive_delay)
            pyautogui.press('1')
            expensive_delay = random.uniform(0.5, 0.6)
            time.sleep(expensive_delay)
        time.sleep(delay)
        t += 1


if __name__ == "__main__":
    loops = random_plus_minus_100(3100)
    # loops = 2126
    high_alch_loop(loops, False)
    # superheat_items(100, 1) #100 items iron
