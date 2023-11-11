import pyautogui

from functions import random_breaks
from firemaking import screen_grab
from utils.common_functions import find_object_precise_and_click, click_random, click_on_match

color = 'agility'

def start_course():
    print('Starting course')
    find_object_precise_and_click(color, 'canifis-first-jump')
    random_breaks(6.02, 7.25)


def first_jump():
    print('First jump')
    find_object_precise_and_click(color, 'canifis-first-jump')
    random_breaks(5.12, 6.65)


def small_northern_house():
    print('Small northern house')
    find_object_precise_and_click('amber', 'canifis-second-jump')
    random_breaks(5.01, 6.5)


def northern_L_house_jump():
    print('Northern L house jump')
    find_object_precise_and_click('amber', 'canifis-third-jump')
    random_breaks(5.8, 7.5)


def north_western_jump():
    print('North western jump')
    find_object_precise_and_click(color, 'canifis-fourth-jump')
    random_breaks(5.19, 6.45)


def pole_vault():
    print('Pole vault')
    find_object_precise_and_click('amber', 'canifis-fifth-jump')
    random_breaks(7.21, 9.15)


def jump_to_last_house():
    print('Jump to last house')
    find_object_precise_and_click(color, 'canifis-sixth-jump')
    random_breaks(7.08, 9.85)


def exit_course_jump():
    find_object_precise_and_click(color, 'canifis-sixth-jump')

    real_color = 'canifis-fell-off' if

    print('Exit course jump')
    find_object_precise_and_click(color, 'canifis-sixth-jump')
    random_breaks(3.52, 5.56)


def run_course(num_times):
    while num_times > 0:
        check_before_jumping(start_course)
        check_before_jumping(first_jump)
        check_before_jumping(small_northern_house)
        check_before_jumping(northern_L_house_jump)
        check_before_jumping(north_western_jump)
        check_before_jumping(pole_vault)
        check_before_jumping(jump_to_last_house)
        check_before_jumping(exit_course_jump)
        num_times = num_times - 1


# todo - checking for marks of grace
# then picking them up
# todo - checking if I fell
# go to restart point

# click on the tree
def check_for_grace():
    x, x, x, x, is_match = screen_grab('mark_of_grace.png', 0.8)
    if is_match:
        print('found mark of grace!!')
        return True

    print('no mark of grace found')
    return False
def check_before_jumping(jump_function):
    if check_for_grace():
        print('Clicking on mark of grace')
        click_on_match('mark_of_grace.png')

    jump_function()


if __name__ == "__main__":
    # assume a screensize of 1805x1400
    run_course(1)
    # Found amber at: minx: 603.0, miny: 752.0, maxx: 612.0, maxy: 762.0
    # clicking at: 608, 758
    #     pyautogui.moveTo(608, 758, duration=0.1)
