import math
import time

import cv2
import numpy as np
import pyautogui
from PIL import Image, ImageGrab
from shapely import Polygon
import random

from firemaking import screen_grab

imageDirectory = 'images/screenshot.png'

image_ranges = {
    #       left, up, right, bottom
    'default': (0, 0, 0, 0),
    'left-half': (0, 0, 1282, 1370),
    # this assumes the screen is on the 2nd half of the window
    'canifis-start-jump': (558, 0, 1000, 1200),
    'canifis-first-jump': (800, 400, 1250, 900),
    'canifis-second-jump': (400, 400, 1000, 841),
    'canifis-third-jump': (250, 850, 1000, 1200),
    'canifis-fourth-jump': (0, 0, 950, 1200),
    'canifis-fifth-jump': (200, 500, 1250, 1250),
    'canifis-sixth-jump': (255, 255, 1840, 1100),
    'canifis-final-jump': (0, 0, 768, 1100),
    # nightmare zone
    'absorption-pot': (0, 0, 76, 74)
}


def screen_Image(screenSize, name='screenshot.png'):
    if screenSize not in image_ranges:
        raise ValueError(f"{screenSize} is not within the range")
    myScreenshot = ImageGrab.grab() if screenSize == 'default' else ImageGrab.grab(bbox=image_ranges[screenSize])
    myScreenshot.save('images/' + name)


# Define your color ranges in a dictionary
color_ranges = {
    'red': ([0, 0, 180], [80, 80, 255]),
    'green': ([0, 180, 0], [80, 255, 80]),
    'amber': ([0, 200, 200], [60, 255, 255]),
    'pickup_high': ([250, 0, 167], [255, 5, 172]),
    'attack_blue': ([200, 200, 0], [255, 255, 5]),
    'agility': ([25, 75, 14], [40, 85, 35]),
    'canfis-small-north-house': ([30, 100, 30], [80, 255, 80]),
}


def find_object_precise_new(color_name, screenSize='default'):
    # Check if the color_name is one of the predefined colors
    if color_name not in color_ranges:
        raise ValueError(f"{color_name} is not a valid color name")

    # If the color_name is valid, get the color ranges
    color = color_ranges[color_name]

    screen_Image(screenSize)
    image = cv2.imread(imageDirectory)
    image = cv2.rectangle(image, pt1=(600, 0), pt2=(850, 200), color=(0, 0, 0), thickness=-1)
    image = cv2.rectangle(image, pt1=(0, 0), pt2=(150, 100), color=(0, 0, 0), thickness=-1)
    boundaries = [color]

    print(f"Searching for {color_name}...")

    # loop over the boundaries
    for (lower, upper) in boundaries:
        # create NumPy arrays from the boundaries
        lower = np.array(lower, dtype="uint8")
        upper = np.array(upper, dtype="uint8")
        # find the colors within the specified boundaries and apply
        # the mask
        mask = cv2.inRange(image, lower, upper)
        result = cv2.bitwise_and(image, image, mask=mask)

        # debug Display the result
        cv2.imshow('mask', mask)
        cv2.imshow('result', result)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        ret, thresh = cv2.threshold(mask, 40, 255, 0)
        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    if len(contours) == 0:
        raise ValueError(f"No matches found for {color_name}")

    # find the biggest countour (c) by the area
    c = max(contours, key=cv2.contourArea)

    x_delta_from_screenshot = image_ranges[screenSize][0]
    y_delta_from_screenshot = image_ranges[screenSize][1]

    minx, miny, maxx, maxy = Polygon(np.squeeze(c)).bounds
    print('-----------')
    print(f'Found {color_name} at: minx: {minx+x_delta_from_screenshot}, miny: {miny+y_delta_from_screenshot}, maxx: {maxx+x_delta_from_screenshot}, maxy: {maxy+y_delta_from_screenshot}')


    x,y = choose_random_median_point(minx, miny, maxx, maxy, x_delta_from_screenshot, y_delta_from_screenshot)

    print(f'clicking at: {x}, {y}')
    print('-----------')

    drag = random.uniform(0.1, 0.4)
    pyautogui.moveTo(x, y, duration=drag)
    drag = random.uniform(0.01, 0.05)
    # just to make sure the mouse has enough time to get there
    time.sleep(drag)
    pyautogui.click(x, y, duration=drag)
    return x, y

def choose_random_median_point(minx, miny, maxx, maxy, delta_x=0, delta_y=0):
    # Calculate median points
    median_x = int((minx + maxx) / 2)
    median_y = int((miny + maxy) / 2)

    # Define the pixel boundary for x and y, only deviating 50% of the max pixels
    pixel_boundary_x = int((maxx - minx) * .25)
    pixel_boundary_y = int((maxy - miny) * .25)

    random_x = random.randrange(median_x - pixel_boundary_x, median_x + pixel_boundary_x)
    random_y = random.randrange(median_y - pixel_boundary_y, median_y + pixel_boundary_y)

    final_x = random_x + delta_x
    final_y = random_y + delta_y

    return final_x, final_y


def random_plus_minus_100(base_number):
    # Generate a random number between -10 and 10, then add it to the base number
    random_offset = np.random.uniform(-100, 100)
    number_with_offset = base_number + random_offset
    rounded_val = math.ceil(number_with_offset)
    return rounded_val


def click_random(x, y):
    drag = random.uniform(0.33, 0.46)
    x = random.randrange(x, x + 11) + 5
    y = random.randrange(y, y + 16) + 5
    pyautogui.moveTo(x, y, duration=drag)
    pyautogui.click()


def is_at_login_screen():
    is_match = screen_grab('login_screen.png')
    print(f'is_match: {is_match}')
    return is_match


def click_on_match(image, threshold=0.7):
    loc, w, h = screen_grab(image, threshold)
    points = list(zip(*loc[::-1]))
    if len(points) >= 2:  # Check if there are at least two matches
        # Access the second match directly
        second_match_point = points[1]
        # Calculate the center of the matched region
        center_x, center_y = second_match_point[0] + w // 2, second_match_point[1] + h // 2
        # Generate random offsets within ±10 pixels
        offset_x = random.randint(-10, 10)
        offset_y = random.randint(-10, 10)
        # Apply the random offsets to the center coordinates
        click_x, click_y = center_x + offset_x, center_y + offset_y
        drag = random.uniform(.1, .3)

        pyautogui.moveTo(click_x, click_y, duration=drag)
        pyautogui.click(click_x, click_y)
        print(f"Clicked at a random position near the center: {click_x}, {click_y}")
        return True
    else:
        print("No matches found to click on.")
        return False
