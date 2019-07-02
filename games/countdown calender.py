from tkinter import Tk, Canvas
from datetime import date, datetime
def get_events():
    list_events = []
    with open('events.txt') as file:
        for line in file:
            line = line.rstrip('\n')
            current_event = line.split(',')
            event_date  = datetime.strptime(current_event[1], '%d/%m/%y').date()
            current_event = event_date 
            list_events.append(current_event)
    return list_events
root = Tk()
c = Canvas(root, width=800, height=800, bg='black' )
c.pack()
c.create_text(100, 50, anchor='w', fill ='orange', font='Arial 28 bold underline', text='My countdown calender')
vertical_space = 100
events = get_events()
for event in events:
    events_name = events[0]
    day_until = days_between_dates(events[1], today)
    display ='it is %s days until %s' % (day_until, events_name)
    c.create_text(100, verticle_space, anchor='w', fill ='light blue ', font='Arial 28 bold ', text= disaplay)
    verticle_space += 30
events = get_events()
today = date.today()

def days_between_dates(date1, date2):
    time_between = str(date1 - date2)
    number_of_days = time_between.split('')
    return number_of_days[0]
