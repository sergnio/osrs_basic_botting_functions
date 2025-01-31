import config_generator
import core

import math
import numpy as np
import cv2
import pyautogui
import random
import time
from shapely.geometry import Polygon
import ctypes
import slyautomation_title
import yaml
from PIL import Image, ImageGrab
import os


import platform
global hwnd
hwnd = 0
global iflag
global icoord
iflag = False
global newTime_break
newTime_break = False
global timer
global timer_break
global ibreak

import pytesseract

with open("pybot-config.yaml", "r") as yamlfile:
    data = yaml.load(yamlfile, Loader=yaml.FullLoader)

class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR

with open("pybot-config.yaml", "r") as yamlfile:
    data = yaml.load(yamlfile, Loader=yaml.FullLoader)

pytesseract.pytesseract.tesseract_cmd = data[0]['Config']['tesseract_path'] + "tesseract"
try:
    im = Image.open("images/tynan_shop.png")
    text = pytesseract.image_to_string(im)
    print(bcolors.OK + "Testing Tesseract is configured: Passed |", text)
except:
    pass
os.environ["TESSDATA_PREFIX"] = data[0]['Config']['tesseract_path'] # + "tessdata"
try:
    im = Image.open("images/tynan_shop.png")
    text = pytesseract.image_to_string(im)
    print(bcolors.OK + "Testing Tesseract is configured: Passed |", text)
except:
    os.environ["TESSDATA_PREFIX"] = data[0]['Config']['tesseract_path'] + "tessdata"
    try:
        im = Image.open("images/tynan_shop.png")
        text = pytesseract.image_to_string(im)
        print(bcolors.OK + "Testing Tesseract is configured: Passed |", text)
    except:
        print(bcolors.FAIL +"Error setting up tesseract: Check the pyconfig.yaml is set up to your tesseract path or is installed correctly, go here and install latest version: " + 'https://digi.bib.uni-mannheim.de/tesseract/?C=M;O=D')

# Constants
gdi32 = ctypes.WinDLL('gdi32.dll')

VERTRES = 10
DESKTOPVERTRES = 117


class DeviceCap:
    VERTRES = 10
    DESKTOPVERTRES = 117


def get_scaling_factor():
    gdi32 = ctypes.WinDLL('gdi32.dll')

    # Get the screen's device context (DC)
    desktop = gdi32.CreateDCW('DISPLAY', None, None, None)

    # Get the logical and physical screen height
    logical_screen_height = gdi32.GetDeviceCaps(desktop, DeviceCap.VERTRES)
    physical_screen_height = gdi32.GetDeviceCaps(desktop, DeviceCap.DESKTOPVERTRES)

    # Calculate the scaling factor
    scaling_factor = physical_screen_height / logical_screen_height

    return scaling_factor


# Usage
scaling_factor = get_scaling_factor()
if scaling_factor == 1.0:
    print(bcolors.OK +"Scaling Factor:", scaling_factor * 100, "%")
else:
    print(bcolors.FAIL +"Scaling Factor: Failed set to 100% | Actual:", scaling_factor * 100, "%")

def get_os_configuration():
    # Get scale and layout information
    user32 = ctypes.windll.user32
    scale_factor = user32.GetDpiForSystem()


    # Get font size information
    scale = 96 / scale_factor
    font_size = user32.SystemParametersInfoW(0x0030, 0, 0, 0) / scale  # SPI_GETNONCLIENTMETRICS



    # Get display resolution information
    width = user32.GetSystemMetrics(0)
    height = user32.GetSystemMetrics(1)

    return scale_factor, font_size, width, height


# Usage
scale_factor, font_size, width, height = get_os_configuration()

desiredWidth = 2560
desiredHeight = 1440
if width == desiredWidth and height == desiredHeight:
    print(bcolors.OK +"Resolution:", width, "x", height)
else:
    print(bcolors.FAIL + f"Resolution not set correctly: Failed set to {desiredWidth} x {desiredHeight} | Actual:", width, "x", height)
try:
    print(bcolors.OK + "tesseract version:", pytesseract.get_tesseract_version())
except SystemExit:
    print(bcolors.FAIL +"tesseract version detailed: not found")

print(bcolors.RESET)
filename = data[0]['Config']['pc_profile']

osrs = data[0]['Config']['file_path_to_client']

live_file = "jagex_cl_oldschool_LIVE.dat"

random_file = "random.dat"
try:
    os.remove(filename + osrs + live_file)
    os.remove(filename + osrs + random_file)
except OSError:
    pass
except FileNotFoundError:
    pass

if platform.system() == 'Linux' or platform.system() == 'Mac':
    filename = filename + osrs + "/jagexcache/oldschool/LIVE/"
else:
    filename = filename + osrs + "\\jagexcache\\oldschool\\LIVE\\"

try:
    for f in os.listdir(filename):
        try:
            if not f.startswith("main_file"):
                continue
            os.remove(os.path.join(filename, f))
        except OSError:
            pass
        except FileNotFoundError:
            pass

except OSError:
    pass
except FileNotFoundError:
    pass
#
print('jagex files deleted')

def deposit_all_Bank():
    banker = 50
    b = random.uniform(0.1, 0.77)
    x = random.randrange(480, 500)  # x = random.randrange(1040, 1050)
    y = random.randrange(626, 647)  # y = random.randrange(775, 805)
    pyautogui.moveTo(x, y, duration=b)
    b = random.uniform(0.01, 0.1)
    pyautogui.click(x, y, duration=b, button='left')
    c = random.uniform(0.1, 4.5)
    time.sleep(c)


def invent_crop():
    return screen_Image(550, 230, 739, 493, 'inventshot.png')


