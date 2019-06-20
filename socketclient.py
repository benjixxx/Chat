import socket

hote = "localhost"
port = 55000

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect(('localhost', 55000))
print ("Connection on {}".format(port))

socket.sendall(b"clement:azerty")
