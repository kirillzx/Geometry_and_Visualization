from math import *

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return '({:.2f}, {:.2f}, {:.2f})'.format(self.x, self.y, self.z)

    def Len(self):
        return sqrt(self.x*self.x + self.y*self.y + self.z*self.z)

    def Norm(self):
        l = self.len()
        if l == 0.0:
            return self
        return Vector(self.x/l, self.y/l, self.z/l)

    def VxR(self, integer):
        return Vector(self.x*integer, self.y*integer, self.z*integer)

    def VplusV(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def VminusV(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def VdotV(self, other):
        return self.x*other.x + self.y*other.y + self.z*other.z

    def VxV(self, other):
        x = self.y*other.z - self.z*other.y
        y = self.z*other.x - self.x*other.z
        z = self.x*other.y - self.y*other.x
        return Vector(x, y, z)
