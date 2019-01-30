import math
class Point:
	def __init__(self,x,y):
		self.x = x
		self.y = y

p1 = Point(2, 4)
p2 = Point(5, 5)

def distance_between_points(p1, p2):
	dis = math.sqrt((p1.x - p2.x) **2 + (p1.y - p2.y) **2)
	return dis
print("The distance is: " + str(distance_between_points(p1, p2)))
