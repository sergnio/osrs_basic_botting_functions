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
ispace = 14


def firemake():
    threshold = 0.7
    clicker = 'left'
    playarea = True
    fast = False
    # image = 'willow_icon.png'
    image = 'maple_log_icon.png'
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

    click_tinderbox()
    # Assuming loc is a tuple of arrays and all arrays have the same length
    loc_list = list(zip(*loc[::-1]))
    for index, pt in enumerate(loc_list):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
        print(f"Match found at: {pt}")

        x = random.randrange(iwidth, iwidth + ispace)
        y = random.randrange(iheight, iheight + ispace)
        icoord = (pt[0] + iheight + x, pt[1] + iwidth + y)

        print(f"Clicking at coordinates: {icoord}")

        drag = random.uniform(0.16, 0.27)
        pyautogui.moveTo(icoord, duration=drag)
        pyautogui.click(icoord, duration=drag, button=clicker)
        fire_made = False
        # only click tinderbox if not last match
        if index != len(loc_list) - 1:
            click_tinderbox()

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
    run_to_firemake_spot()

def run_to_firemake_spot():
    click_minimap_towards_spot()


def click_minimap_towards_spot():
    image = 'firemake_start.png'
    h, img_rgb, loc, w = screen_grab(image, full_color=True)
    # click on the first match
    x = random.randrange(iwidth, iwidth + ispace)
    y = random.randrange(iheight, iheight + ispace)
    icoord = (loc[1] + iheight + x, loc[0] + iwidth + y)
    print(f"Clicking at coordinates: {icoord}")
    drag = random.uniform(0.16, 0.27)
    pyautogui.moveTo(icoord, duration=drag)
    pyautogui.click(icoord, duration=drag, button='left')

    time.sleep(7)


def screen_grab(image, threshold=0.7, left=0, top=0, right=810, bottom=533, full_color=False):
    screen_Image(left, top, right, bottom)

    img_rgb = cv2.imread('images/screenshot.png')

    # Depending on full_color, decide whether to use grayscale or color images for matching.
    if full_color:
        img_to_match = img_rgb
        template = cv2.imread(f'images/{image}')
    else:
        img_to_match = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
        template = cv2.imread(f'images/{image}', 0)

    w, h = template.shape[:2][::-1]
    print(f"Template size: width={w}, height={h}")

    # Choose the correct method for template matching based on whether it's full color or not.
    method = cv2.TM_CCOEFF_NORMED
    res = cv2.matchTemplate(img_to_match, template, method)

    print(f"Matching template...")
    loc = np.where(res >= threshold)
    return h, img_rgb, loc, w


def grab_more_logs():
    # image = 'willow_log_bank.png'
    image = 'maple_log_bank.png'
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
    firemake()
    # run_to_firemake_spot()
