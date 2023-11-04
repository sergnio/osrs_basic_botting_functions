from functions import random_breaks
from utils.common_functions import find_object_precise_new

color = 'green'


def start_course():
    find_object_precise_new(color, 'canifis-first-jump')
    random_breaks(6.02, 7.25)


def first_jump():
    find_object_precise_new(color, 'canifis-first-jump')
    random_breaks(5.12, 6.65)


def second_jump():
    find_object_precise_new(color, 'canifis-second-jump')
    random_breaks(5.01, 6.5)


def third_jump():
    find_object_precise_new(color, 'canifis-third-jump')
    random_breaks(6.8, 8.5)


def fourth_jump():
    find_object_precise_new(color, 'canifis-fourth-jump')
    random_breaks(5.19, 6.45)


def fifth_jump():
    find_object_precise_new(color, 'canifis-fifth-jump')
    random_breaks(7.21, 9.15)


def sixth_jump():
    find_object_precise_new(color, 'canifis-sixth-jump')
    random_breaks(7.08, 9.85)


def final_jump():
    find_object_precise_new(color, 'canifis-sixth-jump')
    random_breaks(3.52, 5.56)


# click on the tree
if __name__ == "__main__":
    start_course()
    first_jump()
    second_jump()
    third_jump()
    fourth_jump()
    fifth_jump()
    sixth_jump()
    final_jump()
