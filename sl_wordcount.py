# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 17:00:40 2018

@author: ChrisIrving
"""
def mainF():
    string=input("please input your string: ")
    word=input("please input the cut word: ")
    string=str.upper(string)  #string.upper() 也一样是对的。
    word=str.upper(word)    #word.upper()
    
    result=wordCount(string)
    print(result)
    print("the frequency of "+word+" is",result[word])

def wordCount(str1): #add function to count
    wordList=str1.split(" ")
    dic={}
    for w in wordList:
        if w:
            if w in dic.keys():
                dic[w]+=1
            else:
                dic[w]=1
    return dic
    
mainF()
