import pywhatkit
import os
import speech_recognition as sr
import pyttsx3

# engine = pyttsx3.init('sapi5')
# voices = engine.getProperty('voices')
# engine.setProperty('voices',voices[0].id)

# def Speak(audio):
#     print(" ")
#     print(f": {audio}")
#     engine.say(audio)
#     engine.runAndWait()

def TakeCommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:

        print(": Listening....")

        r.pause_threshold = 1

        audio = r.listen(source)

        print(": Recognizing...")

        query = r.recognize_google(audio,language='en-in')

        print(f": Your Command : {query}\n")

    oooooo =open('E:\\PROGRAMS\\project\\JARVISYT\\Text.txt','a')
    oooooo.write("\n")
    # oooooo.write(f"  {audio}")
    oooooo.write(f"  {query}")
    oooooo.close()

TakeCommand()