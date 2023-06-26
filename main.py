#Created by Bhavya Doshi: https://www.linkedin.com/in/bhavyadoshi7
#Check README.md to configure the initial packages 

import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

talk('hello my name is bhavya, how can i help you?') #Cange the name from Bhavya to your name is you like

def take_command():
    with sr.Microphone() as source:
        print('listening...')
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        if 'bhavya' in command:
            command = command.replace('bhavya', '')
    return command

def run_bhavya():
    command = take_command()
    if 'play' in command:  #Play from Youtube
        word_yt = command.replace('play', '')
        talk('playing' +word_yt)
        print('playing' +word_yt)
        pywhatkit.playonyt(word_yt)
    elif 'time' in command:  #Show Time
        time = datetime.datetime.now().strftime('%I:%M %p')
        print('Current time is ' +time)
        talk('Current time is ' +time)
    elif 'search' in command:  #Show from Wikipedia
        word = command.replace('search', '')
        info = wikipedia.summary(word, 3)
        print(info)
        talk(info)
    else:  #If the system did not listened the command
        print('Please say the command again.')
        talk('Please say the command again.')

while True:
    run_bhavya()