def random_inventory():
    global newTime_break, actions
    actions = 'inventory tab'
    b = random.uniform(0.1, 15)
    pyautogui.press('f4')
    time.sleep(b)
    pyautogui.press('f4')
    b = random.uniform(0.1, 2)
    time.sleep(b)
    pyautogui.press('esc')
    newTime_break = True


def random_combat():
    global newTime_break, actions
    actions = 'combat tab'
    b = random.uniform(0.1, 15)
    pyautogui.press('f1')
    time.sleep(b)
    pyautogui.press('f1')
    b = random.uniform(0.1, 2)
    time.sleep(b)
    pyautogui.press('esc')
    newTime_break = True


def random_skills():
    global newTime_break, actions
    actions = 'skills tab'
    b = random.uniform(0.1, 15)
    pyautogui.press('f2')
    time.sleep(b)
    pyautogui.press('f2')
    b = random.uniform(0.1, 2)
    time.sleep(b)
    pyautogui.press('esc')
    newTime_break = True


def random_quests():
    global newTime_break, actions
    actions = 'quest tab'
    b = random.uniform(0.1, 15)
    pyautogui.press('f3')
    time.sleep(b)
    pyautogui.press('f3')
    b = random.uniform(0.1, 2)
    time.sleep(b)
    pyautogui.press('esc')
    newTime_break = True


def resize_quick():
    left = 40
    top = 49
    right = 105
    bottom = 67

    im = ImageGrab.grab(bbox=(left, top, right, bottom))
    im.save('images/screen_resize.png', 'png')
def resizeImage():
    resize_quick()
    png = 'images/screen_resize.png'
    im = Image.open(png)
    # saves new cropped image
    width, height = im.size
    new_size = (width * 4, height * 4)
    im1 = im.resize(new_size)
    im1.save('images/textshot.png')


def Miner_Image_quick():
    left = 150
    top = 150
    right = 600
    bottom = 750

    im = ImageGrab.grab(bbox=(left, top, right, bottom))
    im.save('images/miner_img.png', 'png')

def Image_to_Text(preprocess, image, parse_config='--psm 7'):
    resizeImage()
    change_brown_black()
    # construct the argument parse and parse the arguments
    image = cv2.imread('images/' + image)
    image = cv2.bitwise_not(image)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # check to see if we should apply thresholding to preprocess the
    # image
    if preprocess == "thresh":
        gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    # make a check to see if median blurring should be done to remove
    # noise
    if preprocess == "blur":
        gray = cv2.medianBlur(gray, 3)

    if preprocess == 'adaptive':
        gray = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 31, 2)

    # write the grayscale image to disk as a temporary file so we can
    # apply OCR to it
    filename = "{}.png".format(os.getpid())
    cv2.imwrite(filename, gray)
    # load the image as a PIL/Pillow image, apply OCR, and then delete
    # the temporary file
    with Image.open(filename) as im:
        text = pytesseract.image_to_string(im, config=parse_config)
    os.remove(filename)
    #print(text)
    return text

def screen_Image_new(name='screenshot.png'):
    x, y, w, h = core.getWindow(data[0]['Config']['client_title'])
    im = ImageGrab.grab(bbox=(x, y, x+w, y+h))
    im.save('images/' + name, 'png')

def Image_color_new():
    screen_Image_new('images/screenshot2.png')
    image = cv2.imread('images/screenshot2.png')
    image = cv2.rectangle(image, pt1=(600, 0), pt2=(850, 200), color=(0, 0, 0), thickness=-1)
    image = cv2.rectangle(image, pt1=(0, 0), pt2=(150, 100), color=(0, 0, 0), thickness=-1)
    # define the list of boundaries
    red = ([0, 0, 180], [80, 80, 255])  # 0 Index
    green = ([0, 180, 0], [80, 255, 80])  # 1 Index
    amber = ([0, 170, 170], [170, 255, 255])  # 2 Index
    pickup_high = ([150, 0, 100], [255, 60, 160])  # 3 Index
    attack_blue = ([200, 200, 0], [255, 255, 5])

    boundaries = [
        red, green, amber, pickup_high, attack_blue
    ]

    # loop over the boundaries
    for (lower, upper) in boundaries:
        # create NumPy arrays from the boundaries
        lower = np.array(lower, dtype="uint8")
        upper = np.array(upper, dtype="uint8")
        # find the colors within the specified boundaries and apply
        # the mask
        mask = cv2.inRange(image, lower, upper)
        output = cv2.bitwise_and(image, image, mask=mask)
        # show the images
        cv2.imshow("images", np.hstack([image, output]))
        cv2.moveWindow("images", 20, 20);
        cv2.waitKey(0)

def Image_color(left=0, top=0, right=0, bottom=0):
    screen_Image(left, top, right, bottom)
    image = cv2.imread('images/screenshot.png')
    image = cv2.rectangle(image, pt1=(600, 0), pt2=(850, 200), color=(0, 0, 0), thickness=-1)
    image = cv2.rectangle(image, pt1=(0, 0), pt2=(150, 100), color=(0, 0, 0), thickness=-1)
    # define the list of boundaries
    red = ([0, 0, 180], [80, 80, 255])  # 0 Index
    green = ([0, 180, 0], [80, 255, 80])  # 1 Index
    amber = ([0, 170, 170], [170, 255, 255])  # 2 Index
    pickup_high = ([150, 0, 100], [255, 60, 160])  # 3 Index
    attack_blue = ([200, 200, 0], [255, 255, 5])

    boundaries = [
        red, green, amber, pickup_high, attack_blue
    ]

    # loop over the boundaries
    for (lower, upper) in boundaries:
        # create NumPy arrays from the boundaries
        lower = np.array(lower, dtype="uint8")
        upper = np.array(upper, dtype="uint8")
        # find the colors within the specified boundaries and apply
        # the mask
        mask = cv2.inRange(image, lower, upper)
        output = cv2.bitwise_and(image, image, mask=mask)
        # show the images
        cv2.imshow("images", np.hstack([image, output]))
        cv2.moveWindow("images", 20, 20);
        cv2.waitKey(0)


