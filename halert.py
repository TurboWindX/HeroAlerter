#!/usr/bin/python
import requests,sys,json,time,winsound
from datetime import datetime
from os import system,name
f = 220
l = 1000
WD = []
GW = []
BA = []		

try:	
	system('cls||clear')
	print("#####################################################################")
	print("################# HeroMiners Crypto Worker Alerter###################")
	print("#####################################################################")
	print()
	
	CRYPTO = input("Please enter the full name of your CRYPTO. (e.g: aeon,haven,monero): ")
	
	URL = "https://" + CRYPTO + ".herominers.com/api/stats_address?address="
	ADDRESS = input("Please enter your crypto address:")
	URL = URL + ADDRESS + "&longpoll=false"
	intervalx = int(input("Please enter how many seconds do you want between each scans? (Recommended is 60 (1minute) or 600 (10minutes)): "))
	if(intervalx <= 10):
		intervalx = 10

	f = int(input("Please select BEEP frequency for the alerts. (Recommended 220-880): "))
	
	
	while 1:
		time.sleep(intervalx)
		r = requests.get(url = URL)
		data = r.json()
		data = data['workers']
		print()
		print()
		print()
		print()
		print()
		print()
		print()
		print()
		now = datetime.now()
		now = now.strftime("%H:%M:%S")
		print("Time of scan: " + now)
		print("##################################################")
		for hr in data:
			if(WD.count(hr['name']) <= 0):
				WD.append(hr['name'])
				x = input("Do you want to add " + hr['name'] + " on the BEEP alert list ? Y or N: ")
				if(x[0].upper() == "Y"):
					BA.append(hr['name'])

			if(hr['hashrate'] == 0):
				print(hr['name'] + " IS DOWN!!! ALERT ALERT ALERT ! ! !")
				if(BA.count(hr['name']) >= 1):
					winsound.Beep(f,l)


			if(hr['hashrate'] >= 1):
				print(hr['name'] + " IS OK.")
				if(GW.count(hr['name']) <= 1):
					GW.append(hr['name'])
					

			
		print("##################################################")
		print()		
		#print(WD)
except:
	print("Script crashed for some dark magic reasons. Ctrl+c and restart !")
