import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import pyjokes
from ecapture import ecapture as ec
                      


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")

    speak("I am ASHU your Voice assistant Please let me know How may I help you.")

def takeCommannd():
    #it takes microphone input from the user and returns string output

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio=r.listen(source)

    try:
        print("Recognising...")
        querry=r.recognize_google(audio, language='en-in')
        print(f"User said: {querry}\n")
    
    except Exception as e:
        #print(e)

        print("Say that again please.....")
        return "None"
    return querry


if __name__== "__main__":
    wishMe()
    while True:
        querry=takeCommannd().lower()

        #Logic for executing tasks based on query
        if 'wikipedia' in querry:
            speak('Searching wikipedia...')
            querry=querry.replace("wikipedia", "")
            results = wikipedia.summary(querry, sentences=2)
            speak("According to wikipedia")
            speak(results)

        elif 'open youtube' in querry:
            webbrowser.open("youtube.com")

        elif 'open facebook' in querry:
            webbrowser.open("facebook.com")

        elif 'open instagram' in querry:
            webbrowser.open("instagram.com")

        elif 'open google' in querry:
            webbrowser.open("google.com")

        elif 'open amazon' in querry:
            webbrowser.open("amazon.com")

        elif 'play music' in querry:
            musicdir='D:\\My Songs'
            songs=os.listdir(musicdir)
            print(songs)
            a=random.randint(0,11)#we can take the length of songs too but as i had only 12 songs in my list so i had directly written 12
            os.startfile(os.path.join(musicdir,songs[a]))

        elif 'the time' in querry:
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Hello, the time is {strtime}")

        elif 'open spotify' in querry:
            spotifypath="C:\\Users\\hp\\AppData\\Roaming\\Spotify\\Spotify.exe"
            os.startfile(spotifypath)

        elif 'zoom meeting' in querry:
            zoompath="C:\\Users\\hp\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"
            os.startfile(zoompath)

        elif 'listen to harry styles' in querry:
            webbrowser.open("https://www.youtube.com/@HarryStyles/featured")

        elif 'tech channel in youtube' in querry:
            b=random.randint(0,5)
            if b==0:
                webbrowser.open("https://www.youtube.com/@TechBurner")
            elif b==1:
                webbrowser.open("https://www.youtube.com/@TrakinTech")
            elif b==2:
                webbrowser.open("https://www.youtube.com/@TechnicalGuruji")
            elif b==3:
                webbrowser.open("https://www.youtube.com/@unboxtherapy")
            elif b==4:
                webbrowser.open("https://www.youtube.com/@EverythingApplePro")
            elif b==5:
                webbrowser.open("https://www.youtube.com/@austinevans")

        elif 'tell me a joke' in querry:
            myjoke=pyjokes.get_joke(language="en",category="all")
            speak(f"Ok here goes a joke,  {myjoke}")

        elif "weather" in querry:
            webbrowser.open("https://www.google.com/search?q=todays+weather&oq=todays+weather&aqs=chrome..69i57.3038j0j1&sourceid=chrome&ie=UTF-8")

        elif "camera" in querry or "take a photo" in querry:
            ec.capture(0, "Ashu Camera ", "img.jpg")
    

        

                