def exit_bank(Debug=False):
    print("Exiting the bank.")
    if Debug:
        print('exit bank')
    c = random.uniform(0.1, 0.7)
    start = 650
    x = random.randrange(start, start + 13)
    if Debug:
        print('x: ', x)
    startY = 47
    y = random.randrange(startY, startY + 15)
    if Debug:
        print('y: ', y)
    b = random.uniform(0.1, 0.6)
    pyautogui.moveTo(x, y, duration=b)
    b = random.uniform(0.01, 0.3)
    pyautogui.click(duration=b, button='left')
    time.sleep(c)

def teleport_home_new():
    x, y, w, h = core.getWindow(data[0]['Config']['client_title'])
    pyautogui.press('esc')
    random_breaks(0.1, 0.3)
    pyautogui.press('f6')
    random_breaks(0.1, 0.3)
    pick_item(x+w - 170, y+h - 305)

def teleport_home():
    pyautogui.press('esc')
    random_breaks(0.1, 0.3)
    pyautogui.press('f6')
    random_breaks(0.1, 0.3)
    pick_item(1928-1280, 498)


def change_brown_black():
    # Load the aerial image and convert to HSV colourspace
    image = cv2.imread("images/textshot.png")
    #hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    # define the list of boundaries
    # BGR
    # Define lower and uppper limits of what we call "brown"
    brown_lo = np.array([0, 0, 0])
    brown_hi = np.array([60, 80, 85])

    # Mask image to only select browns
    mask = cv2.inRange(image, brown_lo, brown_hi)

    # Change image to red where we found brown
    image[mask > 0] = (0, 0, 0)

    cv2.imwrite("images/textshot.png", image)

def screen_Image(left=0, top=0, right=0, bottom=0, name='screenshot.png'):
    if left != 0 or top != 0 or right != 0 or bottom != 0:
        myScreenshot = ImageGrab.grab(bbox=(left, top, right, bottom))
    else:
        myScreenshot = ImageGrab.grab()
    myScreenshot.save('images/' + name)

def find_Object_precise(item, left=0, top=0, right=0, bottom=0):
    screen_Image(left, top, right, bottom)
    image = cv2.imread('images/screenshot.png')
    image = cv2.rectangle(image, pt1=(600, 0), pt2=(850, 200), color=(0, 0, 0), thickness=-1)
    image = cv2.rectangle(image, pt1=(0, 0), pt2=(150, 100), color=(0, 0, 0), thickness=-1)

    # define the list of boundaries
    # B, G, R

    red = ([0, 0, 180], [80, 80, 255])  # 0 Index
    green = ([0, 180, 0], [80, 255, 80])  # 1 Index
    amber = ([0, 200, 200], [60, 255, 255])  # 2 Index
    pickup_high = ([250, 0, 167], [255, 5, 172])  # 3 Index
    attack_blue = ([200, 200, 0], [255, 255, 5])
    object_list = [red, green, amber, pickup_high, attack_blue]
    boundaries = [object_list[item]]

    # loop over the boundaries
    for (lower, upper) in boundaries:
        # create NumPy arrays from the boundaries
        lower = np.array(lower, dtype="uint8")
        upper = np.array(upper, dtype="uint8")
        # find the colors within the specified boundaries and apply
        # the mask
        mask = cv2.inRange(image, lower, upper)
        output = cv2.bitwise_and(image, image, mask=mask)
        ret, thresh = cv2.threshold(mask, 40, 255, 0)
        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    if len(contours) != 0:
        # find the biggest countour (c) by the area
        c = max(contours, key=cv2.contourArea)
        #print(c)
        #print(np.squeeze(c))
        #print(Polygon(np.squeeze(c)))

        minx, miny, maxx, maxy = Polygon(np.squeeze(c)).bounds
        #print(minx, miny, maxx, maxy)

        x = random.randrange(minx + 1, max(minx + 2,maxx - 1))
        y = random.randrange(miny + 1, max(miny + 2,maxy - 1))
        #print('y: ', y)
        b = random.uniform(0.1, 0.4)
        pyautogui.moveTo(x, y, duration=b)
        b = random.uniform(0.01, 0.05)
        pyautogui.click(duration=b)
        return (x, y)
    return False



def add_blank_square_to_image(filename, left, top):
    image_name_output = 'images/blank_image.png'
    mode = 'RGBA'
    size = (25, 25)
    color = (255, 255, 255, 255)
    im = Image.new(mode, size, color)
    im.save(image_name_output, 'PNG')
    im.close()
    pos = (400 - left, 415 - top)
    frontImage = Image.open(image_name_output)
    background = Image.open(filename)
    background.paste(frontImage, pos, frontImage.convert('RGBA'))
    background.save('images/screenshot.png', format='png')

