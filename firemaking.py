import cv2
import numpy as np
import pyautogui
import random
import time

import pyautogui

from functions import Image_Rec_single, image_Rec_clicker, screen_Image, find_Object_precise
from functions import Image_count
from functions import mini_map_image
from functions import random_breaks
from functions import xp_gain_check

iheight = 5
iwidth = 5
ispace = 20


def firemake():
    threshold = 0.7
    clicker = 'left'
    playarea = True
    fast = False
    image = 'willow_icon.png'
    event = 'lighting log'
    # find tinderbox
    global icoord
    global iflag
    wood_burned = 0

    print(f"Function called with image: {image}, event: {event}, threshold: {threshold}")

    h, img_rgb, loc, w = screen_grab(image, threshold)
    iflag = False

    print(f"Location of matches: {loc}")
    if len(loc[0]) == 0:
        print("No matches found.")

    for pt in zip(*loc[::-1]):
        click_tinderbox()

        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
        print(f"Match found at: {pt}")

        x = random.randrange(iwidth, iwidth + ispace)
        y = random.randrange(iheight, iheight + ispace)
        icoord = pt[0] + iheight + x
        icoord = (icoord, pt[1] + iwidth + y)

        print(f"Clicking at coordinates: {icoord}")

        b = random.uniform(0.36, 0.47)
        pyautogui.moveTo(icoord, duration=b)

        b = random.uniform(0.23, 0.53)
        pyautogui.click(icoord, duration=b, button=clicker)
        fire_made = False

        while not fire_made:
            d = random.uniform(0.59, 0.97)
            time.sleep(d)
            wood_burned += 1
            fire_made = is_fire_made()
            print(f'is fire made: {fire_made}')
            print('wood burned')

    print('done doing that')
    bank()
    grab_more_logs()


def screen_grab(image, threshold=0.7, left=0, top=0, right=810, bottom=533):
    screen_Image(left, top, right, bottom)

    img_rgb = cv2.imread('images/screenshot.png')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(f'images/{image}', 0)
    w, h = template.shape[::-1]
    print(f"Template size: width={w}, height={h}")
    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    print(f"Matching template...")
    loc = np.where(res >= threshold)
    return h, img_rgb, loc, w


def grab_more_logs():
    image = 'willow_log_bank.png'
    h, img_rgb, loc, w = screen_grab(image, right=482, bottom=323)

    print('loc')
    print(loc)

    x = random.randrange(iwidth, iwidth + ispace)
    y = random.randrange(iheight, iheight + ispace)
    finalY = loc[0] + iheight + y
    finalX = loc[1] + iwidth + x
    print(f"Clicking at coordinates: {finalX, finalY}")

    b = random.uniform(0.36, 0.47)
    pyautogui.moveTo(finalX, finalY, duration=b)

    b = random.uniform(0.23, 0.53)
    pyautogui.click(finalX, finalY, duration=b)


def bank():
    print("Going to the Varrock bank spot.")
    find_Object_precise(2)  # amber

    d = random.uniform(1.59, 1.97)
    time.sleep(d)


# needs to be first inv slot
def click_tinderbox():
    firstSlotX = random.randrange(585, 594)
    firstSlotY = random.randrange(253, 259)

    b = random.uniform(0.13, 0.23)
    pyautogui.moveTo(firstSlotX, firstSlotY, duration=b)

    b = random.uniform(0.14, 0.27)
    pyautogui.click(firstSlotX, firstSlotY, duration=b)


def is_fire_made():
    print('checking if fire made')
    fire = False
    while not fire:
        fire = xp_gain_check('firemaking_xp.png', 0.85)
        if fire:
            print('breaking')
            return True


if __name__ == "__main__":
    # firemake()
    grab_more_logs()
