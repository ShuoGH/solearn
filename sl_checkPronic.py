# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 13:08:22 2018

@author: MagicAnn
"""
import math
def checkPronic(num):
    che_Num=int(math.sqrt(num))
    if(num==che_Num * (che_Num+1)):
        print("is a pronic.\n")
    else:
        print("is not a pronic.\n")
        
def input_Check():
    a=int(input("please enter your number:"))
    checkPronic(a)
    
    ch=input("another check(Y for another check/ N or any other letter for quit)?\n")
    if(ch=='Y' or ch=='y'):
        input_Check()
    else:
        print("ok,quit")
input_Check()

    