import machine, network, espnow

sta = network.WLAN(network.STA_IF)
sta.active()
sta.disconnect()

e = espnow.ESPNow()
e.active(True)
peer = b'\x00\x00\x00\x00\x00\x00'
e.add_peer(peer)

e.send('hello world from python')
for i in range(100):
    e.send(peer, str(i)*20, True)
    e.send(b'end')
