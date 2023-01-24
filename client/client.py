import socket, network, time

sta_if = network.WLAN(network.STA_IF)

def internet():
    sta_if.active(True)
    sta_if.scan()
    sta_if.connect('ESP_32','12345678')
    sta_if.isconnected()
    while sta_if.isconnected() == False:
        print('A',end="")
        time.sleep_ms(100)
        continue
    print('!\nConnected!\n')
    return

def sendData(data):
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        addr = ("192.168.4.1",80)
        print(addr)
        s.connect(addr) 
        message = bytes(data,'utf-8')
        s.sendall(message)
        print(str(s.recv(4096),'utf-8'))
    except Exception as e:
        print(e,'!!!')
        pass
    finally:
        s.close()
    return
    
def main():
    messages = [
        "(1/8) Holi, esta es una prueba desde la ESP.",
        "(2/8) Esto ya deberia correr correctamente.",
        "(3/8) En este momento estos mensajes estan saliendo de la ESP esclavo,",
        "(4/8) Pasan por la ESP maestro,",
        "(5/8) Llegan hasta la API, y de ahi se envian a Telegram,",
        "(6/8) Y dan mensaje de confirmacion desde la API,",
        "(7/8) Que regresa a la ESP maestro, y luego a la ESP esclavo.",
        "(8/8) Todo un viaje de ida y vuelta, Eh? :3"
        ]
    
    for message in messages:
        sendData(message)
    return

internet()
main()