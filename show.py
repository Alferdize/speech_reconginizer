import os
def show_E(input,m_v_type):
    cnt = 0
    for root, dirs, files in os.walk('G:'):
        for name in files:
            name1 = name.lower()
            for type in m_v_type:
                if name1.find(type) != -1 and name1.find(input) != -1:
                    print(root + '\\' + name)


def show_F(input,m_v_type):
    cnt = 0
    b = input.find('.')
    input1 = input[b:]
    for root, dirs, files in os.walk('F:'):
        for name in files:
            name1 = name.lower()
            for type in m_v_type:
                if name1.find(type) != -1 and name1.find(input) != -1:
                    print(root + '\\' + name)

def show_H(input,m_v_type):
    cnt = 0
    b = input.find('.')
    input1 = input[b:]
    for root, dirs, files in os.walk('H:'):
        for name in files:
            name1 = name.lower()
            for type in m_v_type:
                if name1.find(type) != -1 and name1.find(input)  != -1:
                    print(root + '\\' + name)
