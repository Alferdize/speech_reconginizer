import no_of as nom
import play as pl
import show as sm
import win32com.client as wincl


def fil_music(input):
    speak = wincl.Dispatch("SAPI.SpVoice")
    music_type = ['.3gp', '.aa', '.aac', '.aax', '.act', '.aiff', '.amr', '.ape', '.au', '.awb', '.dct', '.dss', 'dvf',
                  '.flac', '.gsm', '.iklax', '.ivs', '.m4a', '.m4b', '.m4p', '.mmf', '.mp3', '.mpc', '.msv', '.ogg',
                  '.opus', '.ra', '.rm', '.raw', '.sln', '.tta', '.vox', '.wav', '.wma', '.wv', '.webm', '.8svx']
    print(input)
    n1 = nom.no_E(input,music_type)
    n2 = nom.no_F(input,music_type)
    n3 = nom.no_H(input,music_type)
    n = n1 + n2 + n3
    if n == 1:
        if n1 == 1:
            pl.play_E(input,music_type)
        if n2 == 1:
            pl.play_F(input,music_type)
        if n3 == 1:
            pl.play_H(input,music_type)
    if n > 1:
        sm.show_E(input,music_type)
        sm.show_F(input,music_type)
        sm.show_H(input,music_type)
    if n == 0:
        speak.Speak('Sorry you Does not have such file in your device')