def find_Object_closest(item, left=0, top=0, right=0, bottom=0, clicker='left', size=1):
    screen_Image(left, top, right, bottom)
    add_blank_square_to_image('images/screenshot.png', left, top)
    image = cv2.imread('images/screenshot.png')
    image = cv2.rectangle(image, pt1=(600, 0), pt2=(850, 200), color=(0, 0, 0), thickness=-1)
    image = cv2.rectangle(image, pt1=(0, 0), pt2=(150, 100), color=(0, 0, 0), thickness=-1)

    # define the list of boundaries
    # B, G, R

    red = ([0, 0, 180], [80, 80, 255])  # 0 Index
    green = ([0, 180, 0], [80, 255, 80])  # 1 Index
    amber = ([0, 200, 200], [60, 255, 255])  # 2 Index
    pickup_high = ([250, 0, 167], [255, 5, 172])  # 3 Index
    attack_blue = ([200, 200, 0], [255, 255, 5]) # 4
    object_list = [red, green, amber, pickup_high, attack_blue]
    boundaries = [object_list[item]]
    close_list = []
    close_points = []
    pos = (pyautogui.position().x, pyautogui.position().y)
    # loop over the boundaries
    for (lower, upper) in boundaries:
        # create NumPy arrays from the boundaries
        lower = np.array(lower, dtype="uint8")
        upper = np.array(upper, dtype="uint8")
        # find the colors within the specified boundaries and apply
        # the mask
        mask = cv2.inRange(image, lower, upper)
        output = cv2.bitwise_and(image, image, mask=mask)
        cv2.imwrite("res1.png", np.hstack([image, output]))
        ret, thresh = cv2.threshold(mask, 40, 255, 0)
        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        cnt = contours
        for c in cnt:
            #print(cv2.contourArea(c))
            #print(cv2.boundingRect(c))
            if cv2.contourArea(c) > size:
                x1, y1, w1, h1 = cv2.boundingRect(c)
                close_list.append(abs(abs(pos[0] - x1) + abs(pos[1] - y1)))
                close_points.append((x1, y1))
    if len(contours) == 0:
        #print('not found')
        return False
    #print(close_list)
    #print(close_points)
    if len(close_list) == 0:
       return False
    min_value = min(close_list)
    min_index = close_list.index(min_value)
    coords = close_points[min_index]
    #print(coords)
    #print('min_value:', min_value, '| min_index:', min_index)
    x = random.randrange(5, 20)
    y = random.randrange(5, 20)
    icoord = coords[0] + x + left
    icoord = (icoord, coords[1] + y + top)
    b = random.uniform(0.1, 0.7)
    pyautogui.moveTo(icoord, duration=b)
    b = random.uniform(0.01, 0.3)
    pyautogui.click(icoord, duration=b, button=clicker)
    return close_points

def find_Object(item, left=0, top=0, right=0, bottom=0):
    screen_Image(left, top, right, bottom)
    image = cv2.imread('images/screenshot.png')
    image = cv2.rectangle(image, pt1=(600, 0), pt2=(850, 200), color=(0, 0, 0), thickness=-1)
    image = cv2.rectangle(image, pt1=(0, 0), pt2=(150, 100), color=(0, 0, 0), thickness=-1)
    #cv2.imwrite('images/screenshot3.png', image)
    # define the list of boundaries
    # B, G, R

    red = ([0, 0, 180], [80, 80, 255])  # 0 Index
    green = ([0, 180, 0], [80, 255, 80])  # 1 Index
    amber = ([0, 200, 200], [60, 255, 255])  # 2 Index
    pickup_high = ([150, 0, 100], [255, 60, 160])  # 3 Index
    attack_blue = ([200, 200, 0], [255, 255, 5])
    object_list = [red, green, amber, pickup_high, attack_blue]
    boundaries = [object_list[item]]

    # loop over the boundaries
    for (lower, upper) in boundaries:
        # create NumPy arrays from the boundaries
        lower = np.array(lower, dtype="uint8")
        upper = np.array(upper, dtype="uint8")
        # find the colors within the specified boundaries and apply
        # the mask
        mask = cv2.inRange(image, lower, upper)
        output = cv2.bitwise_and(image, image, mask=mask)
        ret, thresh = cv2.threshold(mask, 40, 255, 0)
        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    if len(contours) != 0:
        #print(len(contours))
        # find the biggest countour (c) by the area
        c = max(contours, key=cv2.contourArea)
        #print(contours)
        x, y, w, h = cv2.boundingRect(c)

        x = random.randrange(x + 5, x + max(w - 5, 6)) + left  # 950,960
        #print('x: ', x)
        y = random.randrange(y + 5, y + max(h - 5, 6)) + top  # 490,500
        #print('y: ', y)
        b = random.uniform(0.1, 0.4)
        pyautogui.moveTo(x, y, duration=b)
        b = random.uniform(0.01, 0.05)
        pyautogui.click(duration=b)
        return (x, y)
    else:
        return False

def find_Object_right_quick(item, left=0, top=0, right=0, bottom=0, y_range=40):
    screen_Image(left, top, right, bottom)
    image = cv2.imread('images/screenshot.png')
    image = cv2.rectangle(image, pt1=(600, 0), pt2=(850, 200), color=(0, 0, 0), thickness=-1)
    image = cv2.rectangle(image, pt1=(0, 0), pt2=(150, 100), color=(0, 0, 0), thickness=-1)

    # define the list of boundaries
    # B, G, R

    red = ([0, 0, 180], [80, 80, 255])  # 0 Index
    green = ([0, 180, 0], [80, 255, 80])  # 1 Index
    amber = ([0, 200, 200], [60, 255, 255])  # 2 Index
    pickup_high = ([250, 0, 167], [255, 5, 172])  # 3 Index
    attack_blue = ([200, 200, 0], [255, 255, 5])
    object_list = [red, green, amber, pickup_high, attack_blue]
    boundaries = [object_list[item]]

    # loop over the boundaries
    for (lower, upper) in boundaries:
        # create NumPy arrays from the boundaries
        lower = np.array(lower, dtype="uint8")
        upper = np.array(upper, dtype="uint8")
        # find the colors within the specified boundaries and apply
        # the mask
        mask = cv2.inRange(image, lower, upper)
        output = cv2.bitwise_and(image, image, mask=mask)
        ret, thresh = cv2.threshold(mask, 40, 255, 0)
        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        cnt = contours[0]
        a = cv2.pointPolygonTest(cnt, (pyautogui.position()[0], pyautogui.position()[1]), True)
        #print(a)
    if len(contours) != 0:
        #print(len(contours))
        # find the biggest countour (c) by the area
        c = max(contours, key=cv2.contourArea)
        #print('max:', c)
        x, y, w, h = cv2.boundingRect(c)

        x = random.randrange(x + 5, x + max(w - 5, 6))  # 950,960
        #print('x: ', x)
        y = random.randrange(y + 5, y + max(h - 5, 6))  # 490,500
        #print('y: ', y)
        b = random.uniform(0.01, 0.1)
        pyautogui.moveTo(x, y, duration=b)
        b = random.uniform(0.01, 0.05)
        pyautogui.click(duration=b, button='right')
        d = random.uniform(0.1,0.4)
        time.sleep(d)
        b = random.uniform(0.01, 0.05)
        c = random.randrange(0, 40)
        y = random.randrange(y_range, y_range+5)
        pyautogui.move(c, y, duration=b)
        b = random.uniform(0.01, 0.1)
        pyautogui.click(duration=b)
        return True
    else:
        return False

