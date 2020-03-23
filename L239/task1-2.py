import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '({:.2f}, {:.2f})'.format(self.x, self.y)
    def distanceTo(self, point):
        return math.sqrt((self.x - point.x)**2 + (self.y - point.y)**2)
p = Point(2.34, 5.67)
print ("%.2f" % p.x)
print ("%.2f" % p.y)
point = Point(-18.5, 13.5)
print(point)
print(p.distanceTo(point))
