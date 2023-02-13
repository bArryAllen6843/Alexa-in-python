from email.mime import audio
from http import server
import pyjokes
from time import strftime
from tkinter import EXCEPTION
from unittest import result
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import pywhatkit
from news import *
from selenium_web import Infow
import randfacts
from weather import *

#pip install pipwin
#pipwin install pyaudio
#pip install wikipedia

# sapi5 an API which microsoft provides for voice recognition 
engine = pyttsx3.init('sapi5')

# there are by default two available voices: male and female
voices = engine.getProperty('voices')
#print(voices)

# voices[0] = male voice & voices[1] = female voice
engine.setProperty('voice', voices[1].id)
#print(voices[0].id)

rate = engine.getProperty('rate')
engine.setProperty('rate', 190)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Good morning!")
    elif hour>=12 and hour<18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")

    speak("I am your Alexa, what can i do for you")


def takeCommand():
    # it takes microphone input from the user and returns string output

    # recognizer class helps in recognizing speech
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        r.energy_threshold = 1000
        audio = r.listen(source)

    try:
        query = r.recognize_google(audio, language='en')
        if 'alexa' in query:
            query = query.replace('alexa', '')
            print(f'{query}\n')

    except Exception as e:
        print("Say that again please...")
        return None
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smpt.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('email', 'password')
    server.sendmail('email', to, content)
    server.close()

if __name__=="__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        # logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'information' in query:
            speak('you need information related to which topic ?')
            query = query.replace("information", "")
            r = sr.Recognizer()
            with sr.Microphone() as source:
                r.pause_threshold = 1
                audio = r.listen(source)
                infor = r.recognize_google(audio)

            speak("searching {} in wikipedia".format(infor))
            assist = Infow()
            assist.get_info(infor)

        elif 'open youtube' in query:
            speak('opening youtube')
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play downloaded songs' in query:
            music_dir = 'C:\\Users\\Asus\\Music\\Playlists'
            songs = os.listdir(music_dir)
            print(songs)
            speak('playing music')
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'time' in query:
            speak("here's what i found")
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f'Current time is {strTime}')

        elif 'open vs code' in query:
            codePath = "C:\\Users\\Asus\\VS code\\Code.exe"
            os.startfile(codePath)

        elif 'play' in query:
            song = query.replace('play', '')
            if 'alexa' in song:
                song = song.replace('alexa', '')
                speak('playing' + song + 'on you-tube')
                pywhatkit.playonyt(song)

        elif 'date' in query:
            speak('sorry, I have a headache')

        elif 'are you single' in query:
            speak('I am in a relationship with wifi')

        elif 'joke' or 'jokes' in query:
            speak("sure sir, get ready for some chuckles")
            speak(pyjokes.get_joke())
            speak('hahahaha!')

        elif 'send email to aayush' in query:
            try:
                speak("what should i say?")
                content = takeCommand()
                to = "codeseeker07@gmail.com"
                sendEmail(to, content)
                speak("Emial has been sent!")
            except Exception as e:
                print(e)
                speak("I am not able to send this email")

        elif 'news' in query:
            speak('sure sir, here are some todays news articles')
            arr = news()
            for i in range(len(arr)):
                print(arr[i])
                speak(arr[i])
                
        elif 'fact' or 'facts' in query:
            speak('sure sir, ')
            x = randfacts.get_fact()
            print(x)
            speak("Did you know that, " + x)

        elif 'weather' or 'temperature' in query:
            speak('Which city you want to know weather for ?')
            r = sr.Recognizer()
            with sr.Microphone() as source:
                r.pause_threshold = 1
                r.energy_threshold = 1000
                cityName = r.listen(source)
                speak('Temperature in {cityName} is - ' + str(temp()))