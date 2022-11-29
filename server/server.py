from machine import Pin
import urequests
import network
import socket
import json

from alerts.messages import MessageError, MessageData, MessageClients, MessageEnd, MessageConnecting, MessageConnected, MessageWaitConnect, MessageConnectedNetwork

# Setting up the LED pin as an output pin.
led = Pin(2, Pin.OUT)
input = Pin(3, Pin.INPUT)

from time import sleep_ms as sms

# Creating a wifi access point.
wifi = network.WLAN(network.AP_IF if input.value() == 1 else network.STA_IF)

# Creating a socket object.
s = socket.socket()

def configure_wifi(Channel: int):
    # Configuring the wifi access point.
    wifi.config(essid = 'ThunderGer', channel = Channel, authmode = 3, password = '12345678')
    wifi.config(max_clients = 15)
    if (wifi.active(True)):
        return True
    return False

def configure_wifi_connector(ssid: str, password: str):
    wifi.active(False)
    sms(5)
    wifi.active(True)
    return 1 if wifi.connect(ssid, password) else 0

def configure_socket(Port: int):
    addr = socket.getaddrinfo('0.0.0.0', Port)[0][-1]
    s.bind(addr)
    s.listen(10)
    return addr

def readClients() :        
    return len(wifi.status('stations'))

def waitClients():    
    channel = 11
    port = 80
    print (configure_socket(port) if configure_wifi(channel) else MessageError)
    print(wifi.ifconfig())                      
    while input.value() == 1:        
        sms(1000)
        if(readClients() > 0): 
            cl,addr = s.accept() 
            data = cl.recv(4096)
            if (len(data) == 0):
                continue
            else: 
                print(MessageData,str(data))
                if (str(data) == "b'Holi'"):
                    prueba = "Crayoli"
                    response = json.dumps({'header':'HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n','data':'{"response":'+ prueba +'}'})
                cl.send(response)  
            cl.close()         
        else:
            print(MessageClients)
    return 1    

def sendMessages():
    print(MessageWaitConnect if configure_wifi_connector('IZZI-6854', '3C0461086854') else MessageConnectedNetwork)
    if not wifi.isconnected():
        print(MessageConnected)
        while(not wifi.isconnected() and timeout < 5):
            led.value(1)
            sms(1)
            print(5- timeout, 'seconds')
            timeout += 1
            led.value(0)
            sms(1)  
    else:
        print(MessageConnecting)
        print(wifi.ifconfig())
        req = urequests.get('https://redcod-production.up.railway.app/test')        
        print(req.text)
        led.value(1)

print(MessageEnd if not waitClients() else sendMessages())