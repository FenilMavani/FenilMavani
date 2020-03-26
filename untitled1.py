#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 20:19:20 2020

@author: fenilmavani
"""
    



from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta



print(timedelta(days=365,hours=5,minutes=1))
now = datetime.now()

print("Today time : "+ str(now))



print("one year from now it will be: "+ str(now + timedelta(days=365)))

print("In 2 days and 3 weeks, it will be: "+ str(now + timedelta(days = 2 , weeks = 3)))



t = datetime.now() - timedelta(weeks=1)
s = t.strftime("%A %B %d, %Y")  

print("One week ago it was: "+s)


today = date.today()
afd = date(today.year, 4,1)


if afd<today:
    print("April fool day already gone by %d days"%((today-afd).days))
    afd = afd.replace(year = today.year+1)
    
time_to_afd = afd-today

print("It is just", time_to_afd, "days until April Fools Day")    