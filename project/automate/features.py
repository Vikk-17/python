import pyttsx3
import speech_recognition as sr


import datetime
import smtplib
from credentials import *
from data import contact 

engine = pyttsx3.init('sapi5')



x = datetime.datetime.now()
hr = x.hour

URL = ['https://www.youtube.com/', 'https://www.google.com/', 'https://www.python.org/']

def wishme():
    if hr >= 0 and hr < 12:
        speak("Morning Sir!")
    elif hr >= 12 and hr < 18:
        speak("Afternoon Sir!")
    else:
        speak("Night Sir!")

def speaker():
    '''Properties of the speaker'''
    # Getting properties
    volume = engine.getProperty('volume')
    rate = engine.getProperty('rate')
    voices = engine.getProperty('voices')

    # Setting properties
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 170)
    engine.setProperty('volume', volume+1.0)
    
    engine.say("Hi, I am Lex.")

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takecommand():
    '''It takes microphone input from the user and returns string output'''

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening . . .")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing . . .")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")
    
    except Exception as e:
        # print(e)
        print("Say that again please . . .")
        return "NONE"
    return query


def sendmail(sendto, content):

    sender = data_email['gmail']
    sender_password = data_email['password']
    # reciver = recivers[0]
    # content = 'Testing the SMTPLIB'

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(sender, sender_password)
    server.sendmail(sender, sendto, content)
    server.close()