# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 22:50:17 2018

@author: MagicAnn
"""
import math
def calANum(num):
    temp=num
    NLen=0
    dig=[]
    s=0
    while(temp!=0):
        dig.append(temp%10)
        temp=temp//10
        NLen+=1
#        print(dig,NLen) #anchor
    for i in range(NLen):
        s+=pow(dig[i],NLen)
    return s
#def searchANum(low,high)
def searchANum(low,high):
    temp0=low+1
    anumList=[]
    while(temp0<=high):
        temp1=calANum(temp0)
        if(temp0==temp1):
            anumList.append(temp0)
        temp0+=1
    return anumList
    
def main():
    choose=input("check a number(type 'c') or search in a given num(type 's')? ")
    if(choose =='c'):
        num=int(input("please input the number you want to check: "))
        s=calANum(num)
        if(s==num):
            print(num,"is an armstrong num.")
        else:
            print("sorry,",num,"isn't a armstrong num.")
    
    elif(choose=='s'):
        low=int(input("please input the low number: "))
        high=int(input("please input the high number: "))
        anumList=searchANum(low,high)
        print("the list is:",anumList)     #其实应该加个判断，如果为空，返回说明
        
    else:
        print("sorry, please try again: ")
        main()
        
main()
        