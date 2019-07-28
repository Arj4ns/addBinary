# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 15:33:51 2019

@author: Arjan
"""

def addBinary(a, b):
    result = ""
    carry = 0
    
    while len(b) > len(a):
        a = "0" + a
        
    while len(a) > len(b):
        b = "0" + b
        
    for j in range(len(a) - 1, -1, -1):
        if int(a[j]) + int(b[j]) + carry == 0:
            result = "0" + result
            carry = 0
        elif int(a[j]) + int(b[j]) + carry == 1:
            result = "1" + result
            carry = 0
        elif int(a[j]) + int(b[j]) + carry == 2:
            result = "0" + result
            carry = 1
        elif int(a[j]) + int(b[j]) + carry == 3:
            result = "1" + result
            carry = 1
    if carry != 0:
        result = str(carry) + result
    return result

print(addBinary("1010", "1011"))