def find_Object_right(item, left=0, top=0, right=0, bottom=0, y_range=40):
    screen_Image(left, top, right, bottom)
    image = cv2.imread('images/screenshot.png')
    image = cv2.rectangle(image, pt1=(600, 0), pt2=(850, 200), color=(0, 0, 0), thickness=-1)
    image = cv2.rectangle(image, pt1=(0, 0), pt2=(150, 100), color=(0, 0, 0), thickness=-1)
    # define the list of boundaries
    # B, G, R

    red = ([0, 0, 180], [80, 80, 255])  # 0 Index
    green = ([0, 180, 0], [80, 255, 80])  # 1 Index
    amber = ([0, 200, 200], [60, 255, 255])  # 2 Index
    pickup_high = ([250, 0, 167], [255, 5, 172])  # 3 Index
    attack_blue = ([200, 200, 0], [255, 255, 5])
    object_list = [red, green, amber, pickup_high, attack_blue]
    boundaries = [object_list[item]]

    # loop over the boundaries
    for (lower, upper) in boundaries:
        # create NumPy arrays from the boundaries
        lower = np.array(lower, dtype="uint8")
        upper = np.array(upper, dtype="uint8")
        # find the colors within the specified boundaries and apply
        # the mask
        mask = cv2.inRange(image, lower, upper)
        output = cv2.bitwise_and(image, image, mask=mask)
        ret, thresh = cv2.threshold(mask, 40, 255, 0)
        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        cnt = contours[0]
        a = cv2.pointPolygonTest(cnt, (pyautogui.position()[0], pyautogui.position()[1]), True)
        #print(a)
    if len(contours) != 0:
        #print(len(contours))
        # find the biggest countour (c) by the area
        c = max(contours, key=cv2.contourArea)
        #print('max:', c)
        x, y, w, h = cv2.boundingRect(c)

        x = random.randrange(x + 5, x + max(w - 5, 6))  # 950,960
        #print('x: ', x)
        y = random.randrange(y + 5, y + max(h - 5, 6))  # 490,500
        #print('y: ', y)
        b = random.uniform(0.1, 0.4)
        pyautogui.moveTo(x, y, duration=b)
        b = random.uniform(0.01, 0.05)
        pyautogui.click(duration=b, button='right')
        d = random.uniform(0.1,0.5)
        time.sleep(d)
        b = random.uniform(0.01, 0.05)
        c = random.randrange(0, 40)
        y = random.randrange(y_range, y_range+5)
        pyautogui.move(c, y, duration=b)
        b = random.uniform(0.01, 0.3)
        pyautogui.click(duration=b)
        return True
    else:
        return False
def spaces(a):
    global actions
    if a == 1:
        d = random.uniform(0.05, 0.1)
        time.sleep(d)
        pyautogui.press('space')
    if a == 0:
        actions = "none"
    if a == 2:
        d = random.uniform(0.05, 0.1)
        time.sleep(d)
        pyautogui.press('space')
        d = random.uniform(0.05, 0.1)
        time.sleep(d)
        pyautogui.press('space')


def skill_lvl_up():
    counter = 0
    myScreenshot = ImageGrab.grab()
    myScreenshot.save(r"images/screen.png")
    img_rgb = cv2.imread(r"images/screen.png")
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread('images/Congrats_flag.png', 0)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
        counter += 1
    # cv2.imwrite('res.png', img_rgb)
    return counter

def skill_lvl_up_new():
    counter = 0
    screen_Image_new("images/screen.png")
    img_rgb = cv2.imread(r"images/screen.png")
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread('images/Congrats_flag.png', 0)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
        counter += 1
    # cv2.imwrite('images/res.png', img_rgb)
    return counter

def pick_item_right(v, u, option=1):
    c = random.uniform(0.1, 0.7)
    d = random.uniform(0.01, 0.15)
    x = random.randrange(v - 10, v + 10)
    #print('x: ', x)
    y = random.randrange(u - 5, u + 5)
    b = random.uniform(0.1, 0.7)
    pyautogui.moveTo(x, y, duration=b)
    time.sleep(d)
    pyautogui.click(button='right')
    time.sleep(c)
    w = random.randrange(0, 10) + x
    #print('x: ', x)
    one = random.randrange(40, 45) + y
    two = random.randrange(50, 55) + y
    three = random.randrange(60, 65) + y
    four = random.randrange(70, 75) + y
    five = random.randrange(80, 85) + y
    six = random.randrange(90,95) + y
    seven = random.randrange(100,105) + y
    eight = random.randrange(110,115) + y
    right_order = {1: one,
                   2: two,
                   3: three,
                   4: four,
                   5: five,
                   6: six,
                   7: seven,
                   8: eight
    }
    z = right_order[option]
    #print('y: ', y)
    pyautogui.moveTo(w, z, duration=b)
    b = random.uniform(0.1, 0.19)
    pyautogui.click(duration=b)
    c = random.uniform(0.1, 0.4)
    time.sleep(c)

