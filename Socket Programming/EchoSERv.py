'''. Echo Server: Description: Create a simple server using Python's socket module that 
echoes back any message received from a client. Upon connection, the server should 
accept messages from the client and send the same message back to the client. This 
is a fundamental exercise to understand the basic communication between a client 
and a server using sockets.
'''

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = ('localhost', 1234)
s.bind(address)

s.listen(1)
print("Waiting for connection...")

while True:
    client, addr = s.accept()
    print('Connection from', addr)
    data = client.recv(1024)
    if not data:
        break
    print("Client:", data)
    client.send(data)
    print("Echo Sent")
    client.close()