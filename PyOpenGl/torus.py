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

    R1 = 0.2
    R2 = 0.1
    
    for j in range(-9,8):
        glBegin(GL_QUAD_STRIP)
        glColor3f(1,0.5,0)
        for i in range(21):
            x1 = (R1 + R2 * cos(pi * j/18)) * cos(pi * i/10)
            y1 = (R1 + R2 * cos(pi * j/18)) * sin(pi * i/10)
            z1 = R2 * sin(pi * j/16)
            x2 = (R1 + R2 * cos(pi * (j+1)/18)) * cos(pi * (i+1)/10)
            y2 = (R1 + R2 * cos(pi * (j+1)/18)) * sin(pi * (i+1)/10)
            z2 = R2 * sin((j+1)/16)
            glVertex3d(x1, y1, z1)
            glVertex3d(x2, y2, z2)
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
