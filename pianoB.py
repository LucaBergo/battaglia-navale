import requests
from random import randint
import time



while True:
	
	time.sleep(3)
	x=randint(0,23)
	y=randint(0,35)

	d=requests.get("http://192.168.1.231:8000/info").json()
	d=d["field"]["grid"][y][x]

	while d==1:
		x=randint(0,23)
		y=randint(0,35)

		d=requests.get("http://192.168.1.231:8000/info").json()
		d=d["field"]["grid"][y][x]


	b=requests.post("http://192.168.1.231:8000", json= {"x": x, "y": y})



