import os
def fil_file_E(input):
    cnt = 0
    b = input.find('.')
    input1 = input[b:]
    for root, dirs, files in os.walk('G:'):
        for name in files:
            name1 = name.lower()
            if name1.find(input) != -1 and name1.find(input1):
                cnt = cnt + 1
    return cnt

def fil_file_F(input):
    cnt = 0
    b = input.find('.')
    input1 = input[b:]
    for root, dirs, files in os.walk('F:'):
        for name in files:
            name1 = name.lower()
            if name1.find(input) != -1 and name1.find(input1):
                cnt = cnt + 1
    return cnt
def fil_file_H(input):
    cnt = 0
    b = input.find('.')
    input1 = input[b:]
    for root, dirs, files in os.walk('H:'):
        for name in files:
            name1 = name.lower()
            if name1.find(input) != -1 and name1.find(input1):
                cnt = cnt + 1
    return cnt

