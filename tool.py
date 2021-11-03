import math
import time
import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


class tool():

    def __init__(self, toolNr, d, l, r, z):
        self.toolNr = toolNr
        self.d = d
        self.l = l
        self.r = r
        self.z = z

    def getToolNr(self):
        return self.toolNr

    def setToolNr(self, value):
        if not isinstance(value, int):
            raise ValueError('ToolNr must be an integer!')
        self.toolNr = value

    def getDurchmesser(self):
        return self.d

    def setDurchmesser(self, value):
        if not isinstance(value, int):
            raise ValueError('Durchmesser must be an integer!')
        self.d = value

    def getSchneidenlaenge(self):
        return self.l

    def setSchneidenlaenge(self, value):
        if not isinstance(value, int):
            raise ValueError('Schneidenlaenge must be an integer!')
        self.l = value

    def getEckradius(self):
        return self.r

    def setEckradius(self, value):
        if not isinstance(value, int):
            raise ValueError('Eckradius must be an integer!')
        self.r = value

    def getSchneidenanzahl(self, value):
        return self.z

    def setSchneidenanzahl(self, value):
        if not isinstance(value, int):
            raise ValueError('Eckradius must be an integer!')
        self.z = value

    # TODO
    def move(self):
        return 0

    def cylinder(self, x1, y1, z1, x2, y2, z2, radius):
        v = [x2 - x1, y2 - y1, z2 - z1]
        height = math.sqrt(v[0] * v[0] + v[1] * v[1] + v[2] * v[2])
        axis = (1, 0, 0) if math.hypot(v[0], v[1]) < 0.001 else cross(v, (0, 0, 1))
        angle = -math.atan2(math.hypot(v[0], v[1]), v[2]) * 180 / math.pi

        glPushMatrix()
        glTranslate(x1, y1, z1)
        glRotate(angle, *axis)
        glutSolidCylinder(radius, height, 24, 12)  # radius, height, line1 in the cylinder, line2 in the cylinder
        glPopMatrix()


def cross(a, b):
    return [a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]]


def setCylinder(tool):
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    # rotation
    # glRotatef(30, 0, -1, 0)

    # move
    glTranslatef(-0.5, 0, 0)

    gluPerspective(45, wnd_w / wnd_h, 0.1, 10)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    # stellt Blickwinkel(für Augen)
    gluLookAt(0, -2, -1, 0, 0, 0, 0, 0, 1)

    # stellt Hintergrund Frabe
    glClearColor(0.5, 0.5, 0.5, 1.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    # glEnable(GL_DEPTH_TEST)
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)  # causes wire frame

    # stellt Zylinder Frabe
    glColor(1, 1, 0.5)

    # Zylinder malen
    tool.cylinder(0, 0, 0, 0, 0, tool.getSchneidenlaenge(), tool.getDurchmesser() / 2)

    glutSwapBuffers()
    glutPostRedisplay()


"""nptx = 10
npty = 10

def drawCoordinates():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 1.0, 0.0)
    glLineWidth(2)

    glBegin(GL_QUADS)

    for ye in range(0, npty):
        for xe in range(0, nptx):
            glVertex3f(xe, ye + 1, 0)
            glVertex3f(xe + 1, ye + 1, 0)
            glVertex3f(xe + 1, ye, 0)
            glVertex3f(xe, ye, 0)

    glEnd()
    glFlush()
"""

if __name__ == '__main__':
    wnd_w, wnd_h = 800, 600
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(wnd_w, wnd_h)
    # glutInitWindowPosition(50, 50)
    glutCreateWindow("Aufgabe 1")

    # ein neuer Zylinder erzeugen
    tool1 = tool(1, 0.08, 0.3, 0, 2)
    tool2 = tool(2, 0.3, 0.6, 0, 2)


    # malen Zylinder
    def runSetCylinder():
        return setCylinder(tool2)

    glutDisplayFunc(runSetCylinder)  # kann nicht wie setCylinder() in glutDisplayFunc() sein

    # glTranslatef(-5, 0, 0)

    glutMainLoop()
