import time

import cv2
import numpy as np
import pyautogui
import random

from utils.common_functions import screen_Image

import builtins
import time

from utils.timestamped_print import enable_timestamped_print

# Save the original print function
original_print = builtins.print


# Define a new print function that includes a timestamp
def timestamped_print(*args, **kwargs):
    # Get the current time
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    # Call the original print function with the timestamp
    original_print(f"{current_time} -", *args, **kwargs)


# Override the built-in print with the new function
builtins.print = timestamped_print


def check_absorption_active():
    loc = screen_grab('absorption_pot_icon.png')
    print(f'loc: {loc}')
    # if these exist, it means there's a match
    xCoords = loc[0][0]
    print(f'xCoords: {xCoords}')
    return len(xCoords) > 0


def screen_grab(image, threshold=0.7):
    screen_Image('default', 'screenshot.png')
    img_rgb = cv2.imread('images/screenshot.png')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(f'images/{image}', 0)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= threshold)
    return loc, w, h


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

        # Wait for a random delay between 0.1 to 0.7 seconds
        delay = random.uniform(0.31, 0.64)
        time.sleep(delay)

        # Perform the second click at the same random position
        pyautogui.click(click_x, click_y)

        pyautogui.moveTo(1100, 122, duration=drag)
        print(f"Clicked again after a {delay} second delay at the same position: {click_x}, {click_y}")
        return True
    else:
        print("No matches found to click on.")
        return False


def toggle_prayer():
    # while we have absorption pots
    has_more_absorption = True

    # contiuously toggle rapid prayer, every 45-58 seconds randomly
    while has_more_absorption:
        click_on_match('quick_toggle_prayer.png')
        # delay = random.uniform(14.1, 58.67)
        nextFlickFloorDelay = 7.2
        nextFlickCeilingDelay = 47.8
        # nextFlickFloorDelay = 2.2
        # nextFlickCeilingDelay = 5.8
        delay = random.uniform(nextFlickFloorDelay, nextFlickCeilingDelay)
        # print out delay
        print(f"Delaying {delay} seconds before toggling prayer.")
        time.sleep(delay)
        has_more_absorption = check_absorption_active()


if __name__ == "__main__":
    toggle_prayer()
