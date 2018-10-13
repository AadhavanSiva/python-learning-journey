# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 19:15:15 2018

@author: Aadhavan
"""

StudentDictionary = []
StudentScore =[]
for i in  range(1):
    StudentName = (input("Please Enter Your Student's Name"))
    Student = int(input("Please Enter Your Student's Score:"))
    StudentDictionary.append(StudentName)
    StudentScore.append(Student)
for Student in StudentScore:
    if Student in StudentScore:
        print("not working")
        StudentScore[Student]
    else:
        print("working")
        StudentScore[Student]

    
print(StudentDictionary)



