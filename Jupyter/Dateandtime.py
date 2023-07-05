import datetime as dt
import time as tm

tm.time()
dtnow = dt.datetime.fromtimestamp(tm.time())
print(dtnow)
dtnow = dt.datetime.fromtimestamp(tm.time())
print(dtnow)
dtnow.year, dtnow.month, dtnow.day, dtnow.hour, dtnow.minute, dtnow.second  # get year, month, day, etc.from a datetime
delta = dt.timedelta(days=100)  # create a timedelta of 100 days
print(delta)
today = dt.date.today()
print(today - delta)  # the date 100 days ago
print(today > today - delta)  # compare dates
