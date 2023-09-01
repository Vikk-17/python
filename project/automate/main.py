#!/usr/bin/env python3

from features import *
import webbrowser
import wikipedia
import os


if __name__ == '__main__':
    speaker()
    speak("Wait a second i am initiating")
    wishme()
    
    while True:
        query = takecommand().lower()

        if 'wikipedia' in query:
            speak("Searching wikipedia . . .")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to wikipedia . . .")
            print(results)
            speak(results)
        
        elif 'break' in query:
            break
        
        elif 'open youtube' in query:
            webbrowser.open(URL[0])
        
        elif 'open google' in query:
            webbrowser.open(URL[1])
        
        elif 'open python docs' in query:
            webbrowser.open(URL[2])

        # elif 'play music' in query:
        #     music_dir = "NONE"
        #     songs = os.listdir(music_dir)
        #     print(songs)
        #     os.startfile(os.path.join(music_dir, songs[0]))
        #     pass

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Current time is {strTime}")
            speak(f"Sir the time is {strTime}")
        
        elif 'open code' in query:
            codePath =  "C:\\Users\\HEISENBERG\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'send email' in query:
            try:
                speak('to whom?')
                reciver = takecommand().lower()
                speak('what should I say?')
                text_to_send = takecommand().lower()
                speak(f'sending email to {reciver}')
                sendmail(contact[reciver], text_to_send)
                speak(f"I have successfully send mail to {reciver}")
            except Exception as e:
                speak("Sorry unable to send the email.")