from PIL import ImageGrab, ImageOps
from numpy import *
import pyautogui
import time

class Cordinates():
    replayBtn = (960, 380)
    dinosaurHead = (702, 385)
    #395
    #740

def restartGame():
    pyautogui.click(Cordinates.replayBtn)

def pressSpace():
    pyautogui.keyDown('space')
    time.sleep(0.05)
    print("Jump")
    pyautogui.keyUp('space')

def imageGrab():
    box = (Cordinates.dinosaurHead[0] + 38, Cordinates.dinosaurHead[1], Cordinates.dinosaurHead[0] + 100, Cordinates.dinosaurHead[1] + 37)
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    return a.sum()

def main():
    restartGame()
    while True:
        if(imageGrab() != 2550):    
            pressSpace()
            time.sleep(0.1)

main()