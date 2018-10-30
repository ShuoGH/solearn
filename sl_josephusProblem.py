# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 17:13:54 2018

@author: MagicAnn
"""

def outputPeople(people):
        print(people,'\n')
        
def sword(people,n):
    if(len(people)==1):
        print("No more people can kill.\nThe last person is No.",people[0])
    elif(n==len(people)-1):
        print(people[n],"kills",people[0]," Sword:",people[1])
        del people[0]
        outputPeople(people)
        sword(people,0)
        
    elif(n==len(people)-2):
        print(people[-2],"kills",people[-1]," Sword:",people[0])
        del people[-1]   #kill the last one
        outputPeople(people)
        sword(people,0)   #begin from the first again
        
    else:
        n+=1
        print(people[n-1],"kills",people[n]," Sword:",people[n+1])
        del people[n]
        outputPeople(people)
        sword(people,n)
        
def jesephusProblem():
    num=int(input("please input a number of people:"))
    p=[]
    i=0
    while(i<num):
        p.append(i+1)
 #       print("this is ",p[i])
        i+=1

    sword(p,0)   #two, first is list, second is beginning num.
    
jesephusProblem()