def pick_item_new(v, u):
    c = random.uniform(0.1, 0.7)
    d = random.uniform(0.01, 0.15)
    x = random.randrange(v, v + 1)
    #print('x: ', x)
    y = random.randrange(u, u + 1)
    b = random.uniform(0.1, 0.6)
    pyautogui.moveTo(x, y, duration=b)
    time.sleep(d)
    pyautogui.click(button='left')
    time.sleep(c)

def pick_item(v, u):
    c = random.uniform(0.1, 0.7)
    d = random.uniform(0.01, 0.15)
    x = random.randrange(v - 10, v + 10)
    #print('x: ', x)
    y = random.randrange(u - 5, u + 5)
    b = random.uniform(0.1, 0.6)
    pyautogui.moveTo(x, y, duration=b)
    time.sleep(d)
    pyautogui.click(button='left')
    time.sleep(c)

def deposit_secondItem_new():
    x, y, w, h = core.getWindow(data[0]['Config']['client_title'])
    if w > 940:
        pick_item(x+w - 115, y+h - 255)
    else:
        pick_item(x+w - 115, y+h - 295)

def deposit_secondItem():
    print("Depositing the second item.")
    c = random.uniform(0.1, 0.7)
    randStartX = 921
    x = random.randrange(randStartX, randStartX + 15)  # 950,960
    #print('x: ', x)
    randStartY = 557
    y = random.randrange(randStartY, randStartY + 10)  # 490,500
    #print('y: ', y)
    b = random.uniform(0.1, 0.7)
    pyautogui.moveTo(x, y, duration=b)
    b = random.uniform(0.01, 0.3)
    pyautogui.click(duration=b, button='left')
    time.sleep(c)

def max_point(x, y, radius):
    # Calculate the distance between the point (x, y) and the center of the circle
    x = x - 745
    y = y - 110
    print(x,y)
    distance = math.sqrt(x**2 + y**2)
    print(distance)
    # If the distance is less than or equal to the radius, the point is inside the circle
    if distance <= radius:
        x = x + 745
        y = y + 110
        return x, y, True

    # If the distance is greater than the radius, the point is outside the circle
    # Calculate the angle between the point and the x-axis
    angle = math.atan2(y, x)

    # Calculate the maximum x and y coordinates that are on the circle
    max_x = radius * math.cos(angle)
    max_y = radius * math.sin(angle)
    max_x = max_x + 744
    max_y = max_y + 109
    return max_x, max_y, False

def mini_map_image(image, iwidth=0, iheight=0, threshold=0.7, clicker='left', xspace=0, yspace=0, Debug=True):
    screen_Image(661, 27, 826, 190, 'mini_map.png')
    img_rgb = cv2.imread('images/mini_map.png')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread('images/' + image, 0)
    #w, h = template.shape[::-1]
    pt = None
    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = threshold
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):
        if Debug:
            cv2.imwrite('images/res.png', img_rgb)
        x_1 = random.randrange(iwidth, iwidth + 1 + xspace)
        y_1 = random.randrange(iheight, iheight + 1 + yspace)
        if Debug:
            print("random points:", x_1,y_1)
            print("final points:", 661 + pt[0] + x_1, 30 + pt[1] + y_1)
        x, y, within_circle = max_point(661 + pt[0] + x_1, 30 + pt[1] + y_1, 74)
        icoord = (x, y)
        if Debug:
            print(icoord, within_circle)
        b = random.uniform(0.1, 0.7)
        pyautogui.moveTo(icoord, duration=b)
        b = random.uniform(0.01, 0.3)
        pyautogui.click(icoord, duration=b, button=clicker)
        if Debug:
            print(True)
        return True
    if Debug:
        print(False)
    return False

def mini_map_bool(image, threshold=0.7):
    screen_Image(1941 - 1280, 27, 2106 - 1280, 190, 'mini_map.png')
    global icoord
    global iflag
    img_rgb = cv2.imread('images/mini_map.png')
    # print('screenshot taken')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread('images/' + image, 0)
    w, h = template.shape[::-1]
    pt = None
    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = threshold
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):
        return True
    return False

def xp_quick():
    left = 469
    top = 50
    right = 525
    bottom = 170

    im = ImageGrab.grab(bbox=(left, top, right, bottom))
    im.save('images/xp_gain.png', 'png')

def xp_gain_check(image, threshold=0.95, showCoords=False):
    xp_quick()
    # read screenshot
    img = cv2.imread('images/xp_gain.png')

    template = cv2.imread('images/' + image, cv2.IMREAD_UNCHANGED)
    hh, ww = template.shape[:2]
    temp_a = template[:, :, 0:3]
    alpha = template[:, :, 3]
    alpha = cv2.merge([alpha, alpha, alpha])
    # set threshold
    threshold = threshold
    # do masked template matching and save correlation image
    corr_img = cv2.matchTemplate(img, temp_a, cv2.TM_CCORR_NORMED, mask=alpha)
    # search for max score
    #result = img.copy()
    max_val = 0
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(corr_img)
    if showCoords:
        print(max_val, max_loc)
    if max_val > threshold:
         # draw match on copy of input
        return True
    else:
        return False

def McropImage_quick():
    left = 150
    top = 150
    right = 600
    bottom = 750

    im = ImageGrab.grab(bbox=(left, top, right, bottom))
    im.save('images/screenshot2.png', 'png')


