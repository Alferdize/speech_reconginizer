import goslate
import win32com.client as wincl
from gtts import gTTS
import os
import translator as tra
import speech_recognition as sr
def translate(input1):
    speak = wincl.Dispatch("SAPI.SpVoice")
    r = sr.Recognizer()
    r.pause_threshold = 0.5
    r.energy_threshold = 3000
    with sr.Microphone() as source:
        print('speak')
        print('listening')
        audio = r.listen(source)
    try:
        a = input1.find('to ')
        a += 3
        input1 = input1[a:]
        #convert = input("Enter the words to speak")
        print('recognizing')
        print("You said " + r.recognize_google(audio))
        convert = r.recognize_google(audio)
        tra.trans(input1, convert)
    except sr.UnknownValueError:
        print("Could not understand")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

