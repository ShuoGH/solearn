# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 11:26:48 2018

@author: MagicAnn
"""

def NonInte_base(decimal,base):
    tempList=[]
    temp=decimal
    while(temp >= base):
#        print("fuck")
        ex=temp%base
        print(ex)
        if(ex>9):
            tempList.append(chr(65+(ex-10)))
            print(ex)
        tempList.append(ex)
        temp=decimal//base
        print(temp)
    tempList.append(temp)
    tempList.reverse()

    numBase= ''.join(map(str,tempList))
    print(numBase)
        
a=int(input("请输入要转换的十进制数字:"))
b=int(input("请输入要转换的进制:"))
print(type(a),type(b))
NonInte_base(a,b)