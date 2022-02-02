import time
import threading
import pyautogui as ptg
import keyboard as key


# cookieLocation = ptg.locateOnScreen('./assets/cookie.PNG')
# print(cookieLocation)

# while 1 : 
#     # ptg.scroll(-15, x = 500, y = 500)
#     print(ptg.position())
#     if key.is_pressed('q'): 
#         quit()




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

clicks = 0
c = False
while 1 :
    if key.is_pressed('t'):
        if c:
            c = False
            print(f'not clicking clicked: {clicks}')
            clicks = 0
            time.sleep(.5)
        else:
            c = True
            print('clicking')
            time.sleep(.5)
    if c:
        # pos = ptg.position()
        # ptg.click(pos.x, pos.y)
        threads = []
        for _ in range(50):
            t = threading.Thread(target=click)
            t.start()
            threads.append(t)
            clicks += 40
        for thread in threads:
            thread.join()
    if key.is_pressed('q'):
        quit()
