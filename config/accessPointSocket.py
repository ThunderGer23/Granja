# * Importing the getaddrinfo and socket functions from the socket module.
from socket import getaddrinfo, socket

# * Importing the variables from the keys.py file.
from keys import ip
from keys import nameModule as mod
from keys import passwordESPServ as passw
from keys import portToCloud as ptC


def accessPoint(sAP, AP, maxClients):
    """
    It creates an access point with the given parameters and returns the socket

    :param sAP: socket for the access point
    :param AP: the access point object
    :param maxClients: The maximum number of clients that can connect to the access point
    :return: The socket object.
    """
    AP.config(essid = mod, channel = 11, authmode = 3, password = passw)
    AP.config(max_clients = maxClients)
    AP.active(True)
    addrAP = getaddrinfo(ip, ptC)[0][-1]
    sAP = socket()
    sAP.bind(addrAP)
    sAP.listen(100)
    print(AP.ifconfig())
    return sAP