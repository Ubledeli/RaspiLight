from gpiozero import RGBLED as rgb
from uvloop.asyncio import sleep as uvsleep


l1 = rgb(9,11,10)
l2 = rgb(6,5,13)

def light(r=0, g=0, b=0):
    return((100-r)/100, (100-g)/100, (100-b)/100)


l1.color = light(90,20,80)
l1.color = light(100,70,10)
