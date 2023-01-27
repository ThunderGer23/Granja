from network import STA_IF, WLAN
from time import sleep_ms as slms
from accesscodes.keys import passwordESPServ as passw
from accesscodes.keys import nameModule as mod

sta_if = WLAN(STA_IF)

def internet():
    sta_if.active(True)
    sta_if.scan()
    sta_if.connect(mod,passw)
    sta_if.isconnected()
    while sta_if.isconnected() == False:
        print('A',end="")
        slms(100)
        continue
    print('!\nConnected!\n')
    return