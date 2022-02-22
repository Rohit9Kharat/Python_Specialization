'''
Created on 01-Jul-2020

@author: Rohit Kharat
'''
import re

fileName = input("Enter file name: ")
fileHandle = open(fileName)

listInt = list()
for line in fileHandle:
    strippedLine = line.rstrip()
    stuff = re.findall('[0-9]+',strippedLine)
    #print(stuff)
    if len(stuff) < 1:
        continue
    #print(stuff)
    for i in range(len(stuff)):
        num = int(stuff[i])
        listInt.append(num)
print(sum(listInt))   
    
    
        
    
        