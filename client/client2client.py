from access.connectTo import internet
from access.iRequirements import requirements
from time import sleep_ms as slms
import espnow

#COM6 MAC (izq): b'X\xbf%6\x1e\x94'
#COM3 MAC (der): b'x\xe3m\t\xb3\x0c'

MAC = None
peers = [b'X\xbf%6\x1e\x94',b'x\xe3m\t\xb3\x0c']
rad = espnow.ESPNow()

def config():
    MAC = internet('NSFW','NotSafe=4Work')
    print('Hi! My MAC is ', MAC)
    rad.active(True)
    peers.remove(MAC)
    print('And my peers are: ', peers)
    for peer in peers:
        rad.add_peer(peer)

async def send(msg):
    await rad.send(msg)

def main():    
    num = 0
    var = ''
    print('Starting communications')
    while(True):
        send(str(num))
        num += 1
        host, msg = rad.recv(1000)
        try:            # msg == None if timeout in recv()
            print(host,' says: ', msg)
        except Exception as e:
            print(Exception)
    
if __name__ == "__main__":
    config()
    main()
