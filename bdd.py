#coding: utf-8
from pg import DB
import socket1

rec=socket1.main()


# Connexion à la database
db= DB(dbname='conn', host='localhost', port=5432, user='pguser', passwd='Azerty1')

def insert(nom,mail,mdp):

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


if verif("cle1ment","azerty") == True:
        pass 
else:
        pass
