import requests
from random import randint
import time



#manca aggiunge riposo ogni 3 secondi per evitare di perdere colpi con funzione time.sleep(3)


a=requests.post("http://192.168.1.231:8000/signup", json= {"name": "VT"}).json() #accreditamento

print(a) #printi per vedere se ti ha registrato


c=requests.get("http://192.168.1.231:8000/info").json()

#print(c)




#questa è un idea per svolgere, mancano le info di bruno come il numero per capire se le caselle sono già state colpite e come fare richiesta per capirlo

while True:
    time.sleep(3)
    x=randint(0,23)
    y=randint(0,35)

    d=requests.get("http://192.168.1.231:8000/info").json()
    d= d["field"]["grid"][x][y]
    #print(d)


   
    while d==1:
        x=randint(0,23)
        y=randint(0,35)
        d=requests.get("http://192.168.1.231:8000/info").json()
        d=d["field"]["grid"][x][y]

    b= requests.post("http://192.168.1.231:8000", json= {"x": x, "y": y})



    #if d==1:
    #    requests.post("http://192.168.1.231:8000", json= {"x": x+1, "y": y})



    #    #richiesta per vedere se casella a x+1 è già stata colpita
    #    requests.post("http://192.168.1.231:8000", json= {"x": x+1, "y": y})    #colpire in orizzontale, prima controlla se non sia stata prima colpita
#
    #    if numeronuovacasella==0: #la nuova casella ad x+1
    #         requests.post("http://192.168.1.231:8000", json= {"x": x, "y": y+1}) #colpire in verticale, , prima controlla se non sia stata prima colpita
    #    elif numeronuovacasella==1:
    #        x=randint(1,35)
    #        y=randint(1,22)  


