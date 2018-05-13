import os

def show_file_E(input):
    b = input.find('.')
    input1 = input[b:]
    for root, dirs, files in os.walk('G:'):
        for name in files:
            name1 = name.lower()
            if name1.find(input) != -1 and name1.find(input1):
                print(root + '\\' + name)


def show_file_H(input):
    b = input.find('.')
    input1 = input[b:]
    for root, dirs, files in os.walk('H:'):
        for name in files:
            name1 = name.lower()
            if name1.find(input) != -1 and name1.find(input1):
                print(root + '\\' + name)


def show_file_F(input):
    b = input.find('.')
    input1 = input[b:]
    for root, dirs, files in os.walk('F:'):
        for name in files:
            name1 = name.lower()
            if name1.find(input) != -1 and name1.find(input1):
                print(root + '\\' + name)

