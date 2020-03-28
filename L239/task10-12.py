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
            self.A = self.A/self.C
            self.B = self.B/self.C
            self.C = 1.0
        elif self.A != 0:
            self.B = self.B/self.A
            self.A = 1.0
            self.C = 0.0
        else:
            self.B = 1.0
            self.A = 0.0
            self.C = 0.0

    def parallelLine(self, point):
        return Line(-self.A, -self.B, (self.A*point.x + self.B*point.y)).normalize()

    def insideTreug(self, point):
        line1 = Line(0, 1, 0)
        line2 = Line(1, 0, 0)
        inter1 = self.intersection(line1)
        inter2 = self.intersection(line2)
        s1 = self.side(point)
        s2 = line1.side(point)
        s3 = line2.side(point)
        # print(inter1, inter2)
        # print(s1, s2, s3)
        if inter1.x > 0 and inter2.y > 0:
            if s1 == 'r' and s2 == 'l' and s3 == 'l':
                return "YES"
            else:
                return "NO"
        elif inter1.x < 0 and inter2.y > 0:
            if s1 == 'r' and s2 == 'l' and s3 == 'l':
                return "YES"
            else:
                return "NO"
        elif inter1.x < 0 and inter2.y < 0:
            if s1 == 'r' and s2 == 'r' and s3 == 'l':
                return "YES"
            else:
                return "NO"
        else:
            if s1 == 'l' and s2 == 'r' and s3 == 'r':
                return "YES"
            else:
                return "NO"


    @staticmethod
    def fromCoord(x1, y1, x2, y2):
        return Line(y1-y2, x2-x1, x1*y2-x2*y1)

line1 = Line.fromCoord(2, 0, 0, 2)
line2 = Line.fromCoord(2, 3, -5, 6)
point = Point(3, 3)
point2 = Point(0.25, 0.1)
# print(line1.normalize(), line1)
# print(line2.normalize())
# print(line2.nearPoint(point2))
# print(line2.oneSide(point, point2))
# print(line2.perpendicularLine(point))
# print(line1.insideTreug(point))
# print(line1.insideTreug(point2))
