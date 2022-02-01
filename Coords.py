import time, os
import threading
import pyautogui as ptg
import keyboard as key

class Coords: 
    def __init__(self, x, y):
        self.x = x
        self.y = y
        try: 

            self.baseColor = ptg.screenshot(region=(x, y, x, y)).getpixel((0, 0))
        except:
            self.baseColor = (0,0,0)


class Clicker:

    def __init__(self):
        self.BUTTON_IMAGES = os.listdir('./assets')
        self.SB_HEIGHT = 64
        self.SB_DARK = [6, 18, 24]
        self.INVIS_UP = 110
        self.INVIS_DOWN = 1000

        self.cookie = self.findSomeButton(2)
        
        self.abvUpgrades = self.findSomeButton(1)
        self.abvSideBtns = self.findSomeButton(0)
        self.store = self.abvSideBtns
        self.store.y -= 400
        self.sideBtnX = self.abvSideBtns.x
        self.scrolled = 0
        sb1 = Coords(1662, 619)
        sb1.index = 0
        self.sideButtons = [sb1]
        self.sideBtnClicks = [0]

        self.whosControl = 0
        self.mt = 0
        self.gt = 0
        self.ut = 0
        self.st = 0
        self.st1 = 0

    def run(self):
        while not self.canClick(self.sideButtons[0]) :
            self.click(self.cookie)

        self.abvUpgrades = self.findSomeButton(1)
        self.click(self.sideButtons[0])
        self.upgrades = Coords(1615, 486)


        t0 = threading.Thread(target=self.mainThread)
        t1 = threading.Thread(target=self.cookieThread)
        t2 = threading.Thread(target=self.goldCookieThread)
        t3 = threading.Thread(target=self.upgradeThread)
        t4 = threading.Thread(target=self.sideButtonThread)
        
        t0.start()
        t1.start()
        t2.start()
        t3.start()
        t4.start()
    def cookieThread(self):
        while 1:
            if self.whosControl == 1:
                self.click(self.cookie)
            if key.is_pressed('q'): 
                quit()
    def goldCookieThread(self):
        while 1:
            goldCookie = self.findGoldCookie()
            if goldCookie.x != 0 and goldCookie.y != 0 :
                self.gt = 1
            else:
                self.gt = 0

            if self.whosControl == 2:
                self.click(goldCookie)
                self.gt = 0

            if key.is_pressed('q'): 
                quit()
    def upgradeThread(self):
        while 1:
            if self.canClick(self.upgrades): 
                self.ut = 1
            else:
                self.ut = 0
            if self.whosControl == 3 :
                self.click(self.upgrades)
                self.ut = 0
            if key.is_pressed('q'): 
                quit()
    def sideButtonThread(self):
        while 1:
            try:
                indexOf = self.sideBtnClicks.indexOf(0)
                if not self.waitForNext(indexOf):
                    indexOf = -1
            except:
                indexOf = -1
            newButton = 0
            casb = self.canAddSideButton()
            if casb:
                self.st = 1
            else:
                self.st = 0
            if indexOf == -1:
                for btn in range(len(self.sideButtons)-1, -1, -1):
                    # self.scrollStore(self.outOfRange(self.sideButtons[btn]))
                    if self.canClick(self.sideButtons[btn]):
                        newButton = self.sideButtons[btn]
                        self.st1 = 1
                        break
                    else:
                        self.st1 = 0
            elif indexOf != -1:
                if self.canClick(self.sideButtons[indexOf]):
                    self.st1 = 1
                    newButton = self.sideButtons[indexOf]
                else:
                    self.st1 = 0
            if self.whosControl == 4:
                if casb:
                    self.addSideButton()
                if newButton != 0:
                    self.click(newButton)
                self.st = 0 
                self.st1 = 0
            if key.is_pressed('q'): 
                quit()
                

    def mainThread(self):
        while 1:
            if self.gt == 1:
                while self.ut == 1 or self.st == 1 or self.st1 == 1:0
                self.whosControl = 2
            elif self.ut == 1:
                while self.gt == 1 or self.st == 1 or self.st1 == 1:0
                self.whosControl = 3
            elif self.st == 1 or self.st1 == 1:
                while self.ut == 1 or self.gt == 1:0
                self.whosControl = 4
            else:
                while self.ut == 1 or self.st == 1 or self.st1 == 1 or self.gt == 1:0
                self.whosControl = 1
            
            if key.is_pressed('q'): 
                quit()


    def canClick(self, coords):
        cPs = Coords(coords.x, coords.y + self.scrolled)
        return not self.rgbCloseEnough(self.ss(cPs).getpixel((0, 0)), coords.baseColor, 20)

    def waitForNext(self, index):
        rgb = Coords(1631, self.sideButtons[index].y + self.scrolled)
        return not self.rgbCloseEnough(self.ss(rgb).getpixel((0, 0)), self.SB_DARK, 20)

    def outOfRange(self, coords):
        y = coords.y + self.scrolled
        if y < self.INVIS_UP or y > self.INVIS_DOWN:
            if self.scrolled < 0:
                return self.INVIS_UP - y
            else: 
                return y - self.INVIS_DOWN
        else:
            return 0

    def findGoldCookie(self):
        return self.findSomeButton(3)

    def canAddSideButton(self):
        y = self.sideButtons[len(self.sideButtons)-1].y + self.SB_HEIGHT + self.scrolled
        rgb = Coords(1631, y)
        return self.rgbCloseEnough(self.ss(rgb).getpixel((0, 0)), self.SB_DARK, 20)

    def addSideButton(self):

        y = self.sideButtons[len(self.sideButtons)-1].y + self.SB_HEIGHT + self.scrolled
        rgb = Coords(1631, y)

        if self.rgbCloseEnough(self.ss(rgb).getpixel((0, 0)), self.SB_DARK, 20):

            ny = self.sideButtons[len(self.sideButtons)-1].y + self.SB_HEIGHT - self.scrolled

            newBtn = Coords(1662, ny)
            newBtn.index = len(self.sideButtons)
            self.sideButtons.append(newBtn)
            self.sideBtnClicks.append(0)

            return 1
        return 0

    def rgbCloseEnough(self, rgb, bsbRGB, sens = 5):
        count = 0
        for c in range(len(rgb)) :
            if rgb[c] > (bsbRGB[c] - sens) and rgb[c] < (bsbRGB[c] + sens) :
                count += 1
        return count == 3

    def scrollStore(self, sc):
        ptg.moveTo(self.store.x, self.store.y)
        ptg.scroll(sc)
        self.scrolled += sc

    def findSomeButton(self, index):
        image = './assets/' + self.BUTTON_IMAGES[index]
        found = ptg.locateOnScreen(image)
        if found == None:
            return Coords(0, 0)
        found = ptg.center(found)
        return Coords(found.x, found.y)
    def click(self, coords):
        cPs = Coords(coords.x, coords.y + self.scrolled)
        try:
            self.sideBtnClicks[coords.index] += 1
        except:
            0
        ptg.click(cPs.x, cPs.y-5)
    def move(self, coords):
        ptg.moveTo(coords.x, coords.y-5)
    def ss(self, coords):
        return ptg.screenshot(region=(coords.x, coords.y, coords.x, coords.y))
    

c = Clicker()
c.run()