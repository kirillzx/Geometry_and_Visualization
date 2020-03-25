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
        elif self.C<0:
            c = '- {:.2f}'.format(abs(self.C))
        else:
            c = '+ {:.2f}'.format(abs(self.C))

        return '{}x {}y {} = 0'.format(a, b, c)


    def distanceToZero(self):
        d = math.sqrt(self.A*self.A + self.B*self.B)
        if d == 0:
            return 0
        else:
            return abs(self.C)/d

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

    def perpendicularLine(self, point):
        a_new = self.B/self.A
        c_new = (self.B/self.A)*point.x - point.y
        return Line(a_new, -1, -c_new)

    def nearPoint(self, point):
        a_new = -self.B/self.A
        b_new = 1
        c_new = (self.B/self.A)*point.x - point.y
        p = Line(a_new, b_new, c_new)
        return self.intersection(p)

    def side(self, point):
        side = self.A*point.x + self.B*point.y + self.C
        if abs(side) < 0.001:
            return 'on'
        elif side > 0:
            return 'l'
        else:
            return 'r'

    def oneSide(self, point1, point2):
        m1 = self.side(point1)
        m2 = self.side(point2)
        if (m1, m2) == ('r', 'r') or (m1, m2) == ('l', 'l'):
            return True
        elif (m1, m2) == ('r', 'l') or (m1, m2) == ('l', 'r'):
            return False
        else:
            return True

    def normalize(self):
        if self.C != 0:
            return Line(self.A/self.C, self.B/self.C, 1)
        elif self.A != 0:
            return Line(1, self.B/self.A, self.C/self.A)
        else:
            return Line(self.A/self.B, 1, self.C/self.B)

    def parallelLine(self, point):
        return Line(-self.A, -self.B, (self.A*point.x + self.B*point.y)).normalize()

    @staticmethod
    def fromCoord(x1, y1, x2, y2):
        return Line(y1-y2, x2-x1, x1*y2-x2*y1)

line1 = Line.fromCoord(0, 1, 1, 0)
line2 = Line.fromCoord(1, 0, 0, 1)
point = Point(2, 3)
point2 = Point(-6, -0.9999)
# print(line2.nearPoint(point2))
# print(line2.oneSide(point, point2))
print(line2.perpendicularLine(point))
