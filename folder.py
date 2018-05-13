import search_folder as ser
import open_folder as of
import show_folder as sf
import win32com.client as wincl
def fil_folder(input):
    print(input)
    n1 = ser.fil_folder_E(input)
    n2 = ser.fil_folder_F(input)
    n3 = ser.fil_folder_H(input)
    n = n1 + n2 + n3
    if n == 1:
        if n1 == 1:
            of.open_folder_E(input)
        if n2 == 1:
            of.open_folder_F(input)
        if n3 == 1:
            of.open_folder_H(input)
    if n > 1:
        sf.show_folder_E(input)
        sf.show_folder_F(input)
        sf.show_folder_H(input)
    if n == 0:
        speak = wincl.Dispatch("SAPI.SpVoice")
        speak.Speak('Sorry you Does not have such folder in your device')
