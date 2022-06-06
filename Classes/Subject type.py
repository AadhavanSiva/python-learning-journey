# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 16:18:43 2018

@author: Aadhavan
"""

class Subject:
    def __init__(self, name1, passMark, maxMark):
        self.name = name1
        self.passMark = passMark
        self.maxMark = maxMark
        self.average = 3
        
classSubject = Subject("science", ">= 70", " 70")
print("CLASS SUBJECT IS", classSubject.name)
print("THE PASS MARK IS", classSubject.passMark)
print("THE  MAX IS", classSubject.maxMark)
print("THE AVERAGE MARKS ARE", classSubject.average)