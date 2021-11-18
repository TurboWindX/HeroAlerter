#!/usr/bin/env python3
import requests,sys,json,time
import pygame

from datetime import datetime
import os
import platform

WD = [] #Full workers list
GW = []
BA = [] #Audio alert list 
MH = [] #list of dict containing workername and minimum hashrate

def main():
    try:   
        pygame.init() #Fast and dirty way to get true cross-platform audio play.
        sysos = platform.system() #Get current OS (Linux,MAC,Windows)
        
        if sysos == "Windows":
            os.system('cls')
            cwd = os.path.dirname(os.path.realpath(__file__))#Get current working dir
            audio_file = cwd + '\\audio.wav' #Path to audio file
            Sound = pygame.mixer.Sound(audio_file) #Define a Sound object with previous audio file 
            print("#####################################################################")
            print("################# HeroMiners Crypto Worker Alerter###################")
            print("#####################################################################")
            print()
            
            CRYPTO = input("Please enter the full name of your CRYPTO. (e.g: aeon,haven,monero): ") #This is used to point to correct subdomain
            
            URL = "https://" + CRYPTO + ".herominers.com/api/stats_address?address=" #Start building URL
            ADDRESS = input("Please enter your crypto address:")
            URL = URL + ADDRESS + "&longpoll=false" #Finish building URL
            intervalx = int(input("Please enter how many seconds do you want between each scans? (Recommended is 60 (1minute) or 600 (10minutes)): "))
            if(intervalx <= 10):#10seconds is pretty quick already, no need to go crazy
                intervalx = 10
            brange = int(input("How many times should the alert ring?:"))
            r = requests.get(url = URL)#GET request to HeroMiners API
            data = r.json()
            data = data['workers'] #Parsing, yay
            for hr in data:
                    if(WD.count(hr['name']) <= 0): #Check if WD contains name of worker
                        WD.append(hr['name'])
                        x = "Yes"
                        try:
                            x = input("Do you want to add " + hr['name'] + " on the alert list ? Y or N(default is Y): ")
                        except:
                            print()
                        try:
                            if(x[0].upper() == "Y"):
                                BA.append(hr['name'])
                        except:
                            BA.append(hr['name'])
                        print("Current hashrate of " + str(hr['name']) + " is "+ str(hr['hashrate']))
                        y = 1
                        try:
                          y = int(input("Do you want to put a minimum hashrate for this worker? (Enter a number, 1 is default): "))
                        except:
                          print()
                        MH.append({"workername":str(hr['name']),"minhashrate":y})
                        
                        
                            
            while 1:
                time.sleep(intervalx)
                r = requests.get(url = URL)#get request to api
                data = r.json() #serialize
                data = data['workers'] #parse
                print()
                print()
                print()
                print()
                print()
                print()
                print()
                print()
                now = datetime.now() #get time
                now = now.strftime("%H:%M:%S") #print time
                print("Time of scan: " + now)
                print("##################################################")
                for hr in data:
                    if(WD.count(hr['name']) <= 0): #check if new worker has been added
                        WD.append(hr['name'])
                        x = input("Do you want to add " + hr['name'] + " on the alert list ? Y or N: ")
                        if(x[0].upper() == "Y"):
                            BA.append(hr['name'])
                        print("Current hashrate of " + str(hr['name']) + " is "+ str(hr['hashrate']))
                        y = int(input("Do you want to put a minimum hashrate for this worker? (Enter a number, 0 is default): "))
                        if(y >= 1):
                            MH.append({"workername":str(hr['name']),"minhashrate":y})

                    #if(hr['hashrate'] == 0): #if worker hashrate is 0
                    #    print(hr['name'] + " IS DOWN!!! ALERT ALERT ALERT ! ! !")
                    #    if(BA.count(hr['name']) >= 1): #if it is on the audio alert list
                    #        for i in range(brange): #iterate for the number of times desired
                            
                                #print('\a')
                                #print(hr['name'] + " IS DOWN!!! ALERT ALERT ALERT ! ! !")
                                #Sound.play()

                    #TODO minimum hashrate
                    #if(hr['hashrate'] >= 1):
                    #    print(hr['name'] + " IS OK.")
                    #    if(GW.count(hr['name']) <= 1):
                    #        GW.append(hr['name'])
                    # 

                    for workerdata in MH:
                        if(workerdata['workername'] == hr['name']):
                            if(workerdata['minhashrate'] >= hr['hashrate']):
                                print(hr['name'] + " IS DOWN!!! ALERT ALERT ALERT ! ! !")
                                for workers in BA:
                                    if(workers == hr['name']):
                                        for i in range(brange):
                                            Sound.play()
                                            time.sleep(2)
                            if(workerdata['minhashrate'] < hr['hashrate']):
                                print(hr['name'] + " is OK.")
                          

                           

                    
                print("##################################################")
                print()     
                #print(WD)
        
        if sysos == "Linux":
            os.system('clear')
            cwd = os.path.dirname(os.path.realpath(__file__))
            audio_file = cwd + '/audio.wav'
            Sound = pygame.mixer.Sound(audio_file)
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
            brange = int(input("How many times should the alert ring?:"))
            r = requests.get(url = URL)
            data = r.json()
            data = data['workers']
            if(WD.count(hr['name']) <= 0): #check if new worker has been added
                        WD.append(hr['name'])
                        try:
                            x = input("Do you want to add " + hr['name'] + " on the alert list ? Y or N(default is Y): ")
                            if(x[0].upper() == "Y"):
                                BA.append(hr['name'])
                        except:
                            BA.append(hr['name'])
                        print("Current hashrate of " + str(hr['name']) + " is "+ str(hr['hashrate']))
                        y = int(input("Do you want to put a minimum hashrate for this worker? (Enter a number, 0 is default): "))
                        if(y >= 1):
                            MH.append({"workername":str(hr['name']),"minhashrate":y})
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
                        try:
                            x = input("Do you want to add " + hr['name'] + " on the alert list ? Y or N(default is Y): ")
                            if(x[0].upper() == "Y"):
                                BA.append(hr['name'])
                        except:
                            BA.append(hr['name'])
                    #if(hr['hashrate'] == 0):
                    #    print(hr['name'] + " IS DOWN!!! ALERT ALERT ALERT ! ! !")
                    #    if(BA.count(hr['name']) >= 1):
                    #        for i in range(brange):
                    #            #print('\a')
                    #            #print(hr['name'] + " IS DOWN!!! ALERT ALERT ALERT ! ! !")
                    #            Sound.play()
                    #            #playsound(audio_file)
                    #            
                            

                    #if(hr['hashrate'] >= 1):
                    #    print(hr['name'] + " IS OK.")
                    #    if(GW.count(hr['name']) <= 1):
                    #        GW.append(hr['name'])
                    #        
                    for workerdata in MH:
                        if(workerdata['workername'] == hr['name']):
                            if(workerdata['minhashrate'] >= hr['hashrate']):
                                print(hr['name'] + " IS DOWN!!! ALERT ALERT ALERT ! ! !")
                                for workers in BA:
                                    if(workers == hr['name']):
                                        for i in range(brange):
                                            Sound.play()
                                            time.sleep(2)
                            if(workerdata['minhashrate'] < hr['hashrate']):
                                print(hr['name'] + " is OK.")
                    
                print("##################################################")
                print()     
                #print(WD)
    except Exception as e: print(e)
        
if __name__ == "__main__":
    main()