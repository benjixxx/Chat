# coding: utf-8
import socket
nom=""
mdp=""


socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(('', 55555))

while True:
    socket.listen(5)
    client, address = socket.accept()
    response= client.recv(2048)
    rep=response.decode('utf-8')
    print(type(rep))
    rep=rep.split(':')
    nom=rep[0]
    mdp=rep[1]
    print(mdp,nom)
    client.close()

