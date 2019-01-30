class Rectangle:
    def __init__(self, width, height, conrner):
        self.width = width
        self.height = height
        self.corner = conrner
        

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y



def find_center(rect):
    p = Point(0.0, 0.0)
    p.x = rect.corner.x + rect.width/2
    p.y = rect.corner.y + rect.height/2
    return p


def print_point(p):
    print('(%g, %g)' %(p.x, p.y))


def move_rectangle(rect1, dx, dy):
    
    x = rect1.corner.x + dx
    y = rect1.corner.y + dy
    p = Point(x, y)
    new_rect = Rectangle(rect1.width, rect1.height,p)
    return new_rect

def print_rectangle(rect):
    print('(%g, %g)' %(rect.width, rect.height))
    print(print_point(rect.corner))
    
corner = Point(0.0, 0.0)
box = Rectangle(100.0, 200.0, corner)

box1 = Rectangle(300.0, 500.0, corner)


center = find_center(box)
print(print_point(center))

new_rect = move_rectangle(box1, 430.0, 330.0)
print(print_rectangle(new_rect))