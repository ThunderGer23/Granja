from machine import Pin
from time import sleep_ms as sms
import _thread as th

SR1 = {}
SR2 = {}

def setup():
    global SR1, SR2
    SR1 = {
        'DATA':Pin(16,Pin.OUT),
        'CLEAR':Pin(17,Pin.OUT),
        'CLOCK':Pin(18,Pin.OUT),
        'num':0,
        'display': [
            [1,1,1,1,0,1,1,1],
            [0,0,0,1,0,0,0,1],
            [0,1,1,0,1,0,1,1],
            [0,0,1,1,1,0,1,1],
            [0,0,0,1,1,1,0,1],
            [0,0,1,1,1,1,1,0],
            [1,1,1,1,1,1,0,0],
            [0,0,0,1,0,0,1,1],
            [1,1,1,1,1,1,1,1],
            [0,0,0,1,1,1,1,1],
        ]
    }

    SR2 = {
        'DATA':Pin(19,Pin.OUT),
        'CLEAR':Pin(21,Pin.OUT),
        'CLOCK':Pin(22,Pin.OUT),
        'num':0,
        'display': [
            [1,1,1,1,1,1,0,0],
            [0,0,1,1,1,1,1,0],
            [1,1,1,1,1,1,1,1],
            [0,0,0,1,0,0,1,1],
            [0,0,0,1,1,1,1,1],
            [0,0,0,1,0,0,0,1],
            [0,1,1,0,1,0,1,1],
            [0,0,1,1,1,0,1,1],
            [0,0,0,1,1,1,0,1],
            [1,1,1,1,0,1,1,1],
        ]
    }
    SR1['CLEAR'].value(1)
    SR2['CLEAR'].value(1)
    return

def ver(reg: dict):
    reg['CLEAR'].value(0)
    sms(250)
    reg['CLEAR'].value(1)
    reg['DATA'].value(1)
    for i in range(7):
        reg['DATA'].value(1) if(reg['display'][reg['num']][i] == 1) else reg['DATA'].value(0)
        reg['CLOCK'].value(1)
        sms(250)
        reg['CLOCK'].value(0)
    return

def looping(reg: dict):
    ver(reg)
    sms(250)
    reg['num'] = 0 if reg['num'] == 10 else reg['num']+1
    return

setup()
'''
th.start_new_thread(looping,(SR1,))
th.start_new_thread(looping,(SR2,))
'''
looping(SR1)
looping(SR2)