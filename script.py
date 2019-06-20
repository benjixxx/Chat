import datetime
import time

with open("logs.txt", "a") as file:
    day = datetime.datetime.now()
    file.write("Création du compte " + "le : " + day.strftime("%b %d %Y %H:%M:%S") + "\n") 
