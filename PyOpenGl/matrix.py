from math import *
from vector import *

class Matrix():
    def __init__(self, row1, row2, row3):
        self.row1 = row1
        self.row2 = row2
        self.row3 = row3

        self.column1 = Vector(row1.x, row2.x, row3.x)
        self.column2 = Vector(row1.y, row2.y, row3.y)
        self.column3 = Vector(row1.z, row2.z, row3.z)

    @staticmethod
    def mI():
        row1 = Vector(1, 0, 0)
        row2 = Vector(0, 1, 0)
        row3 = Vector(0, 0, 1)
        return Matrix(row1, row2, row3)

    @staticmethod
    def MRot(vector, angle):
        row1 = Vector(0, vector.z, -vector.y)
        row2 = Vector(-vector.z, 0, vector.x)
        row3 = Vector(vector.y, -vector.x, 0)
        s = Matrix(row1, row2, row3)
        rotation_matrix = Matrix.mI().add(s.mult(sin(angle))).add(s.mult_matrix(s).mult(1 - cos(angle)))
        return rotation_matrix

    def MxR(self, integer):
        row1 = self.row1.VxR(integer)
        row2 = self.row2.VxR(integer)
        row3 = self.row3.VxR(integer)
        return Matrix(row1, row2, row3)

    def MplusM(self, matrix):
        row1 = self.row1.VplusV(matrix.row1)
        row2 = self.row2.VplusV(matrix.row2)
        row3 = self.row3.VplusV(matrix.row3)
        return Matrix(row1, row2, row3)

    def MminusM(self, matrix):
        row1 = self.row1.VminusV(matrix.row1)
        row2 = self.row2.VminusV(matrix.row2)
        row3 = self.row3.VminusV(matrix.row3)
        return Matrix(row1, row2, row3)

    def MxV(self, vector):
        x = self.row1.VdotV(vector)
        y = self.row2.VdotV(vector)
        z = self.row3.VdotV(vector)
        return Vector(x, y, z)

    def MxM(self, matrix):
        x = self.row1.VdotV(matrix.column1)
        y = self.row1.VdotV(matrix.column2)
        z = self.row1.VdotV(matrix.column3)
        row1 = Vector(x, y, z)

        x = self.row2.VdotV(matrix.column1)
        y = self.row2.VdotV(matrix.column2)
        z = self.row2.VdotV(matrix.column3)
        row2 = Vector(x, y, z)

        x = self.row3.VdotV(matrix.column1)
        y = self.row3.VdotV(matrix.column2)
        z = self.row3.VdotV(matrix.column3)
        row3 = Vector(x, y, z)

        return Matrix(row1, row2, row3)
