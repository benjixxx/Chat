# coding: utf-8
nom=""
mdp=""

def main():
    global nom
    global mdp
    import socket
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.bind(('', 55000))

    while True:
            socket.listen(5)
            client, address = socket.accept()
            response= client.recv(2048)
            rep=response.split(':')
            nom=rep[0]
            mdp=rep[1]
            client.close()

