# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 19:19:28 2019

@author: Aadhavan
"""

#  1. import the connector 
import mysql.connector as conn

#2. Connect to database, host - machine where database runs
#       
mydb = conn.connect(  host="localhost",  user="root", passwd="REDACTED_DB_PASSWORD", 
                    database="python")

#3. Create cursor - to execute SQL ( Structured Query Language)
mycursor = mydb.cursor()

#4 Build the SQL and execute (insert sql)
sql = "SELECT * FROM movies"
mycursor.execute(sql)


#5.  Fetch the result and display
myresult = mycursor.fetchall()

for x in myresult:
  print(x)

  
mydb.close()
#print(mydb)