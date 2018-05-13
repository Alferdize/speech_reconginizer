import open as opn
from time import ctime
import time
from tkinter import *
import speech_recognition as sr
from pygame import mixer
import pyperclip
import threading
import translation as trans
import operation as pm
import dictionary_tref as dct
#import win32com.client as wincl
import webbrowser
from tkinter import *
from tkinter import ttk
import webbrowser
import speech_recognition as sr
from pygame import mixer

root = Tk()
root.title('Universal Search Bar')
root.iconbitmap('mic.ico')

style = ttk.Style()
style.theme_use('winnative')

photo = PhotoImage(file='microphone.png').subsample(15,15)

label1 = ttk.Label(root, text='Query:')
label1.grid(row=0, column=0)
entry1 = ttk.Entry(root, width=40)
entry1.grid(row=0, column=1, columnspan=4)

btn2 = StringVar()

def callback():
    '''print('recognizing')
    print("You said " + r.recognize_google(audio))#conversion
    input = r.recognize_google(audio)
    #input=input('Enter your command')
    '''
    print("You said " +input)
    input = entry1.get()
    input = input.lower()
    if input.find('open') != -1:
        opn.fil_search(input)
    elif input.find('play') != -1 or input.find('play') != -1:
        pm.op_music(input)
    elif input.find('translate') != -1:
        trans.translate(input)
    elif input.find('define') != -1:
        dct.dict(input)
    elif input.find('time') != -1:
        print(ctime())
        speak.Speak(ctime())
    else:
        pass

def get(event):
    '''print('recognizing')
    print("You said " + r.recognize_google(audio))#conversion
    '''
    input = entry1.get()
    #input=input('Enter your command')
    input = input.lower()
    if input.find('open') != -1:
        opn.fil_search(input)
    elif input.find('play') != -1 or input.find('play') != -1:
        pm.op_music(input)
    elif input.find('translate') != -1:
        trans.translate(input)
    elif input.find('define') != -1:
        dct.dict(input)
    elif input.find('time') != -1:
        print(ctime())
    elif input.find('google') != -1:
        webbrowser.open('http://google.com/search?q='+entry1.get())
    elif input.find('youtub') != -1:
        webbrowser.open('https://www.youtube.com/results?search_query='+entry1.get())
    else:
        pass


   

def buttonClick():

    mixer.init()
    mixer.music.load('chime1.mp3')
    mixer.music.play()

    r = sr.Recognizer()
    r.pause_threshold = 0.5
    r.energy_threshold = 4500

    with sr.Microphone() as source:
        audio = r.listen(source, timeout=5)
    try:
        input = str(r.recognize_google(audio))
        input = input.lower()
        if input.find('open') != -1 :
            opn.fil_search(input)
        if input.find('play') != -1 or input.find('play') != -1:
            pm.op_music(input)
        if input.find('translate') != -1:
            trans.translate(input)
        if input.find('define') != -1:
            dct.dict(input)
        if input.find('time') != -1:
            print(ctime())
        if input.find('google') != -1:
            webbrowser.open('http://google.com/search?q='+input)
        if input.find('google') != -1:
            webbrowser.open('https://www.youtube.com/results?search_query='+input)
    except sr.UnknownValueError:
            print('Google Speech Recognition could not understand audio')

    except sr.RequestError as e:
            print('Could not request results from Google Speech Recognition Service')

    else:
        pass
entry1.bind('<Return>', get)

MyButton1 = ttk.Button(root, text='Search', width=10, command=callback)
MyButton1.grid(row=0, column=6)

MyButton6 = Button(root, image=photo, command=buttonClick, bd=0, activebackground='#c1bfbf', overrelief='groove', relief='sunken')
MyButton6.grid(row=0, column=5)

entry1.focus()
root.wm_attributes('-topmost', 1)
btn2.set('google')
root.mainloop()
