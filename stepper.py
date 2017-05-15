from machine import Pin as pin
p1 = pin(16 , pin.OUT)
p2 = pin(14 , pin.OUT)
p3 = pin(12 , pin.OUT)
p4 = pin(13 , pin.OUT)
led = pin(15 , pin.OUT)

from time import sleep
def loop_single(t=0.01, pin1=p1,pin2=p3,pin3=p2,pin4=p4):
    '''mind the inversion 1-3-2-4'''
    while True:
        pin1.high()
        pin2.low()
        pin3.low()
        pin4.low()
        sleep(t)
        pin1.low()
        pin2.high()
        pin3.low()
        pin4.low()
        sleep(t)
        pin1.low()
        pin2.low()
        pin3.high()
        pin4.low()
        sleep(t)
        pin1.low()
        pin2.low()
        pin3.low()
        pin4.high()
        sleep(t)

def loop_double(t=0.01, pin1=p1,pin2=p3,pin3=p2,pin4=p4):
    '''mind the inversion 1-3-2-4'''
    while True:
        pin1.high()
        pin2.high()
        pin3.low()
        pin4.low()
        sleep(t)
        pin1.low()
        pin2.high()
        pin3.high()
        pin4.low()
        sleep(t)
        pin1.low()
        pin2.low()
        pin3.high()
        pin4.high()
        sleep(t)
        pin1.high()
        pin2.low()
        pin3.low()
        pin4.high()
        sleep(t)


def right(delay):
    loop_single(t = delay)

def left(delay):
    loop_single(t = delay,pin1=p4,pin2=p2,pin3=p3,pin4=p1)
