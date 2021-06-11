from recordaudio import recordAudio
#from nmap_mod import nmap_scan
from response import *
from programs import *
from utilities import *
from nmap_mod import *

while True:
    try:
        recorded_audio = recordAudio()

        if "name" in recorded_audio:
            speak("My name is Bob")
  
        # how are you?
        if "how are you" in recorded_audio:
            speak("I am fine...")  
        
        # date
        if "date" in recorded_audio:
            # get today's date
            speak("The date is" + get_date()) 
        
        # time
        if "time" in recorded_audio:
            # get current time 
            speak("The time is " + get_time())

        #start a full scan antivirus
        elif 'full scan' in recorded_audio:
            full_scan()
        
        elif 'full scam' in recorded_audio:
            full_scan()

        #start a quick antivirus scan
        elif 'quick scan' in recorded_audio:
            quick_scan()

        elif 'quick scam' in recorded_audio:
            quick_scan()
            
        #set ip for nmap
        if ' set ' in recorded_audio:
            host = input("What ip do you want to scan? ")

        #nmap module
        elif 'scan' in recorded_audio:
            nmap_scan(recorded_audio,host)

        elif 'scam' in recorded_audio:
            nmap_scan(recorded_audio,host)     
        
        #open a program
        elif 'open' in recorded_audio:
            open(recorded_audio)
        

        #find something in google
        elif 'google' in recorded_audio:
            web(recorded_audio)


    except Exception:
        print("Bob dont understand you, plz try again...")
        
