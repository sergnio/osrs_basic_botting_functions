import time

import pyautogui
import random

def click_on_coordinates(center_x, center_y, duration=0.1):
    """
    Moves the mouse to the given coordinates on the screen and performs a click.

    :param x: The x-coordinate on the screen where to click.
    :param y: The y-coordinate on the screen where to click.
    :param duration: The time taken to move the mouse to the coordinates before clicking.
    """
    # Generate random offsets within ±5 pixels
    offset_x = random.randint(-5, 5)
    offset_y = random.randint(-5, 5)
    # Apply the random offsets to the center coordinates
    click_x, click_y = center_x + offset_x, center_y + offset_y

    drag = random.uniform(0.33, 0.46)
    delay = random.uniform(3.14, 3.89)
    pyautogui.moveTo(click_x, click_y, duration=drag)
    pyautogui.click()
    time.sleep(delay)


def fruit_stalls():
    x_coord = 340  # Replace with your desired x-coordinate
    y_coord = 200  # Replace with your desired y-coordinate
    click_on_coordinates(x_coord, y_coord)


# Example usage:
if __name__ == "__main__":
   while 1:
       fruit_stalls()
