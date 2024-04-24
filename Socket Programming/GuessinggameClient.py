import socket
import random
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
address = ('localhost', 1234)
s.connect(address)
while True:
    guess = input('Guess a number: ')
    s.send(guess.encode())
    data = s.recv(1024)
    print('Server:', data.decode())
    if data.decode() == 'Correct!':

        break
s.close()



