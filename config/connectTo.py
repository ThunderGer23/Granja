from network import STA_IF, WLAN
from time import sleep_ms as slms

def internet(mod, passw):
    """
    It connects to the internet
    
    @param mod: The name of the WiFi network you want to connect to
    @param passw: The password for the WiFi network
    @return: Nothing.
    """
    sta_if = WLAN(STA_IF)
    sta_if.active(True)
    sta_if.scan()
    sta_if.connect(mod,passw)
    sta_if.isconnected()
    while sta_if.isconnected() == False:
        print('A',end="")
        slms(100)
        continue
    MAC = sta_if.config("mac")
    print('\nMAC Address is: ',MAC)
    return MAC

if __name__ == '__main__':
    internet('NSFW','NotSafe=4Work')
