import cv2
import numpy as np
import pyautogui
import random
import time

import pyautogui

from functions import Image_Rec_single, image_Rec_clicker, screen_Image
from functions import Image_count
from functions import mini_map_image
from functions import random_breaks
from functions import xp_gain_check


def firemake():
    iheight = 5
    iwidth = 5
    threshold = 0.7
    clicker = 'left'
    ispace = 20
    playarea = True
    fast = False
    image = 'willow_icon.png'
    event = 'lighting log'
    # find tinderbox
    global icoord
    global iflag
    wood_burned = 0

    print(f"Function called with image: {image}, event: {event}, threshold: {threshold}")

    if playarea:
        screen_Image(0, 0, 810, 533)
        print("Capturing play area screenshot.")
    else:
        screen_Image(550, 230, 739, 493)
        print("Capturing non-play area screenshot.")

    img_rgb = cv2.imread('images/screenshot.png')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(f'images/{image}', 0)
    w, h = template.shape[::-1]

    print(f"Template size: width={w}, height={h}")

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)

    print(f"Matching template...")
    loc = np.where(res >= threshold)
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
            print('wood burned')

        print('done doing that')


def click_tinderbox():
    firstSlotX = random.randrange(585, 594)
    firstSlotY = random.randrange(253, 259)

    b = random.uniform(0.33, 0.43)
    pyautogui.moveTo(firstSlotX, firstSlotY, duration=b)

    b = random.uniform(0.24, 0.47)
    pyautogui.click(firstSlotX, firstSlotY, duration=b)


def is_fire_made():
    print('checking if fire made')
    fire = False
    while not fire:
        print('checking fire')
        fire = xp_gain_check('firemaking_xp.png', 0.85)
        if fire:
            print('breaking')
            break

if __name__ == "__main__":
    firemake()
