import network, time, upip, socket
import json as ujson
requests = None
sta_if = network.WLAN(network.STA_IF)
AP = network.WLAN(network.AP_IF)
sAP = None

def internet():
    sta_if.active(True)
    sta_if.scan()
    sta_if.connect('Totalplay-64AA','64AA2A07y2jxWzgP')
    sta_if.isconnected()
    while sta_if.isconnected() == False:
        print('A',end="")
        time.sleep_ms(100)
        continue
    print('!\nConnected!\n')
    return

def accessPoint():
    global sAP
    AP.config(essid = 'ESP_32', channel = 11, authmode = 3, password = '12345678')
    AP.config(max_clients = 15)
    AP.active(True)
    addrAP = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
    sAP = socket.socket()
    sAP.bind(addrAP)
    sAP.listen(100)
    print(AP.ifconfig())
    return

def requirements():
    global requests
    upip.debug = True
    upip.install('urequests')
    import urequests
    requests = urequests
    return

def sendRequest(req):
    token = req["token"]
    message = req['message']
    url = req['url']
    request = {'token': token,'message': message}
    post_data = ujson.dumps(request).encode('utf8')
    print("\n\n",str(post_data),"\n\n")
    res = requests.post(url,headers = {'content-type': 'application/json'},data=post_data)
    return res.text
            
def config():
    accessPoint()
    internet()
    requirements()
    return

def main():
    request = {
        'token':'daa39d53-6283-47a1-b945-b7ee6528dde0',#'5f7be1f5-3dbb-41dc-8645-300beced1fe4',
        'message':'Beep-boop',
        'url':'https://notigram-api.fly.dev/sendMessage'
    }
    text = ''
    while(True):
        time.sleep(1)
        if(sta_if.isconnected()) and (len(AP.status('stations')) > 0):
            cl,addrAP = sAP.accept()
            request['message'] = cl.recv(4096)
            if(len(request['message']) == 0):
                print('Continue...')
                continue
            else:
                response = sendRequest(request)
                print('Response({}): '.format(len(response)),response)
                cl.send(response)
            cl.close()
        else:
            if sta_if.isconnected() != True: print('Wi-Fi is not connected.')
            if len(AP.status('stations')) == 0: print('No hay clientes :\'v')
    return
        

config()
main()
    