def findarea_attack_quick(object, deep=20):
    McropImage_quick()
    image = cv2.imread(r"images/screenshot2.png")

    # B, G, R
    # --------------------- ADD OBJECTS -------------------
    red = ([0, 0, 180], [80, 80, 255])
    green = ([0, 180, 0], [80, 255, 80])
    pickup_high = ([200, 0, 100], [255, 30, 190])
    attack_blue = ([250, 250, 0], [255, 255, 5])
    amber = ([0, 160, 160], [80, 255, 255])
    # --------------------- ADD OBJECTS -------------------
    ore_list = [red, green, pickup_high, attack_blue, amber]
    boundaries = [ore_list[object]]
    # loop over the boundaries
    for (lower, upper) in boundaries:
        # create NumPy arrays from the boundaries
        lower = np.array(lower, dtype="uint8")
        upper = np.array(upper, dtype="uint8")
        # find the colors within the specified boundaries and apply
        # the mask
        mask = cv2.inRange(image, lower, upper)
        output = cv2.bitwise_and(image, image, mask=mask)
        ret, thresh = cv2.threshold(mask, 40, 255, 0)
        # if (cv2.__version__[0] > 3):
        # contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        # else:
        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        if len(contours) != 0:
            # draw in blue the contours that were founded
            # cv2.drawContours(output, contours, -1, 255, 3)
            # find the biggest countour (c) by the area
            c = max(contours, key=cv2.contourArea)

            x, y, w, h = cv2.boundingRect(c)
            # draw the biggest contour (c) in green
            whalf = max(round(w / 2), 1)
            hhalf = max(round(h / 2), 1)
            # cv2.rectangle(output, (x, y), (x + w, y + h), (0, 255, 0), 2)
            x = random.randrange(x + 150 + whalf - deep, x + 150 + max(whalf + deep, 1))  # 950,960
            #print('attack x: ', x)
            y = random.randrange(y + 150 + hhalf - deep, y + 150 + max(hhalf + deep, 1))  # 490,500
            #print('attack y: ', y)
            b = random.uniform(0.01, 0.1)
            pyautogui.moveTo(x, y, duration=b)
            b = random.uniform(0.01, 0.05)
            pyautogui.click(duration=b)
            return (x,y)
    return (0,0)
    # show the images
    # cv2.imshow("Result", np.hstack([image, output]))

def Image_Rec_single(image, event, iheight=5, iwidth=5, threshold=0.7, clicker='left', ispace=20, playarea=True):
    global icoord
    global iflag
    if playarea:
        screen_Image(0, 0, 600, 750)
    else:
        screen_Image(620, 480, 820, 750)
    img_rgb = cv2.imread('images/screenshot.png')
    # print('screenshot taken')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread('images/' + image, 0)
    w, h = template.shape[::-1]
    pt = None
    # print('getting match requirements')
    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = threshold
    loc = np.where(res >= threshold)
    # print('determine loc and threshold')
    # if len(loc[0]) == 0:
    # exit()
    icoord = (0,0)
    iflag = False
    event = event
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
    # print('result of pt')
    if pt is None:
        iflag = False
        return iflag, icoord
        # print(event, 'Not Found...')
    else:
        iflag = True
        # cv2.imwrite('res.png', img_rgb)
        # print(event, 'Found...')
        if playarea == False:
            cropx = 620
            cropy = 480
        else:
            cropx = 0
            cropy = 0
        x = random.randrange(iwidth, iwidth + ispace) + cropx
        y = random.randrange(iheight, iheight + ispace) + cropy
        icoord = pt[0] + iheight + x
        icoord = (icoord, pt[1] + iwidth + y)
        b = random.uniform(0.1, 0.7)
        pyautogui.moveTo(icoord, duration=b)
        b = random.uniform(0.01, 0.3)
        pyautogui.click(icoord, duration=b, button=clicker)
    return iflag, icoord

def Image_Rec_single_closest(image, threshold=0.7, clicker='left', playarea=True):
    myScreenshot = ImageGrab.grab()
    myScreenshot.save('images/screenshot.png')
    img_rgb = cv2.imread('images/screenshot.png')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread('images/' + image, 0)
    w, h = template.shape[::-1]
    pt = None
    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = threshold
    loc = np.where(res >= threshold)
    close_list = []
    close_points = []
    pos = pyautogui.position()
    #print((pos[0],pos[1]))
    for pt in zip(*loc[::-1]):
        close_list.append(abs(abs(pos[0] - pt[0]) + abs(pos[1] - pt[1])))
        close_points.append(pt)
    if pt is None:
        #print('not found')
        return False
    #print(close_list)
    #print(close_points)
    min_value = min(close_list)
    min_index = close_list.index(min_value)
    coords = close_points[min_index]
    #print(coords)
    #print('min_value:', min_value, '| min_index:', min_index)
    if playarea == False:
        cropx = 620
        cropy = 480
    else:
        cropx = 0
        cropy = 0
    x = random.randrange(5, 20) + cropx
    y = random.randrange(5, 20) + cropy
    icoord = coords[0] + x
    icoord = (icoord, coords[1] + y)
    b = random.uniform(0.1, 0.7)
    pyautogui.moveTo(icoord, duration=b)
    b = random.uniform(0.01, 0.3)
    pyautogui.click(icoord, duration=b, button=clicker)
    return True

def bank_ready(deposit_second=True):
    bank = Image_count('bank_deposit.png', 0.75)
    #print("bank deposit open:", bank)
    if bank > 0:
        if deposit_second:
            deposit_secondItem()
        return True
    else:
        return False
    return False

def invent_enabled():
    return Image_count('inventory_enabled.png', threshold=0.95)

def run_enabled():
    return Image_count('run_enabled.png', threshold=0.95)

def make_enabled(make='make_craft.png'):
    return Image_count(make, threshold=0.95)


