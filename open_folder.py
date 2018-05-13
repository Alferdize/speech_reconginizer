import webbrowser
import os

def open_folder_E(input):
    for root, dirs, files in os.walk('G:'):
        for name in dirs:
            name1 = name.lower()
            if name1.find(input) != -1:
                webbrowser.open(root + '\\' + name1)

def open_folder_F(input):
    for root, dirs, files in os.walk('F:'):
        for name in dirs:
            name1 = name.lower()
            if name1.find(input) != -1:
                webbrowser.open(root + '\\' + name1)

def open_folder_H(input):
    for root, dirs, files in os.walk('H:'):
        for name in dirs:
            name1 = name.lower()
            if name1.find(input) != -1:
                webbrowser.open(root + '\\' + name1)
