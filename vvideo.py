import no_of as nom
import play as pl
import show as sm
import win32com.client as wincl

def fil_video(input):
    video_type = ['.webm', '.mkv', '.flv', '.vob', '.ogv', '.ogg', '.drc', '.gif', '.gifv', '.mng', '.avi', '.mov',
                  '.qt', '.wmv', '.yuv', '.rm', '.rmvb', '.asf', '.amv', '.mp4', '.m4p', '.m4v', '.mpg', '.mpeg',
                  '.m2v', '.svi', '.3gp', '.3g2', '.mxf', '.rop', '.nsv', '.f4a']
    speak = wincl.Dispatch("SAPI.SpVoice")
    n1 = nom.no_E(input,video_type)
    n2 = nom.no_F(input,video_type)
    n3 = nom.no_H(input,video_type)
    n = n1 + n2 + n3
    if n == 1:
        if n1 == 1:
            pl.play_E(input,video_type)
        if n2 == 1:
            pl.play_F(input,video_type)
        if n3 == 1:
            pl.play_H(input,video_type)
    if n > 1:
        sm.show_E(input,video_type)
        sm.show_F(input,video_type)
        sm.show_H(input,video_type)
    if n == 0:
        speak.Speak('Sorry you Does not have such file in your device')
