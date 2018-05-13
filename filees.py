import os
import subprocess
import search_files as ser
import open_files as of
import show_files as sf
import win32com.client as wincl
speak = wincl.Dispatch("SAPI.SpVoice")

def fil_file(input):
    print(input)
    n1 = ser.fil_file_E(input)
    n2 = ser.fil_file_F(input)
    n3 = ser.fil_file_H(input)
    n = n1 + n2 + n3
    if n == 1:
        if n1 == 1:
            of.open_file_E(input)
        if n2 == 1:
            of.open_file_F(input)
        if n3 == 1:
            of.open_file_H(input)
    if n > 1:
        sf.show_file_E(input)
        sf.show_file_F(input)
        sf.show_file_H(input)
    if n == 0:
        speak.Speak('Sorry you Does not have such file in your device')








