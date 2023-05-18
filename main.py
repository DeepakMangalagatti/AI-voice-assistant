import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import os
import webbrowser
import smtplib

engine=pyttsx3.init()
voices=engine.getProperty("voices")
# print(voices[0].id)
engine.setProperty("voices",voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wish_me():
    hour=int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Good Morning")

    elif hour>=12 and hour<18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak('''Hi I am David sir, Welcome to your productive sanctuary, where ideas take flight and accomplishments thrive, May your day be filled with focus, efficiency, and an abundance of inspiration
          How May I Help you ''')

def Take_Command():

   # IT TAKES INPUT FROM THE MICROPHONE AND RETURNS THE STRING
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold=1 # seconds of nonspeaking audio before a space is Considered  is complete
        audio=r.listen(source)

    try:
        print("Recognizing..........")
        query=r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again..!")
        return "None"

    return query

def sendmail(to,subject):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login("deepakmangalagatti1998@gmail.com","your password")
    server.sendmail("harry@gmail.com",to,subject)
    server.close()

if __name__ == '__main__':
    # speak("My name is deepak")
    wish_me()
    while True:
        query=Take_Command().lower()
    #logic for tasks executing based on query
        if 'wikipedia' in query:
             speak("Searching wikipedia........")
             query=query.replace("wikipedia","")
             results=wikipedia.summary(query,sentences=2)
             speak("According to wikipedia")
             print(results)
             speak(results)

        elif "youtube" in query:
            webbrowser.open("www.youtube.com")

        elif"google" in query:
            webbrowser.open("www.google.com")

        elif "mail" in query:
            try:
                print("what should i say....")
                speak("what should i say....")
                subject=Take_Command()
                to="deepakmangalagatti1998@gmail.com"
                sendmail(to,subject)
                print("E-mail has been sent....")
                speak("E-mail has been sent....")
            except Exception as e:
                print(e)
                print(" i am not able to send the mail")

        if "code" in query:
            path ="C:\\Program Files\\JetBrains\\PyCharm Community Edition 2023.1\\bin\\pycharm64.exe"
            os.path.exists(path)
            os.startfile(path)

        if "music" in query:
            path = "E:\\Rema, Selena Gomez - Calm Down (Official Music Video).mp3"
            os.path.exists(path)
            os.startfile(path)


