# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 19:41:03 2020

@author: Aadhavan
"""

import time
#
#print(time.time())
#
#def lots_of_numbers(max):
#    for x in range(0,max):
#        print(x)
#        
#lots_of_numbers(1000)
#
#def lots_of_numbers(max):
#    t1 = time.time()
#    for x in range(0,max):
#        #print(x)
#        c = 666*778
#    t2 = time.time()
#    print('it took %s seconds to print' % (t2-t1))
#        
#lots_of_numbers(98109000)

#print("current time =>",time.asctime())
#
#t = (2007,10,30,10,30,48,1,1,2)
#print(time.asctime(t))
#
#print(time.localtime())

t = (2007,10,30,10,30,48,1,1,2)
print(time.asctime())
t = time.localtime()
print(t)
year = t[0]
month = t[1]
print("current year",year,"current month",month)

#for x in range(1,61):
#    print(x)
#    time.sleep(1)