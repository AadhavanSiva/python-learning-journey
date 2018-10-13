# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 19:15:15 2018

@author: Aadhavan
"""

StudentList = []
for i in  range(2):
    Student = int(input("Please Enter Your Student's Score:"))
    StudentList.append(Student)

StudentSet = set (StudentList)

print(StudentSet)

for score in StudentSet:
    if( score >= 90):
        print("A+")
    if( score < 90 and score >= 80):
        print("B+")
    if( score < 80 and score >= 70):
        print("C+")
    if( score < 70 and score >= 60):
        print("D+")
    if( score < 60 and score >= 50):
        print("E+")
    if( score < 50 and score >= 0):
        print("F+")
    

