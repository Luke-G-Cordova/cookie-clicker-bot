import time
import threading
import os
import pyautogui as ptg
import keyboard as key


globVars = {
    "clickAway": False, 
    "clicks": 0
}
def handelCtrlI():
    if globVars["clickAway"]:
        globVars["clickAway"] = False
        print(f'not clicking clicked: {globVars["clicks"]}')
        globVars["clicks"] = 0
        time.sleep(.5)
    else:
        globVars["clickAway"] = True
        print('clicking')
        time.sleep(.5)

key.add_hotkey('q', os._exit, args=[0])
key.add_hotkey('ctrl+i', handelCtrlI)


def goldenCookie():
        image = './assets/golden_cookie.PNG'
        found = ptg.locateOnScreen(image, confidence=0.8)
        if found == None:
            return False
        else:
            found = ptg.center(found)
            pos = ptg.position()
            ptg.click(found.x, found.y)
            ptg.click(pos.x, pos.y)
            print('clicked gcookie')
            return True

def click():
    pos = ptg.position()
    ptg.click(pos.x, pos.y)
    ptg.click(pos.x, pos.y)
    ptg.click(pos.x, pos.y)
    ptg.click(pos.x, pos.y)
    ptg.click(pos.x, pos.y)
    ptg.click(pos.x, pos.y)
    ptg.click(pos.x, pos.y)
    ptg.click(pos.x, pos.y)
    ptg.click(pos.x, pos.y)
    ptg.click(pos.x, pos.y)



while 1 :
    if globVars["clickAway"]:
        goldenCookie()
        threads = []
        for _ in range(50):
            t = threading.Thread(target=click)
            t.start()
            threads.append(t)
            globVars["clicks"] += 40
        
        for thread in threads:
            thread.join()


