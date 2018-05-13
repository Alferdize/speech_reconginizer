import filees as fil
import folder as fol
import soft as sof
import win32com.client as wincl

speak = wincl.Dispatch("SAPI.SpVoice")

def fil_search(input):
    if input.find('file') != -1:
        a = input.find('file ')
        a += 5
        print(a)
        input1 = input[a:]
        input1 = input1.lower()
        fil.fil_file(input1)
    if input.find('folder') != -1:
        a = input.rfind('folder ')
        a += 7
        input1 = input[a:]
        input1 = input1.lower()
        fol.fil_folder(input1)
    if input.find('file') == -1 and input.find('folder') == -1:
        a = input.rfind('open ')
        a += 5
        input1 = input[a:]
        input1 = input1.lower()
        speak.Speak('opening')
        sof.open_soft(input)


