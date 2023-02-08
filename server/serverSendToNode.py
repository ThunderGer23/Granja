import time
from network import AP_IF, STA_IF, WLAN

from config.accessPointSocket import accessPoint
from messages.messages import MessageEnd, request

requests = None
sta_if = WLAN(STA_IF)
AP = WLAN(AP_IF)
sAP = None
maxClients = 15

def config():
    try:
        global sAP, requests
        sAP = accessPoint(sAP, AP, maxClients)
        requests = requirements()
        return 1
    except:
        return 0

def main():
    if (not config()):
        return MessageEnd

    while(True):
        time.sleep(1)
        if(len(AP.status('stations')) > 0):
            cl,addrAP = sAP.accept()
            request['message'] = cl.recv(4096)
            if(len(request['message']) == 0):
                print('Continue...')
                continue
            else:
                response = 'Probando alv :v/'
                print('Response({}): '.format(len(response)),response)
                cl.send(response)
            cl.close()

main()