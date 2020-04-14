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
        elif self.A<0:
            a = '-{:.2f}'.format(abs(self.A))
        else:
            a = '{:.2f}'.format(abs(self.A))

        if self.B > 0:
            b = '+ {:.2f}'.format(self.B)
        elif self.B<0:
            b = '- {:.2f}'.format(abs(self.B))
        else:
            b = '+ {:.2f}'.format(abs(self.B))


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
        A = -1
        if self.B != 0:
            B = self.A / self.B
        else:
            B = self.B
        C = point.x - B*point.y
        return Line(-A, -B, -C)

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
            self.A = self.A / self.C
            self.B = self.B / self.C
            self.C = 1
        elif self.A != 0:
            self.A = 1
            self.B = self.B / self.A
            self.C = 0
        else:
            self.A = 0
            self.B = 1
            self.C = 0


    def parallelLine(self, point):
        return Line(-self.A, -self.B, (self.A*point.x + self.B*point.y)).normalize()

    def insideTreug(self, point):
        if (self.A == 0) or (self.B == 0):
            return "NO"
        else:
            axis_x = Line.fromCoord(0,0,1,0)
            axis_y = Line.fromCoord(0,0,0,1)

            int_a_x = self.intersection(axis_x)
            int_b_y = self.intersection(axis_y)
            int_c = axis_x.intersection(axis_y)

            new_a = (int_a_x.x - point.x) * (int_b_y.y - int_a_x.y) - (int_b_y.x - int_a_x.x) * (int_a_x.y - point.y)
            new_b = (int_b_y.x - point.x) * (int_c.y - int_b_y.y) - (int_c.x - int_b_y.x) * (int_b_y.y - point.y)
            new_c = (int_c.x - point.x) * (int_a_x.y - int_c.y) - (int_a_x.x - int_c.x)*(int_c.y - point.y)

            sign = lambda a: 1 if a>0 else -1 if a<0 else 0
            if sign(new_a) == sign(new_b) == sign(new_c):
                return "YES"
            else:
                return "NO"


    @staticmethod
    def fromCoord(x1, y1, x2, y2):
        return Line(y1-y2, x2-x1, x1*y2-x2*y1)

line1 = Line.fromCoord(-3, 3, 4.5, -4.5)
line2 = Line.fromCoord(2, 3, -5, 6)
point = Point(3, 3)
point2 = Point(0.25, 0.1)
print(line1)
print(line1.normalize(), line1)
# print(line2.normalize())
# print(line2.nearPoint(point2))
# print(line2.oneSide(point, point2))
# print(line2.perpendicularLine(point))
print(line1.insideTreug(point))
# print(line1.insideTreug(point2))
