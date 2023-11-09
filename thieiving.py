import time

import pyautogui
import random

from functions import drop_item, release_drop_item
from utils.common_functions import random_plus_minus_100
from utils.timestamped_print import enable_timestamped_print


def click_on_coordinates(center_x, center_y, drag = random.uniform(0.38, 0.46)):
    """
    Moves the mouse to the given coordinates on the screen and performs a click.

    :param x: The x-coordinate on the screen where to click.
    :param y: The y-coordinate on the screen where to click.
    :param duration: The time taken to move the mouse to the coordinates before clicking.
    """
    # Generate random offsets within ±5 pixels
    offset_x = random.randint(-7, 8)
    offset_y = random.randint(-6, 9)
    # Apply the random offsets to the center coordinates
    click_x, click_y = center_x + offset_x, center_y + offset_y

    pyautogui.moveTo(click_x, click_y, duration=drag)
    pyautogui.click()


def drop_first_item():
    drop_item()
    drag = random.uniform(0.63, 0.76)
    click_on_coordinates(584, 252, drag=drag)
    release_drop_item()


def fruit_stalls():
    x_coord = 450  # Replace with your desired x-coordinate
    y_coord = 230  # Replace with your desired y-coordinate
    # delay = .96
    click_on_coordinates(x_coord, y_coord)
    drop_first_item()

    delay = random.uniform(0.81, 1.52)
    time.sleep(delay)


# Example usage:
if __name__ == "__main__":
    enable_timestamped_print()
    loops = random_plus_minus_100(4000)
    count = 0
    # start a timer
    timer = time.time()
    randomFloor = 23
    randomCeil = 52

    random_break = random.randint(randomFloor, randomCeil)
    print(f'will break after {random_break} fruit stalls')

    while count <= loops:
        fruit_stalls()
        count += 1
        print(f"Completed {count} fruit stalls in {round((time.time() - timer) / 60, 2)} minutes")
        # after a random number between 100 and 200 stalls, take a 2-3 minute break
        if count % random_break == 0:
            small_break = random.randint(3, 11)
            print(f"Taking a {small_break} second break after {count} fruit stalls.")
            time.sleep(small_break)
            print("Break over. Back to fruit stalls.")

            random_break = random.randint(randomFloor, randomCeil)
            print(f'New break time after {random_break + count} fruit stalls')

