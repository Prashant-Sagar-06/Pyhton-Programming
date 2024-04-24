''' Chat Application: Description: Implement a basic chat application using Python's 
socket module where multiple clients can connect to a server and communicate 
with each other. Clients should be able to send messages to the server, which will 
broadcast them to all other connected clients. Additional features like joining and 
leaving notifications can be included to enhance the functionality.'''

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = (socket.gethostname(), 1234)
s.bind(address)

s.listen(1)
print("Waiting for connection..." , address)
client, addr = s.accept()
print('Connection from', addr)


while 1:
    data = client.recv(1024)
    if not data:
        break
    print("Client:", data.decode())
    data = input("Server:").encode()
    client.send(data)
client.close()
s.close()    