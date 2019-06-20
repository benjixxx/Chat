#coding: utf-8
from pg import DB
import socket
import re
# Connexion à la database
db= DB(dbname='conn', host='localhost', port=5432, user='pguser', passwd='Azerty1')

# def envoi(ip, port):
#         global socket
#         port = port
#         socket.connect((ip, port))
#         socket.send(b"clem:mdp")
#         socket.close()
    

def insert(nom,mdp,mail):

    qry="INSERT INTO utilisateur VALUES ( '" + nom + "',' " + mail +"', '"+ mdp +"' )"
    db.query(qry)
    db.commit()
    
def verif(nom,mdp):

        qry="SELECT EXISTS ( SELECT * FROM utilisateur WHERE nom='" + nom + "' AND mdp='" + mdp + "') AS test"
        for row in db.query(qry):
                if row[0] == True:
                        return True
                else:
                        return False

# #Créer la table si elle n'existe pas
        db.query("""CREATE TABLE IF NOT EXISTS utilisateur (
        nom     varchar(100) UNIQUE,
        mail    varchar(200),
        mdp     varchar(20)) """)

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   
socket.bind(('', 55000))
socket.listen(200)
client, address = socket.accept()
while True:
        response= client.recv(2048).decode()
        rep=response.split(':')
        nom=rep[0]
        mdp=rep[1]
        if (len(rep)) == 3:
                mail=rep[2]
                patternMail="^\w+@\w+..{2,3}(.{2,3})?$"
                if not re.match(patternMail, mail):
                       client.send(b"Format du mail incorrect")
                else :
                    insert(nom,mdp,mail)
                    nom=nom.encode()
                    client.send(nom +b":True")

        elif verif(nom,mdp) == True:
                nom=nom.encode()
                client.send(nom +b":True")
        else:
                nom=nom.encode()
                client.send(nom+b":False")
                


#             insert(nom,mail,mdp)
#     except:
#     while 
#     if verif(nom,mdp) == True:
#         nom=nom.encode()
#         client.send(nom +b":True")
#     else:
#         nom=nom.encode()
#         client.send(nom+b":False")
#         response= client.recv(2048).decode()
#         rep=response.split(':')
#         print(rep[0],rep[1])

# client.close()
# socket.shutdown()


