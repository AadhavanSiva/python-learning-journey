# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 19:55:28 2018

@author: Oviya
"""
import datetime

class School:
    def __init__(self,name,address):
        self.name = name;
        self.address = address

class Student:
    def __init__(self, name, grade, dateOfBirth, school):
        self.name = name;
        self.grade = grade;
        self.school = school;
    
class Teacher:
    def __init__(self, name, grade, school):
        self.name = name
        self.grade = grade
        self.school =school
        

middleSchool = School("Middle School", "45 Holliston street, Medway, MA")
elementarySchool = School("Elementry School", "7 cassidy street, Medway, MA")
student1 = Student("Aadhavan", "V", datetime.date(2007,10,30), middleSchool)

student2 = Student("Oviya", "V", datetime.date(2009,8,28), elementarySchool)
print(student2.name)
print(student1.name)
print(student1.grade)
print(student1.school.name)
print(student1.school.address)

teacher1 = Teacher("Che", "4", elementarySchool)
print(teacher1.name)

print(teacher1.school.name)

print(teacher1.school.address)
