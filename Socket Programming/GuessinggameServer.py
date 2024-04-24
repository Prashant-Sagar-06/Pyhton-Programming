'''Guessing Game: Description: Develop a server-client guessing game using Python's 
socket module. The server generates a random number, and the client tries to guess 
it by sending guesses to the server. The server provides hints (higher or lower) until 
the client guesses the correct number. This exercise helps in understanding how to 
handle communication between client and server for interactive games.'''

import socket
import random
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = ('localhost', 1234)
s.bind(address)

s.listen(1)
print("Waiting for connection...")

client, addr = s.accept()
print('Connection from', addr)
number = random.randint(1, 100)
while True:
    data = client.recv(1024)
    if not data:
        break
    guess = int(data)
    if guess == number:
        client.send(b'Correct!')
        break
    elif guess < number:
        client.send(b'Higher')
    else:
        client.send(b'Lower')
    client.close()
