import time
import pyautogui as ptg
import keyboard as key

class Coords: 
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.baseColor = ptg.screenshot(region=(x, y, x, y)).getpixel((0, 0))

def click(coords): 
    ptg.click(coords.x, coords.y-5)
def ss(coords):
    return ptg.screenshot(region=(coords.x, coords.y, coords.x, coords.y))
def canClick(coords):
    return ss(coords).getpixel((0, 0)) != coords.baseColor
def rgbCloseEnough(rgb):
    bsbRGB = [6, 18, 24]
    sens = 5
    count = 0
    for c in range(len(rgb)) :
        if rgb[c] > (bsbRGB[c] - sens) and rgb[c] < (bsbRGB[c] + sens) :
            count += 1
    return count == 3


# cursor = Coords(1662, 619)
# upgrades = Coords(1615, 516)
cookie = Coords(300, 500)
sideButtons = [Coords(1662, 619)]
sideBtnClicks = [0]

def canAdd():
    rgb = Coords(1631, sideButtons[len(sideButtons)-1].y + 63)
    if rgbCloseEnough(ss(rgb).getpixel((0, 0))):
        newBtn = Coords(1662, sideButtons[len(sideButtons)-1].y + 63)
        sideButtons.append(newBtn)
        sideBtnClicks.append(0)
        return 1
    return 0
def inRange(index):
    rgb = Coords(1631, sideButtons[index].y)
    return not rgbCloseEnough(ss(rgb).getpixel((0, 0)))
while not canClick(sideButtons[0]): 
    click(cookie)

click(sideButtons[0])
sideBtnClicks[0] += 1
upgrades = Coords(1615, 486)
myTimer = 0

while 1: 
    click(cookie)
    myTimer+=1
    indexOf = -1
    try:
        indexOf = sideBtnClicks.index(0)
        if not inRange(indexOf):
            indexOf = -1
    except:
        indexOf = -1

    if myTimer > 5 and indexOf == -1:
        myTimer = 0
        canAdd()
        for btn in range(len(sideButtons)-1, -1, -1):
            while canClick(sideButtons[btn]):
                click(sideButtons[btn])
                sideBtnClicks[btn] += 1
        if canClick(upgrades): 
            click(upgrades)
    elif myTimer > 5 and indexOf != -1:
        myTimer = 0
        canAdd()
        if canClick(sideButtons[indexOf]):
            click(sideButtons[indexOf])
            sideBtnClicks[indexOf] += 1

    if key.is_pressed('q'): 
        quit()
    

# def getBounds(): 
#     while 1: 
#         som = ptg.position()
#         som = Coords(som.x, som.y)
#         # print(ss(som).getpixel((0, 0)))
#         print(ptg.position())
#         if key.is_pressed('q'): 
#             quit()
# getBounds()
