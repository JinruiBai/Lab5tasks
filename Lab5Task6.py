class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def __add__(self, another):
        point = Point()
        if isinstance(another, Point):
            point.x = self.x + another.x
            point.y = self.y + another.y
            return point
        
        elif type(another) == tuple:
            point.x = self.x + another[0]
            point.y = self.y + another[1]
            return point
        
    def __radd__(self, other):
        return self.__add__(other)
    
    def __str__(self):
        return "(%s, %s)" % (self.x, self.y)
    
point1 = Point(2, 14)
point2 = Point(1, 3)
point_r = point1 + point2
tuple3 = (2, 3)
tuple_r = point1 + tuple3
print (point_r, tuple_r)

        
        