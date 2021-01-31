import pyautogui as p
import time as t
import cv2
import keyboard as k



t.sleep(3)



while(k.is_pressed('ctrl') == False):
    img = p.screenshot(region=(440,200,950,600))
    for x in range(0,950,5):
        for y in range(0,600,5):
            r,g,b = img.getpixel((x,y))
            if((b==34)and(g==87)):
                p.click(x+440,y+200)
                t.sleep(0.2)
                break


#for getting pixel where you point the mouse
#while 1:
#    x,y = p.position()
#    print(p.pixel(x,y))
#    t.sleep(2)
