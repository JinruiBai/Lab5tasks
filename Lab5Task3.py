class Time:
    def __init__(self, h, m, s):
        self.h = h
        self.m = m
        self.s = s
        
def print_time(t):
    a = '(%.2d:%.2d:%.2d)' % (t.h, t.m, t.s)
    return a
    
time = Time(11, 29, 40)
print(print_time(time))
