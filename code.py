import speech_recognition as sr
import pyaudio
import pywhatkit
import os
import pyttsx3
engine =pyttsx3.init()
rate=engine.getProperty("rate")
engine.setProperty("rate",110)
engine.say("welcome , mohamed fayad")
engine.runAndWait()
lis=sr.Recognizer()
with sr.Microphone() as source:
    print("Listen...")
    voice =lis.listen(source)
    command= lis.recognize_google(voice)
    command=command.lower()
    print(command)
    if("open") in command:
        command=command.replace("open",'')
        if("play") in command:
            command=command.replace("play",'')
            pywhatkit.playonyt(command)  
        if("notepad") in command:
            os.system("notepad")
                
   