
import socket

hote = "localhost"
port = 55000

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((hote, port))
print ("Connection on {}".format(port))

socket.send(b"clem:mdp")

socket.close()