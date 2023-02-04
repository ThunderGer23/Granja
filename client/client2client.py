from access.connectTo import internet
from access.iRequirements import requirements
from time import sleep_ms as slms
import espnow


#COM6 MAC (izq): b'X\xbf%6\x1e\x94'
#COM3 MAC (der): b'x\xe3m\t\xb3\x0c'

MAC = internet('NSFW','NotSafe=4Work')

rad = espnow.ESPNow()
rad.active(True)
peers = [b'X\xbf%6\x1e\x94',b'x\xe3m\t\xb3\x0c']
peers.remove(MAC)
for peer in peers:
    rad.add_peer(peer)
    
num = 0
var = ''
print('Starting communications')
while(True):
    for peer in peers:
        var = rad.send(peer,str(num),False)
    num += 1
    host, msg = rad.irecv(100)
    if(msg):             # msg == None if timeout in recv()
        print(host,' says: ', msg)
        if(msg == b'end'):
            break
    
