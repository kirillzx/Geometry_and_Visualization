from math import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from matrix import *
from vector import *
from check import *
from PIL import Image, ImageDraw

def h_map(filename, val):
    image = Image.open(filename)
    width  = image.size[0]
    height = image.size[1]
    pix = image.load()
    array = [[0]*width for _ in range(height)]
    for x in range(width)[:-1]:
            for y in range(height):
                    array[x][y] = round(pix[x, y]*val, 3)
    return array

window_width = 800
window_height = 600

# Процедура инициализации
def init():
    glEnable(GL_DEPTH_TEST)
    glClearColor(1.0, 1.0, 1.0, 1.0) # Белый цвет для первоначальной закраски
    glMatrixMode(GL_PROJECTION) # Выбираем матрицу проекций
    glLoadIdentity()            # Сбрасываем все предыдущие трансформации
    gluPerspective(90, window_width / window_height, 0.001, 30) # Задаем перспективу
	#gluOrtho2D(-1.0, 1.0, -1.0, 1.0) # Определяем границы рисования по горизонтали и вертикали
    global anglex, angley, anglez, zoom, filled, map1, camPOS, camDIR, camUP, op, od, of
    anglex = 0
    angley = 0
    anglez = 0
    zoom = 1.0
    filled = 0
    map1 = h_map('map.bmp', 0.3)
    op = Vector(0,0,map1[0][0])
    od = Vector(0.7,0.7,0)
    camPOS = op.VplusV(Vector(-1, -1, 1))
    camDIR = Vector(0.7, 0.7, 0)
    camUP = Vector(0, 0, 1)
    of = 0

# Процедура обработки обычных клавиш
def keyboardkeys(key, x, y):
    global anglex, angley, anglez, zoom, filled, camPOS, camDIR, camUP

    if key == b'\x1b':
        sys.exit(0)
    if key == b'w':
        anglex += 5
    if key == b's':
        anglex -= 5
    if key == b'q':
        angley += 5
    if key == b'e':
        angley -= 5
    if key == b'a':
        anglez += 5
    if key == b'd':
        anglez -= 5
    if key == b'-':
        zoom /= 1.1
    if key == b'=':
        zoom *= 1.1
    if key == b' ':
        filled = 1 - filled
    if key == b'o':
        rotM = Matrix.MRot(camDIR, 3.14/10)
        camUP = rotM.MxV(camUP)
    if key == b'k':
        rotM = Matrix.MRot(camDIR, -3.14/10)
        camUP = rotM.MxV(camUP)
    if key == b'p':
        cross = camDIR.VxV(camUP)
        rotM = Matrix.MRot(cross, 3.14/10)
        camUP = rotM.MxV(camUP)
        camDIR = rotM.MxV(camDIR)
    if key == b'l':
        cross = camDIR.VxV(camUP)
        rotM = Matrix.MRot(cross, -3.14/10)
        camUP = rotM.MxV(camUP)
        camDIR = rotM.MxV(camDIR)
    if key == b'y':
        camPOS = camPOS.VplusV(camDIR.VxR(0.3))
    if key == b'u':
        camPOS = camPOS.VminusV(camDIR.VxR(0.3))
    if key == b'i':
        rotM = Matrix.MRot(camUP, 3.14/10)
        camDIR = rotM.MxV(camDIR)
    if key == b'j':
        rotM = Matrix.MRot(camUP, -3.14/10)
        camDIR = rotM.MxV(camDIR)
    glutPostRedisplay()         # Вызываем процедуру перерисовки

def specialkeys(key,x,y):
    global anglex, angley, anglez, zoom, filled, camPOS, camDIR, camUP, map1, op, od, of
    if key == GLUT_KEY_LEFT:
        r1 = Matrix.MRot(Vector(0,0,1),-3.14/10)
        od = r1.MxV(od)
        of += 1
        if of == 24 or of == -24:
            of = 0
    if key == GLUT_KEY_RIGHT:
        r1 = Matrix.MRot(Vector(0,0,1), 3.14/10)
        od = r1.MxV(od)
        of -= 1
        if of == 24 or of == -24:
            of = 0
    if key == GLUT_KEY_UP:
        op = op.VplusV(od)
        op.z = GetZ(op.x,op.y,map1) + 0.3
        camPOS = camPOS.VplusV(od)
        camPOS.z = op.z + 0.3
    if key == GLUT_KEY_DOWN:
        op = op.VminusV(od)
        op.z = GetZ(op.x,op.y, map1) + 0.3
        camPOS = camPOS.VminusV(od)
        camPOS.z = op.z + 0.5

