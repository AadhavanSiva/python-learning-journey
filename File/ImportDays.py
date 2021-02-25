from datetime import *


def getWeekday(date1):
    days = ["Monday","Tuesday","Wednesday","Thrusday","Friday","Saturday","Sunday"]
    return days[date1.weekday()]
 

def list_file_content(file_name):
    with open(file_name) as file:
        for line in file:
            line = line.rstrip("\n")
            current_event = line.split(",")
#            print(current_event[0])
            event_date = datetime.strptime(current_event[1], '%m/%d/%y').date()
#            print(event_date - date.today())
##            daysBetween= str(event_date- date.today())
#            print(event_date, date.today())
            print(current_event[0],days_between_dates(event_date, date.today()))
            
            
def days_between_dates(date1, date2):
    time_between = str(date1 - date2)      
    number_of_days = time_between.split(',')
    return number_of_days[0]


# aadhavanBirthday: date = date(2009, 10, 30)
#newDate = date.__new__(2021)
#print(newDate)
#aadhavanBirthday = date(2007, 10, 30)
list_file_content("dates.txt")

print()
#
#oviyaBirthday = date(2009, 8, 28)
#sivaBirthday = date (1975, 3, 9)
#print(getWeekday(oviyaBirthday))
#print(date.today())
#halloween = date(2021,10,30)
#current_date = date.today()
#print(halloween - current_date)

#print(oviyaBirthday - aadhavanBirthday)
#print(aadhavanBirthday - oviyaBirthday )
#result = getWeekday(aadhavanBirthday)
#print(result)
#print(list_file_content - current_date)
#print(oviyaBirthday)
#print( oviyaBirthday.weekday() )

#print(oviyaBirthday)



#print(oviyaBirthday - aadhavanBirthday)
#print(aadhavanBirthday - oviyaBirthday)

#number_of_days = oviyaBirthday - aadhavanBirthday

# Output
# Halloween 200 days
# Christmas 230 days
# New year 235 days