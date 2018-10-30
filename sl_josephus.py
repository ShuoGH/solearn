# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 21:17:37 2018

@author: MagicAnn
"""

class Node():
#创建环形链表的各个节点       
    def __init__(self,value,next=None):
        self.value=value
        self.next=next
        
def createLink(num):
#根据节点创建环形链表
    root=Node(1)
    temp=root
    for i in range(num-1):
        temp.next=Node(i+2)
        temp=temp.next
    temp.next=root
    return root
   
def josephus(num,k):
    if(num==1):
        print("survive:",num)
        return
    root=createLink(num)
    temp=root
    
    while(1):
        for i in range(k-2):  #循环k-2次
            temp=temp.next 
            i+=1
        print("kill",temp.next.value)
        temp.next=temp.next.next #相当于跳过了下一个，也就是kill掉的node
        temp=temp.next
        if(temp.next==temp):
            break
        
    print("survive",temp.value)
        
a=int(input("请输入人数:"))
b=int(input("kill number:"))
josephus(a,b)            
            
    
    
    