from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# Процедура инициализации
def init():
    glEnable(GL_DEPTH_TEST)
    glClearColor(0.5, 0.5, 0.5, 1.0) # Серый цвет для первоначальной закраски
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0) # Определяем границы рисования по горизонтали и вертикали

# Процедура обработки обычных клавиш
def keyboardkeys(key, x, y):
    if key == b'\x1b':
        sys.exit(0)
    glutPostRedisplay()         # Вызываем процедуру перерисовки

def best_cubes(x, y, z, length):
    k = length/2
    
    glColor3f(1, 0, 0)
    glVertex3d(x - k, y - k, z + k)
    glVertex3d(x + k, y - k, z + k)
    glVertex3d(x + k, y + k, z + k)
    glVertex3d(x - k, y + k, z + k)

    glColor3f(0, 1, 0)
    glVertex3d(x - k, y - k, z - k)
    glVertex3d(x + k, y - k, z - k)
    glVertex3d(x + k, y + k, z - k)
    glVertex3d(x - k, y + k, z - k)

    glColor3f(0, 0, 1)
    glVertex3d(x - k, y + k, z + k)
    glVertex3d(x + k, y + k, z + k)
    glVertex3d(x + k, y + k, z - k)
    glVertex3d(x - k, y + k, z - k)

    glColor3f(1, 1, 0)
    glVertex3d(x - k, y - k, z - k)
    glVertex3d(x - k, y + k, z - k)
    glVertex3d(x - k, y + k, z + k)
    glVertex3d(x - k, y - k, z + k)

    glColor3f(0, 1, 1)
    glVertex3d(x + k, y - k, z + k)
    glVertex3d(x + k, y - k, z - k)
    glVertex3d(x + k, y + k, z - k)
    glVertex3d(x + k, y + k, z + k)

    glColor3f(1, 0, 1)
    glVertex3d(x - k, y - k, z + k)
    glVertex3d(x - k, y - k, z - k)
    glVertex3d(x + k, y - k, z - k)
    glVertex3d(x + k, y - k, z + k)

# Процедура рисования
def draw(*args, **kwargs):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # Очищаем экран и заливаем текущим цветом фона
    glRotated(0.125,1,1,1)

    glBegin(GL_QUADS)

    best_cubes(0.5, 0.5, 0.5, 0.2)
    best_cubes(0.5, -0.5, 0.5, 0.2)
    best_cubes(0.5, -0.5, -0.5, 0.2)
    best_cubes(0.5, 0.5, -0.5, 0.2)
    best_cubes(-0.5, 0.5, 0.5, 0.2)
    best_cubes(-0.5, -0.5, 0.5, 0.2)
    best_cubes(-0.5, 0.5, -0.5, 0.2)
    best_cubes(-0.5, -0.5, -0.5, 0.2)

    glEnd()

    glutSwapBuffers()           # Меняем буферы
    glutPostRedisplay()         # Вызываем процедуру перерисовки

glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(800, 600)
glutInitWindowPosition(50, 50)
glutInit(sys.argv)
glutCreateWindow(b"OpenGL Cube")
# Определяем процедуру, отвечающую за рисование
glutDisplayFunc(draw)
# Определяем процедуру, отвечающую за обработку обычных клавиш
glutKeyboardFunc(keyboardkeys)
# Вызываем нашу функцию инициализации
init()
glutMainLoop()
