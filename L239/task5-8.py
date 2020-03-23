import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '({:.2f}, {:.2f})'.format(self.x, self.y)

    def distanceTo(self, point):
        return math.sqrt((self.x - point.x)**2 + (self.y - point.y)**2)


class Line:
    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C
        self.x1 = 0
        self.x2 = 1
        if B != 0:
            self.y1 = -self.C/self.B
            self.y2 = (-self.C - self.A)/self.B
        else:
            self.y1 = -self.C
            self.y2 = -self.C - self.A
    def __str__(self):
        if self.A > 0:
            a = '{:.2f}'.format(self.A)
        else:
            a = '-{:.2f}'.format(abs(self.A))

        if self.B > 0:
            b = '+ {:.2f}'.format(self.B)
        else:
            b = '- {:.2f}'.format(abs(self.B))

        if self.C > 0:
            c = '+ {:.2f}'.format(self.C)
        else:
            c = '- {:.2f}'.format(abs(self.C))

        return '{}x {}y {} = 0'.format(a, b, c)


    def distanceToZero(self):
        d = math.sqrt(self.A*self.A + self.B*self.B)
        if d == 0:
            return 0
        else:
            return abs(self.C)/math.sqrt(self.A*self.A + self.B*self.B)

    def distanceToPoint(self, point):
        d = math.sqrt(self.A*self.A + self.B*self.B)
        if d == 0:
            return 0
        else:
            return abs(self.A*point.x + self.B*point.y + self.C)/d

    def isParallel(self, line):
        if abs(self.A*line.B - self.B*line.A) <= 0.001:
            return True
        else:
            return False

    def intersection(self, line):
        if not self.isParallel(line):
            det1 = self.B * line.C - self.C * line.B
            det2 = self.C * line.A - self.A * line.C
            det = self.A * line.B - self.B * line.A
            return Point(det1/det, det2/det)
        else:
            return 'NO'

    def perpendicular(self, point):
        a = -1
        b = (self.y1 - self.y2)
        c = (point.x - b*point.y)
        return Line(a, b, c)

    def nearPoint(self, point):
        return self.intersection(self.perpendicular(point))

    @staticmethod
    def fromCoord(x1, y1, x2, y2):
        return Line(y1-y2, x2-x1, x1*y2-x2*y1)

line = Line.fromCoord(1, 0, 0, 1)
point = Point(3, 4)
# print(line)
# print(line.distanceToPoint(point))
line1 = Line.fromCoord(0, 1, 1, 0)
line2 = Line.fromCoord(5, 0, 0, 5)
# print(line1.isParallel(line2))
# print(line1.intersection(line2))
print(line1.nearPoint(point))
