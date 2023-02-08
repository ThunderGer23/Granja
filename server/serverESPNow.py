import network, espnow

sta = network.WLAN(network.STA_IF)
sta.active()
sta.disconnect()

e = espnow.ESPNow()
e.active(True)
peer = b'\x00\x00\x00\x00\x00\x00'
e.add_peer(peer)
while True:
    host, msg = e.recv()
    if msg:
        print(host, msg)
        if msg == b'end':
            break