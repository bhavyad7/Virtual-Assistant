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

talk('hello my name is bhavya, how can i help you?')

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
    if 'play' in command:
        word_yt = command.replace('play', '')
        talk('playing' +word_yt)
        print('playing' +word_yt)
        pywhatkit.playonyt(word_yt)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print('Current time is ' +time)
        talk('Current time is ' +time)
    elif 'search' in command:
        word = command.replace('search', '')
        info = wikipedia.summary(word, 3)
        print(info)
        talk(info)
    else:
        print('Please say the command again.')
        talk('Please say the command again.')

while True:
    run_bhavya()
