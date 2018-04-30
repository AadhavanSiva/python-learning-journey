# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 20:31:02 2018

@author: Sharmila
"""

teacherName = input("please enter a name")
teacherGrade = input("please enter a grade")

teachersFile = open("teacherNameAndGrade","a")

teachersFile.write(teacherName)
teachersFile.write(",")
teachersFile.write(teacherGrade)
teachersFile.write("\n")

teachersFile.close();