import os
import subprocess
def fil_folder_E(input):
    cnt = 0
    for root, dirs, files in os.walk('G:'):
        for name in dirs:
            name1 = name.lower()
            if name1.find(input) != -1:
                cnt += 1
    return cnt

def fil_folder_F(input):
    cnt = 0
    for root, dirs, files in os.walk('F:'):
        for name in dirs:
            name1 = name.lower()
            if name1.find(input) != -1:
                cnt += 1
    return cnt

def fil_folder_H(input):
    cnt = 0
    for root, dirs, files in os.walk('H:'):
        for name in dirs:
            name1 = name.lower()
            if name1.find(input) != -1:
                cnt += 1
    return cnt