def image_Rec_clicker(image, event, iheight=5, iwidth=5, threshold=0.7, clicker='left', ispace=20, playarea=True, fast=False):
    global icoord
    global iflag

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
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
        print(f"Match found at: {pt}")

        if playarea == False:
            cropx = 620
            cropy = 480
        else:
            cropx = 0
            cropy = 0

        x = random.randrange(iwidth, iwidth + ispace) + cropx
        y = random.randrange(iheight, iheight + ispace) + cropy
        icoord = pt[0] + iheight + x
        icoord = (icoord, pt[1] + iwidth + y)

        print(f"Clicking at coordinates: {icoord}")

        b = random.uniform(0.05, 0.1) if fast else random.uniform(0.1, 0.3)
        pyautogui.moveTo(icoord, duration=b)

        b = random.uniform(0.01, 0.05) if fast else random.uniform(0.05, 0.15)
        pyautogui.click(icoord, duration=b, button=clicker)
        iflag = True

    return iflag
def image_Rec_inventory(image, threshold=0.8, clicker='left', iheight=5, iwidth=5, ispace=10):
    global icoord
    global iflag
    invent_crop()
    img_rgb = cv2.imread('images/inventshot.png')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread('images/' + image, 0)
    w, h = template.shape[::-1]
    pt = None
    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = threshold
    loc = np.where(res >= threshold)
    iflag = False
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
        if pt is None:
            iflag = False
        else:
            iflag = True
            x = random.randrange(iwidth, iwidth + ispace) + 620
            y = random.randrange(iheight, iheight + ispace) + 480
            icoord = pt[0] + iheight + x
            icoord = (icoord, pt[1] + iwidth + y)
            b = random.uniform(0.1, 0.3)
            pyautogui.moveTo(icoord, duration=b)
            b = random.uniform(0.01, 0.15)
            pyautogui.click(icoord, duration=b, button=clicker)
    return iflag


def Image_count(object, threshold=0.8, left=0, top=0, right=0, bottom=0):
    counter = 0
    screen_Image(left, top, right, bottom, name='screenshot.png')
    img_rgb = cv2.imread('images/screenshot.png')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread('images/' + object, 0)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
        counter += 1
    return counter

def Image_count_alpha(temp, threshold=0.89, left=0, top=0, right=0, bottom=0):
    counter = 0
    screen_Image(left, top, right, bottom, name='screenshot.png')
    # read screenshot
    img = cv2.imread('images/screenshot.png')
    # read pawn image template
    # template = cv2.imread('chess_template.png', cv2.IMREAD_UNCHANGED)
    template = cv2.imread('images/' + temp, cv2.IMREAD_UNCHANGED)
    hh, ww = template.shape[:2]
    # extract pawn base image and alpha channel and make alpha 3 channels
    temp_a = template[:, :, 0:3]
    alpha = template[:, :, 3]
    alpha = cv2.merge([alpha, alpha, alpha])
    # set threshold
    threshold = threshold
    # do masked template matching and save correlation image
    corr_img = cv2.matchTemplate(img, temp_a, cv2.TM_CCORR_NORMED, mask=alpha)
    # search for max score
    result = img.copy()
    max_val = 1
    while max_val > threshold:

        # find max value of correlation image
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(corr_img)
        #print(max_val, max_loc)

        if max_val > threshold:
            # draw match on copy of input
            counter += 1
            cv2.rectangle(result, max_loc, (max_loc[0] + ww, max_loc[1] + hh), (0, 0, 255), 2)
        else:
            break
    return counter
def invent_count(object, threshold=0.8):
    screen_Image(620, 480, 820, 750, 'inventshot.png')
    counter = 0
    img_rgb = cv2.imread('images/inventshot.png')
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread('images/' + object, 0)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
        counter += 1
    return counter
def drop_item():
    c = random.uniform(0.1, 0.2)
    d = random.uniform(0.1, 0.23)

    time.sleep(c)
    pyautogui.keyDown('shift')
    time.sleep(d)


def release_drop_item():
    e = random.uniform(0.1, 0.3)
    f = random.uniform(0.1, 0.2)

    time.sleep(e)
    pyautogui.keyUp('shift')
    time.sleep(f)


def random_breaks(minsec, maxsec):
    print(f"Initiating a random break for {minsec}-{maxsec} seconds.")
    e = random.uniform(minsec, maxsec)
    time.sleep(e)
    print(f"Random break of {e} seconds completed.")


def findarea(object):
    screen_Image()
    image = cv2.imread('images/screenshot.png')
    red = ([0, 0, 180], [80, 80, 255])  # 0 Index
    green = ([0, 180, 0], [80, 255, 80])  # 1 Index
    amber = ([0, 200, 200], [60, 255, 255])  # 2 Index
    pickup_high = ([250, 0, 167], [255, 5, 172])  # 3 Index
    attack_blue = ([250, 250, 0], [255, 255, 5])
    object_list = [red, green, amber, pickup_high, attack_blue]
    boundaries = [object_list[object]]
    # loop over the boundaries
    for (lower, upper) in boundaries:
        # create NumPy arrays from the boundaries
        lower = np.array(lower, dtype="uint8")
        upper = np.array(upper, dtype="uint8")
        # find the colors within the specified boundaries and apply
        # the mask
        mask = cv2.inRange(image, lower, upper)
        output = cv2.bitwise_and(image, image, mask=mask)
        ret, thresh = cv2.threshold(mask, 40, 255, 0)
        # if (cv2.__version__[0] > 3):
        # contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        # else:
        contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    if len(contours) != 0:
        # draw in blue the contours that were founded
        cv2.drawContours(output, contours, -1, 255, 3)
        # find the biggest countour (c) by the area
        c = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(c)
        # draw the biggest co  ntour (c) in green
        cv2.rectangle(output, (x, y), (x + w, y + h), (0, 255, 0), 2)
    # show the images
    cv2.imshow("Result", np.hstack([image, output]))
    cv2.waitKey(0)
