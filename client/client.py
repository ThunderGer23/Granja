import socket

while(True):
 with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
  addr = ("192.168.4.1",80)
  s.connect(addr) 
  message = bytes(input('Message: '),'utf-8')
  s.sendall(message)
  print(str(s.recv(4096),'utf-8'))
  s.close()