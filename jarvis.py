from ast import Num
from importlib.util import spec_from_file_location
from sys import _enablelegacywindowsfsencoding
from tokenize import Double
import pyttsx3
import speech_recognition as sr
import webbrowser
import pywhatkit
import os
import wikipedia
import pyautogui
import time
import keyboard

Assistant= pyttsx3.init('sapi5')
voices=Assistant.getProperty('voices')
print(voices)
Assistant.setProperty('voices',voices[0].id)
Assistant.setProperty('rate',170)

def Speak(audio):
      
    print('')
    Assistant.say(audio)
    print(f':{audio}')
    Assistant.runAndWait()
    
    
def takecommand():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening...')
        command.pause_threshold=1
        audio=command.listen(source)
        
        try:
            print("recognizing...")
            query= command.recognize_google(audio,language='en-in')
            print(f"you said:{query}")
            
        except Exception as Error:
            return "None"
        return query.lower()


query=takecommand()
if 'jarvis' in query:
    Speak('yes sir , what can i do for you')
else:
    Speak('no command found')

def TaskExe():
    
    def Whatsapp():
        Speak("who should i text sir")
        # name=takecommand()
        
        # if 'gowrav' in name:
        #     Speak('what should i text sir')
        #     msg=takecommand()
        #     Speak("tell me the time")
        #     hour=int(takecommand())
        #     Speak('time in minutes')
        #     pywhatkit.sendwhatmsg("+918904126670",msg,hour,min,5)
        #     Speak("ok sir ,the message is sent0")
        
        
        
        
      
        
        
    def Music():
        Speak('what should i play sir')
        musicName=takecommand()
    
        if 'heart attack' in musicName:
            os.startfile('Telegram Desktop\\heartattack.p3')

        else:
            pywhatkit.playonyt(musicName)
        Speak('enjoy your music sir')     
        
    def openapps():
        Speak('ok sir,wait a second')
        
        if 'telegram' in query:
            os.startfile('D:\\vedio\\Telegram.exe')

        elif 'opera' in query:
            os.startfile('C:\\Users\\Abhi\\AppData\\Local\\Programs\\Opera GX\\launcher.exe')
    
        elif 'anime' in query:
            webbrowser.open('https://animeowl.net')
        elif 'HD today' in query:
            webbrowser.open('https://hdtoday.cc//home')
        elif 'ibomma' in query:
            webbrowser.open('https://ww2.ibomma.cc//telugu-movies/')
        elif 'movie rules' in query:
            webbrowser.open('https://movierulzhd.ink//movies/')
        elif 'youtube' in query:
            webbrowser.open('https://www.youtube.com')
        elif 'maps' in query:
            webbrowser.open('https://www.google.com/maps/@15.0172605,76.3178081,7z')
        Speak('here you go sir')
    

        
   
    while True:
        query=takecommand()
        if 'jarvis' in query:
             Speak('welcome back sir')
             Speak('How can i help you today')        
        elif 'how are you' in query:
            Speak('i am fine sir')
        
        elif 'take a break jarvis' in query:
            Speak('fine sir')
            Speak('call me any time you need')
            break
        elif 'search youtube' in query:
            Speak('these are your results')
            query=query.replace("jarvis","")
            query=query.replace("search youtube","")
            web='https://www.youtube.com/results?search_query='+query
            webbrowser.open(web)

        elif 'google search' in query:
            Speak('these are your results')
            query=query.replace("jarvis","")
            query=query.replace("google search","")
            pywhatkit.search(query)
            
        
        
        elif 'open website' in query:
            Speak('these are your results')
            query=query.replace("jarvis","")
            query=query.replace("website","")
            web1=query.replace("open","")
            web2='https://www.'+web1+'.com/'
            webbrowser.open(web2)
            
        elif 'launch website' in query:
            Speak('launching')
            query=query.replace("launch","")
            web=query.replace("website","")
            web3='https://www.'+web+'.com'
            webbrowser.open(web3)
            
        elif 'music' in query:
            
            Music()
        
        elif 'wikipedia' in query:
            Speak('searching wikipedia')
            query=query.replace("jarvis","")
            query=query.replace("wikipedia","")
            wiki=wikipedia.summary(query,2)
            Speak(f"according to wikipedia:{wiki}")

        
            
            
        elif 'screenshot' in query:
            query=query.replace("jarvis take","")
            kk=pyautogui.screenshot()
            kk.save('C:\\Users\\Abhi\\OneDrive\\Pictures\\Screenshots')
            
            
        elif 'open youtube' in query:
            openapps()
        elif 'open telegram' in query:
            openapps()
            
        elif 'open anime' in query:
            openapps()
        elif 'open HD' in query:
            openapps()
        elif 'open ibomma ' in query:
            openapps()
        elif 'open movie rules' in query:
            openapps()
        elif 'open maps' in query:
            openapps()
        elif 'open opera' in query:
            openapps()
        
        elif 'send message' in query:
            Whatsapp()
        
TaskExe()
