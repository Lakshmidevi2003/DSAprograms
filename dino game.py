import pyautogui as p
import time
print("playint")
i=0
y=1
while True:
    i+=1
    if (i%2==0):
        x=p.pixel(540,182)
        if x!=y:
            p.press('space')
            y=x
            time.sleep(0.009)
    else:
       x=p.pixel(540,227)
       if x!=y:
         p.press('space')
         y=x
         time.sleep(0.009)   
