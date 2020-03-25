from math import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# Процедура инициализации
def init():
	glEnable(GL_DEPTH_TEST)
	glClearColor(0.5, 0.5, 0.5, 1.0) # Серый цвет для первоначальной закраски
	gluOrtho2D(-1.0, 1.0, -1.0, 1.0) # Определяем границы рисования по горизонтали и вертикали
	global filled
	filled = 1

# Процедура обработки обычных клавиш
def keyboardkeys(key, x, y):
	global filled
	if key == b'\x1b':
		sys.exit(0)
	if key == b' ':
		filled = 1 - filled
	glutPostRedisplay()         # Вызываем процедуру перерисовки

# Процедура рисования
def draw(*args, **kwargs):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # Очищаем экран и заливаем текущим цветом фона
    glRotated(0.125,1,1,1)

    R = 0.3
    for j in range(-9,8):
        glBegin(GL_QUAD_STRIP)
        glColor3f(1,0,1)
        for i in range(21):
            z1 = R * sin(pi * j/18)
            z2 = R * sin(pi*(j+1)/18)
            k1 = R * cos(pi * j/18)
            k2 = R * cos(pi*(j+1)/18)
            glVertex3d(k1*cos(i*2*pi/20), k1*sin(i*2*pi/20), z1)
            glVertex3d(k2*cos(i*2*pi/20), k2*sin(i*2*pi/20), z2)
        glEnd()

    glBegin(GL_QUAD_STRIP)
    glColor3f(0,0,0)
    for i in range(21):
        r = R * cos(pi/4)
        z1 = R * sin(pi/4)
        glVertex3d(r*cos(i*2*pi/20), r*sin(i*2*pi/20), z1)
        glVertex3d(r*cos(i*2*pi/20), r*sin(i*2*pi/20), 1)
    glEnd()

    glBegin(GL_TRIANGLE_FAN)
    glColor3f(0,0,0)
    glVertex3d(0,0,1)
    for i in range(21):
        glVertex3d(r*cos(i*2*pi/20),r*sin(i*2*pi/20),1)
    glEnd()
        
    glutSwapBuffers()           # Меняем буферы
    glutPostRedisplay()         # Вызываем процедуру перерисовки

glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(800, 600)
glutInitWindowPosition(50, 50)
glutInit(sys.argv)
glutCreateWindow(b"OpenGL")
# Определяем процедуру, отвечающую за рисование
glutDisplayFunc(draw)
# Определяем процедуру, отвечающую за обработку обычных клавиш
glutKeyboardFunc(keyboardkeys)
# Вызываем нашу функцию инициализации
init()
glutMainLoop()
