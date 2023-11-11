from functions import random_breaks
from utils.common_functions import find_object_precise_new

color = 'agility'


def start_course():
    find_object_precise_new(color, 'canifis-first-jump')
    random_breaks(6.02, 7.25)


def first_jump():
    find_object_precise_new(color, 'canifis-first-jump')
    random_breaks(5.12, 6.65)


def second_jump():
    find_object_precise_new(color, 'canifis-second-jump')
    random_breaks(5.01, 6.5)


def northern_house_jump():
    find_object_precise_new(color, 'canifis-third-jump')
    random_breaks(5.8, 7.5)


def north_western_jump():
    find_object_precise_new(color, 'canifis-fourth-jump')
    random_breaks(5.19, 6.45)


def pole_vault():
    find_object_precise_new(color, 'canifis-fifth-jump')
    random_breaks(7.21, 9.15)


def jump_to_last_house():
    find_object_precise_new(color, 'canifis-sixth-jump')
    random_breaks(7.08, 9.85)


def exit_course_jump():
    find_object_precise_new(color, 'canifis-sixth-jump')
    random_breaks(3.52, 5.56)


def run_course(num_times):
    while num_times > 0:
        start_course()
        first_jump()
        second_jump()
        northern_house_jump()
        north_western_jump()
        pole_vault()
        jump_to_last_house()
        exit_course_jump()
        num_times = num_times - 1

# todo - checking for marks of grace
    # then picking them up
# todo - checking if I fell
    # go to restart point

# click on the tree
if __name__ == "__main__":
    # assume a screensize of 1805x1400
    run_course(1)
