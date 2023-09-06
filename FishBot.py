import threading
from pyautogui import *
import pyautogui
import time
import keyboard

'''
For this tool to work you need to manually set cordinates of certain objects
because of screen resolution differences and program position differences
'''

#Set to 'True' if you want to see your cursor cordinates shown in console
debug=False

#preset X/Y coordinates of certain game objects for tool to work
innerBauble = 1080,690 # inner fishing bubble preferably left middle side
VShapeOrnament = 1104,653 # it should be on the fishing bubble where you need to hit directions
confirmationButton = 1000,720 # confirmation button on fish catching 



fishing = False #dont touch
def up():
    keyboard.press('w')
    time.sleep(0.1)
    keyboard.release('w')
def down():
    keyboard.press('s')
    time.sleep(0.1)
    keyboard.release('s')
def left():
    keyboard.press('a')
    time.sleep(0.1)
    keyboard.release('a')
def right():
    keyboard.press('d')
    time.sleep(0.1)
    keyboard.release('d')
def space():
    keyboard.press('space')
    time.sleep(0.1)
    keyboard.release('space')

def checkCords():
    while True:
        x, y = pyautogui.position()
        print(f"x: {x}, y: {y}")
        time.sleep(1)
def checkColor():
    while True:
        x, y = pyautogui.position()
        r, g, b = pyautogui.pixel(x, y)
        print(f"The RGB value of the pixel at ({x}, {y}) is ({r}, {g}, {b})")
        time.sleep(1)
def doFishing():
    global fishing
    #up = The RGB value of the pixel at (1701, 507) is (225, 50, 50)
    #down = The RGB value of the pixel at (1673, 536) is (52, 144, 245)
    #left = The RGB value of the pixel at (1713, 567) is (244, 196, 66)
    #right = The RGB value of the pixel at (1726, 462) is (45, 235, 43)
    #space = The RGB value of the pixel at (1666, 432) is (174, 49, 208)
    while fishing:
        pic = pyautogui.screenshot(region=(innerBauble,20,20)) #bauble region
        width, height = pic.size

        for x in range(0, width):
            for y in range(0, height):
                r,g,b = pic.getpixel((x,y))
                
                if r == 225 and g == 50 and b == 50:
                    threading.Thread(target=up).start()
                if r == 52 and g == 144 and b == 245:
                    threading.Thread(target=down).start()
                if r == 244 and g == 196 and b == 66:
                    threading.Thread(target=left).start()
                if r == 45 and g == 235 and b == 43:
                    threading.Thread(target=right).start()
                if r == 174 and g == 49 and b == 208:
                    threading.Thread(target=space).start()


#MAIN LOOP
if debug:
    threading.Thread(target=checkCords).start()
    #threading.Thread(target=checkColor).start()
while True:
    time.sleep(0.1)
    while fishing == False:
        print('throwing rod')
        pic = pyautogui.screenshot(region=(VShapeOrnament,2,2))
        width, height = pic.size

        for x in range(0, width):
            for y in range(0, height):
                r,g,b = pic.getpixel((x,y))
                if r != 255 and g != 255 and b != 255: 
                    fishing = True
        time.sleep(1)
    if fishing == True: 
        print('started fishing')
        keyboard.press('space')
        time.sleep(0.1)
        keyboard.release('space')

        threading.Thread(target=doFishing).start()
        threading.Thread(target=doFishing).start()
        time.sleep(3)
    while True:
        print("waiting for catch...")
        breakout = False
        
        pic = pyautogui.screenshot(region=(confirmationButton,2,2))
        width, height = pic.size
        
        for x in range(0, width):
            for y in range(0, height):
                r,g,b = pic.getpixel((x,y))
                if r >= 248 and g >= 248 and b >= 248:
                    breakout = True
        time.sleep(0.5)
        if breakout:
            keyboard.press('space')
            time.sleep(0.1)
            keyboard.release('space')
            fishing = False
            break
