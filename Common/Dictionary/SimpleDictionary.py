# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 17:48:26 2019

@author: Oviya
"""

#names = ["oscar", "brody"]
#ages = [2, 5]
#print( names[1] )
#print( ages[0] )
MLB_teams = {
        'Boston'   : 'Red Sox',
        "Colorado" : 'Rockies',
        'Newyork City':'Yankees',
        'Newyork State':'Mets'}

city_population = {
        "Boston": 15000000,
        "Medway": 15000,
        "Franklin":25000
        }


fourth_grade_students = {
        10: "Sharon",
        25: "John",
        3: "Kelly"
        }
for student_age in fourth_grade_students:
    print("Age of student", student_age, "  Name of student", fourth_grade_students[student_age])
    
#print("First value of MLB_teams", MLB_teams["Boston"])
##city_state_name = "Virginia State"
##if( city_state_name in MLB_teams):
##    team_name = MLB_teams[city_state_name]
##    print(team_name)
##else:
##    print(city_state_name, " is not in the MLB teams")
##
##city_name = "millis"
##if ( city_name not in city_population):
##    print(city_name, " is not in the city population")
##else:
##    print("Population of ", city_name, " is ", city_population[city_name])
#
##print entire dictionary
#print("To print entire dictionary",MLB_teams)
#print( "Keys =>", MLB_teams.keys() )
#print( "Values =>",list( MLB_teams.values() ) )
#
#print("To print entire dictionary one by one")
for city_name in MLB_teams:
    print("key name ", city_name, ", Value (city_name)  : ", MLB_teams[city_name])

print (city_population.keys())
print (city_population.values())
for city in city_population:
    print("City : ", city, ", Population : ", city_population[city])
#    
    
#for number in fourth_grade_students:
#    print( "Student number :", number,", ", "name :",  fourth_grade_students[number])

    #  Student number : <>, name : <
    