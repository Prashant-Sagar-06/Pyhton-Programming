import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
address=(socket.gethostname(),1234)
s.connect(address)

while True:
    data = input('client:').encode()
    s.send(data)
    res = s.recv(1024)
    if not res:
        break
    print('Server:',res.decode())
s.close()    

