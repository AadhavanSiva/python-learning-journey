# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 19:19:28 2019

@author: Aadhavan
"""

#  1. import the connector 
import mysql.connector as conn

#2. Connect to database
mydb = conn.connect(  host="localhost",  user="root", passwd="REDACTED_DB_PASSWORD", 
                    database="python")

#3. Create cursor - to execute SQL ( Structured Query Language)
mycursor = mydb.cursor()

#4 Build the SQL and values (insert sql)
#movies - table,  MovieId, MovieName.... columns
sql = "INSERT INTO movies (MovieId, MovieName, Year, Rating) VALUES (%s, %s, %s, %s)"
movieId = 8
movieName = "Finding Dory"
year = 2018
rating = 66
val = (movieId, movieName, year, rating)

#5.  Execute & Commit SQL
mycursor.execute(sql, val)

#6  Saving
mydb.commit()
  
#7 Close
mydb.close()
print("DONE")