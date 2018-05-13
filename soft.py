import os
import subprocess
def open_soft(input):
    if input.find('notepad') != -1:
        os.system('notepad.exe')
    if input.find('internet explorer') != -1 or input.find('browser') != -1 or input.find('web browser') != -1:
        subprocess.Popen(['C:\Program Files\Internet Explorer\\iexplore.exe'])
    if input.find('dolby') != -1:
        subprocess.Popen(['C:\Program Files\Dolby\Dolby DAX2\DAX2_APP\DolbyDAX2DesktopUI'])
    if input.find('pyCharm') != -1:
        subprocess.Popen(['C:\\Program Files\\JetBrains\\PyCharm 2017.2.3\\bin\\pycharm64.exe'])
    if input.find('firefox') != -1 or input.find('mozilla') != -1:
        subprocess.Popen(['C:\Program Files\Mozilla Firefox\\firefox.exe'])
