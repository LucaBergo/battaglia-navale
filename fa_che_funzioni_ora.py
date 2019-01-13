import requests
from random import randint
import time






def coords(x,y):


	d=requests.get("http://192.168.1.231:8000/info").json()
	d=d["field"]["grid"][y][x]
	while d==1 or d==2:
		x=randint(0,23)
		y=randint(0,35)
		d=requests.get("http://192.168.1.231:8000/info").json()
		d=d["field"]["grid"][y][x]
	



def attack(x,y):
	b=requests.post("http://192.168.1.231:8000", json= {"x": x, "y": y})
	d=requests.get("http://192.168.1.231:8000/info").json()
	d=d["field"]["grid"][y][x]
	if d==2:
		#d=requests.get("http://192.168.1.231:8000/info").json()
		#d=d["field"]["grid"][y][x]
		if x<23 or x>=0:
			d=requests.get("http://192.168.1.231:8000/info").json()
			d=d["field"]["grid"][y][x+1]
			if d==0:
				for i in range(1,8):
					if x>23:
						break
					else:
						d=requests.get("http://192.168.1.231:8000/info").json()
						d=d["field"]["grid"][y][x+i]
						if d==0:
							requests.post("http://192.168.1.231:8000", json= {"x": x+i, "y": y})
		
				 
			
			elif d==1:
				if x<=23 or x>0:
					d=requests.get("http://192.168.1.231:8000/info").json()
					d=d["field"]["grid"][y][x-1]
					if d==0:
						for i in range(1,8):
							if x<0:
								break
							else:
								d=requests.get("http://192.168.1.231:8000/info").json()
								d=d["field"]["grid"][y][x-i]
								if d==0:
									requests.post("http://192.168.1.231:8000", json= {"x": x-i, "y": y})
	
		if y<=35 or y>0:
			d=requests.get("http://192.168.1.231:8000/info").json()
			d=d["field"]["grid"][y-1][x]
			if d==0:
				for i in range(1,8):
					if y>0:
						break
					else:
						d=requests.get("http://192.168.1.231:8000/info").json()
						d=d["field"]["grid"][y-i][x]
						if d==0:
							requests.post("http://192.168.1.231:8000", json= {"x": x, "y": y-1})
	
			elif d==1 or d==2:
				if y<35 or y>=0:
					d=requests.get("http://192.168.1.231:8000/info").json()
					d=d["field"]["grid"][y-1][x]
					if d==0:
						for i in range(1,8):
							if y>35:
								break
							else:
								d=requests.get("http://192.168.1.231:8000/info").json()
								d=d["field"]["grid"][y-i][x]
								if d==0:
									requests.post("http://192.168.1.231:8000", json= {"x": x, "y": y-1})





while True:

	time.sleep(3)
	x=randint(0,23)
	y=randint(0,35)
	a=coords(x,y)
	
	if a==0:
		attack(x,y)


	

