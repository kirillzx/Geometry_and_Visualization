from math import *
from matrix import *
from vector import *

def GetZ(x, y, H):
    x1 = trunc(x)
    y1 = trunc(y)
    x2 = x - x1
    y2 = y - y1

    if (x1 + y1) % 2 == 0:
        r = True
    else:
        r = False

    if r:
        if x2 > y2:
            v1 = Vector(x1,y1+1,H[x1][y1+1])
            v2 = Vector(1,0,H[x1+1][y1+1] - H[x1][y1+1])
            v3 = Vector(0,-1,H[x1][y1] - H[x1][y1+1])
        else:
            v1 = Vector(x1+1,y1,H[x1+1][y1])
            v2 = Vector(0,1,H[x1+1][y1+1] - H[x1+1][y1])
            v3 = Vector(-1,0,H[x1][y1] - H[x1+1][y1])
    else:
        if y2 < 1 - x2:
            v1 = Vector(x1,y1,H[x1][y1])
            v2 = Vector(0,1,H[x1][y1+1] - H[x1][y1])
            v3 = Vector(1,0,H[x1+1][y1] - H[x1][y1])
        else:
            v1 = Vector(x1+1,y1+1,H[x1+1][y1+1])
            v2 = Vector(-1,0,H[x1][y1+1] - H[x1+1][y1+1])
            v3 = Vector(0,-1,H[x1+1][y1] - H[x1+1][y1+1])

    t1 = v2.VxV(v3)
    z = -(t1.x*x+t1.y*y-t1.VdotV(v1))/t1.z
    return z
# def strR(r):
#     return '{0:.2f}'.format(r)
# f = open('H.txt', 'r')
# wH = int(f.readline())
# hH = int(f.readline())
# for x in range(wH):
# 	H.append([])
# 	for y in range(hH):
# 		z = float(f.readline())
# 		H[x].append(z)
# f.close()
#
# x, y = map(float, input().split())
#print(strR(GetZ(x, y)))
