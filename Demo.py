# !/usr/bin python3                                 
# encoding   :   utf-8 -*-                            
# author     :   浮川                              
# File       :   Demo.py
# Date       :   2021/6/24 10:34


import random
def Unicode():
    a = []
    for i in range(500):
        val = random.randint(0x4e00, 0x9fbf)
        a.append(chr(val))
    return a


a = Unicode()
print(a)
b = [str(j) for j in a]
str2 = ''.join(b)
print(str2)
