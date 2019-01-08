import requests
from random import randint



#manca aggiunge riposo ogni 3 secondi per evitare di perdere colpi con funzione time.sleep(3)


a=requests.post("http://192.168.1.231:8000/signup", json= {"name": "VT"}) #accreditamento

print(a) #printi per vedere se ti ha registrato


#questa è un idea per svolgere, mancano le info di bruno come il numero per capire se le caselle sono già state colpite e come fare richiesta per capirlo

while True:
    x=randint(1,35)
    y=randint(1,22)

    #richiesta per vedere se la casella è già stata colpita 
    while numerocasella==1:
        x=randint(1,35)-1
        y=randint(1,35)-1
        #richiesta per vedere se la casella è già stata colpita

    b= requests.post("http://192.168.1.231:8000", json= {"x": x, "y": y})

    if numerocasella==1: #a x e y precedenti #vuol dire che l abbiamo colpita
        #richiesta per vedere se casella a x+1 è già stata colpita
        requests.post("http://192.168.1.231:8000", json= {"x": x+1, "y": y})    #colpire in orizzontale, prima controlla se non sia stata prima colpita

        if numeronuovacasella==0: #la nuova casella ad x+1
             requests.post("http://192.168.1.231:8000", json= {"x": x, "y": y+1}) #colpire in verticale, , prima controlla se non sia stata prima colpita
        elif numeronuovacasella==1:
            x=randint(1,35)
            y=randint(1,22)  





       




