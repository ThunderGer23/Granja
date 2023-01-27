import time
from network import AP_IF, STA_IF, WLAN

# * Importing the modem and password from the keys.py file.
# ! Change access passwords for each access node
from keys.keys import modem as mod
from keys.keys import passModem as passw

# * Importing the modules from the access folder.
from config.accessPointSocket import accessPoint
from config.connectTo import internet
from config.iRequirements import requirements
from keys.sendRequestSocket import sendRequest
from messages.messages import (MessageClients, MessageConfigError, MessageWiFi, request)

# * Defining the variables that will be used in the program.
requests = None
sta_if = WLAN(STA_IF)
AP = WLAN(AP_IF)
sAP = None
maxClients = 15

def config():
    """
    It sets up the access point, connects to the internet, and installs the required packages
    :return: The return value is the result of the function.
    """
    try:
        global sAP, requests
        sAP = accessPoint(sAP, AP, maxClients)
        internet(mod, passw)
        requests = requirements()
        return 1
    except:
        return 0

def main():
    """
    A function that is called when the program starts.
    :return: The response is a string.
    """
    if (not config()):
        return MessageConfigError

    while(True):
        time.sleep(1)
        if(sta_if.isconnected()) and (len(AP.status('stations')) > 0):
            cl,addrAP = sAP.accept()
            request['message'] = cl.recv(4096)
            if(len(request['message']) == 0):
                print('Continue...')
                continue
            else:
                response = sendRequest(request, requests)
                print('Response({}): '.format(len(response)),response)
                cl.send(response)
            cl.close()
        else:
            if sta_if.isconnected() != True: print(MessageWiFi)
            if len(AP.status('stations')) == 0: print(MessageClients)

main()