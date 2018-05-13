from PyDictionary import PyDictionary
import win32com.client as wincl
def dict(input):
    a = input.rfind('define ')
    a += 7
    input1 = input[a:]
    input1 = input1.lower()
    speak = wincl.Dispatch("SAPI.SpVoice")
    dictionary = PyDictionary()
    print(dictionary.meaning("indentation"))
    speak.Speak(dictionary.meaning("indentation"))