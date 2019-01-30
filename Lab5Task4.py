import time
import datetime

class Time(object):
    def __init__(self, year=2018, month=4, day=28, hour=12, minute=0, sec=0):
        self.date = datetime.datetime(year, month, day, hour, minute, sec)
    
    
    def mktime(self):
        return time.mktime(self.date.timetuple())
        
        
t1 = Time(2019, 1, 20, 10)
t2 = Time(2019, 2, 01, 1)

def is_after(time1, time2):
    return time1.mktime() > time2.mktime()
    
print (is_after(t1, t2))