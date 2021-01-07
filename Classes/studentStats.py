# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 21:22:01 2021

@author: Aadhavan
"""

class StudentStats:
  def __init__(self, student_id, attendence, grade, name):
    self.attendence = attendence
    self.grade = grade
    self.name = name
    self.student_id = student_id
    
  def print(self):
    print("The student id is ", self.student_id)
    print("The student's attendence for today is " + self.attendence)
    print("The student's name is " + self.name)
    print("The student's grade is " + self.grade)
        
  def attendence(self):
      if self.attendence == True:
          self.attendence= "present"
      else:
          self.attendence= "absent"
          
      
Class1 = StudentStats(1203, False, "7th", "Sharmila")
Class1.print()
Class1.absent()
Class1.attendence
