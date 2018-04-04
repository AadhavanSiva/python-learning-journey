u# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 19:48:   
@author: Sharmila
"""

marks = []
marks.append(85)
marks.append(90)

marks.append(75)
marks.append(60)


    
#mark = int(input("Enter marks ( -1 Exit) "))
#while( mark != -1 ):
#    marks.append(mark);
#    mark = int(input("Enter marks ( -1 - Exit) "))
#    
index = 0
while (index < len(marks)):
    print (marks[index] )
    index += 1
    
    

marks.remove(100)

index = 0
while (index < len(marks)):
    print (marks[index] )
    index += 1
