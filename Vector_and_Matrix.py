from math import *

def Len(x):
    sum = 0
    for i in range(len(x)):
        sum += x[i]*x[i]
    return sqrt(sum)

def Norm(x):
    x = list(x)
    length = Len(x)
    for i in range(len(x)):
        if x[i] != 0:
            x[i] = x[i]/length
        else:
            x[i] = 0.0
    return tuple(x)

def VxR(x, a):
    x = list(x)
    for i in range(len(x)):
        x[i] = a*x[i]
    return tuple(x)

def VplusV(x, y):
    x = list(x)
    y = list(y)
    for i in range(len(x)):
        x[i] = x[i]+y[i]
    return tuple(x)

def VminusV(x, y):
    x = list(x)
    y = list(y)
    for i in range(len(x)):
        x[i] = x[i]-y[i]
    return tuple(x)

def VdotV(x, y):
    x = list(x)
    y = list(y)
    sum = 0
    for i in range(len(x)):
        sum += x[i]*y[i]
    return sum

def VxV(x, y):
    x = list(x)
    y = list(y)
    x1 = x[1]*y[2] - y[1]*x[2]
    x2 = x[0]*y[2] - y[0]*x[2]
    x3 = x[0]*y[1] - x[1]*y[0]
    return tuple([x1, -x2, x3])

def mI():
    a = [[0.00 for y in range(3)] for x in range(3)]
    for i in range(3):
        for j in range(3):
            if i == j:
                a[i][j] = 1.00
    return tuple(map(tuple, a))

def MxR(a, R):
        a = list(map(list, a))
        for i in range(len(a)):
            for j in range(len(a[0])):
                a[i][j] = a[i][j]*R
        return tuple(map(tuple, a))

def MplusM(a, b):
        a = list(map(list, a))
        b = list(map(list, b))
        for i in range(len(a)):
            for j in range(len(a[0])):
                a[i][j] = a[i][j]+b[i][j]
        return tuple(map(tuple, a))

def MminusM(a, b):
        a = list(map(list, a))
        b = list(map(list, b))
        for i in range(len(a)):
            for j in range(len(a[0])):
                a[i][j] = a[i][j]-b[i][j]
        return tuple(map(tuple, a))

def MxV(a, x):
        a = list(map(list, a))
        x = list(x)
        y = [0 for i in range(len(x))]
        for i in range(len(a)):
            sum = 0
            for j in range(len(a[0])):
                sum += a[i][j]*x[j]
            y[i] = sum
        return tuple(y)

def MxM(a, b):
        a = list(map(list, a))
        b = list(map(list, b))
        c = [[0.0 for i in range(len(a))] for i in range(len(a))]
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    c[i][j] += a[i][k] * b[k][j]

        return tuple(map(tuple, c))
def MRot(x, a):
        row1 = (0, x[2], -x[1])
        row2 = (-x[2], 0, x[0])
        row3 = (x[2], -x[0], 0)
        s = ((row1, row2, row3))
        r1 = MplusM(mI(), MxR(s, sin(a)))
        rotation_matrix = MplusM(r1, MxR(MxM(s, s), 1 - cos(a)))
        return rotation_matrix

# print(VxR((1,0,0),5))
# print(VplusV((1.0,0.0,0.0), (2,3,4)))
# print(VdotV((1,0,1),(1,0,1)))
# print(VxV((4,5,6),(1,2.5,4.7)))
a = mI()
b = ((1,2,3),(4,5,6),(7,8,9))
print(MxR(a, 4))
print(MplusM(a,b))
print(MxV(b, (1,2,1)))
print(MxM(a,b))
print(MRot((1,0,0), 3.1))
