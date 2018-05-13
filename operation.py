import fmusic as fm
import vvideo as vv
import win32com.client as wincl
def op_music(input):
    speak = wincl.Dispatch("SAPI.SpVoice")
    if input.find('music') != -1:
        a = input.find('music ')
        a += 6
        print(a)
        input1 = input[a:]
        input1 = input1.lower()
        speak.Speak("playing")
        fm.fil_music(input1)
    if input.find('video') != -1:

        a = input.rfind('video ')
        a += 6
        input1 = input[a:]
        input1 = input1.lower()
        speak.Speak("playing")
        vv.fil_video(input1)