def cilinder():
	R = 0.5

	glBegin(GL_TRIANGLE_FAN)

	glVertex3d( 0,  0, -0.5)
	for i in range(21):
		glVertex3d(R * cos(2*pi*i/20), \
			R * sin(2*pi*i/20), -0.5)

	glEnd()

	glBegin(GL_QUAD_STRIP)

	for i in range(21):
		glVertex3d(R * cos(2*pi*i/20), \
			R * sin(2*pi*i/20), -0.5)
		glVertex3d(R * cos(2*pi*i/20), \
			R * sin(2*pi*i/20), 0.5)

	glEnd()

	glBegin(GL_TRIANGLE_FAN)

	glVertex3d( 0,  0, 0.5)
	for i in range(21):
		glVertex3d(R * cos(2*pi*i/20), \
			R * sin(2*pi*i/20), 0.5)

	glEnd()

def sphere():
	R = 0.5

	for j in range(-9,9):
		glBegin(GL_QUAD_STRIP)

		for i in range(21):
			glVertex3d(R * cos(pi*j/18) * cos(2*pi*i/20), \
				R * cos(pi*j/18) * sin(2*pi*i/20), \
				R * sin(pi*j/18))
			glVertex3d(R * cos(pi*(j+1)/18) * cos(2*pi*i/20), \
				R * cos(pi*(j+1)/18) * sin(2*pi*i/20), \
				R * sin(pi*(j+1)/18))

		glEnd()

# Процедура рисования
def draw(*args, **kwargs):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    global anglex, angley, anglez, zoom, filled, camPOS, camDIR, camUP, map1, op, od, of
    gluLookAt(camPOS.x, camPOS.y, camPOS.z,
              camPOS.x + camDIR.x, camPOS.y + camDIR.y, camPOS.z + camDIR.z,
              camUP.x, camUP.y, camUP.z)
    glRotated(anglex,1,0,0)
    glRotated(angley,0,1,0)
    glRotated(anglez,0,0,1)
    glScaled(zoom,zoom,zoom)

    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
    glPushMatrix()
    glColor3f(1,0.5,1)
    glTranslated(op.x,op.y,op.z)
    glRotated(of*10,0,0,1)
    glRotated(90,-1,-1,0)
    sphere()
    glPopMatrix()

    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    n = len(map1)
    m = len(map1[0])
    for y in range(1, n, 2):
        for x in range(1, m, 2):
            glBegin(GL_TRIANGLE_FAN)
            glColor3f(0, 0, 0)
            glVertex3d(x, y, map1[x][y])

            glVertex3d(x + 1, y, map1[x + 1][y])
            glVertex3d(x + 1, y + 1, map1[x + 1][y + 1])
            glVertex3d(x, y + 1, map1[x][y + 1])
            glVertex3d(x - 1, y + 1, map1[x - 1][y + 1])
            glVertex3d(x - 1, y, map1[x - 1][y])
            glVertex3d(x - 1, y - 1, map1[x - 1][y - 1])
            glVertex3d(x, y - 1, map1[x][y - 1])
            glVertex3d(x + 1, y - 1, map1[x + 1][y - 1])
            glVertex3d(x + 1, y, map1[x + 1][y])

            glEnd()

    glutSwapBuffers()           # Меняем буферы
    glutPostRedisplay()         # Вызываем процедуру перерисовки

glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(window_width, window_height)
glutInitWindowPosition(50, 50)
glutInit(sys.argv)
glutCreateWindow(b"OpenGL VSR!")
# Определяем процедуру, отвечающую за рисование
glutDisplayFunc(draw)
# Определяем процедуру, отвечающую за обработку обычных и необычных клавиш
glutKeyboardFunc(keyboardkeys)
glutSpecialFunc(specialkeys)
# Вызываем нашу функцию инициализации
init()
glutMainLoop()
