import math
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
        else:
            c = '- {:.2f}'.format(abs(self.C))

        return '{}x {}y {} = 0'.format(a, b, c)

    @staticmethod
    def fromCoord(x1, y1, x2, y2):
        return Line(y1-y2, x2-x1, x1*y2-x2*y1)
    def distanceToZero(self):
        d = math.sqrt(self.A*self.A + self.B*self.B)
        if d == 0:
            return 0
        else:    
            return abs(self.C)/math.sqrt(self.A*self.A + self.B*self.B)
line = Line.fromCoord(1, 0, 0, 1)
# print(line)
print(line.distanceToZero())
