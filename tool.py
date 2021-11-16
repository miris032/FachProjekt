import time
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math
import readCSV


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

    def drawCylinder(self, startPosition, h):

        "begin on this position"
        glTranslatef(startPosition[0], startPosition[1], startPosition[2])

        "draw the cylinder"
        glBegin(GL_QUAD_STRIP)
        for i in range(0, 360, 5):
            glColor3f(1, 0.85, 0.72)
            glVertex3f(math.sin(i), math.cos(i), h)
            glVertex3f(math.sin(i), math.cos(i), 0)
        glEnd()

        glBegin(GL_LINES)
        glColor(0, 1, 1)
        glVertex3f(1, 0, h)
        glVertex3f(0, 0, h)
        glEnd()


# TODO
def drawPath():
    return None


def drawCoord(tup, dicht):

    glBegin(GL_LINES)


    glColor4f(1.0, 1.0, 1.0, 0.3)
    for i1 in range(0, int(tup[0]), dicht):
        glVertex3f(i1, 0, 0)
        glVertex3f(i1, tup[1], 0)
    for i2 in range(0, int(tup[1]), dicht):
        glVertex3f(0, i2, 0)
        glVertex3f(tup[0], i2, 0)

    for j1 in range(0, int(tup[1]), dicht):
        glVertex3f(0, j1, 0)
        glVertex3f(0, j1, tup[2])
    for j2 in range(0, int(tup[2]), dicht):
        glVertex3f(0, 0, j2)
        glVertex3f(0, tup[1], j2)

    for k1 in range(0, int(tup[2]), dicht):
        glVertex3f(0, 0, k1)
        glVertex3f(tup[0], 0, k1)
    for k2 in range(0, int(tup[0]), dicht):
        glVertex3f(k2, 0, 0)
        glVertex3f(k2, 0, tup[2])


    "draw x, y, z axis"
    glColor(1, 0, 0)
    glVertex3f(0, 0, 0)
    glVertex3f(tup[0], 0, 0)

    glColor(0, 1, 0)
    glVertex3f(0, 0, 0)
    glVertex3f(0, tup[1], 0)

    glColor(0, 0, 1)
    glVertex3f(0, 0, 0)
    glVertex3f(0, 0, tup[2])


    glEnd()




if __name__ == '__main__':

    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0] / display[1]), 0, 50.0)
    glTranslatef(0, 0, -20)

    "set the camera position"
    gluLookAt(120, 100, 120, 0, 0, 0, 0, 0, 1)

    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glEnable(GL_BLEND)

    "make a new tool: tool01"
    tool01 = tool(2, 0.3, 6, 0, 2)

    (x, y, z) = (0, 0, 0)
    movementList = readCSV.getPosFromCsv()


    for i in range(len(movementList)):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # glRotatef(1, 0, 1, 0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glPushMatrix()


        "move the cylinder:"
        tool01.drawCylinder((x, y, z), tool01.getSchneidenlaenge())

        "slow it down"
        # time.sleep(0.1)

        "print position info"
        # print(i, ": ", (x, y, z))

        x = movementList[i][0]
        y = movementList[i][1]
        z = movementList[i][2]
        glTranslatef(x, y, z)


        glPopMatrix()

        "draw the coordinate system"
        drawCoord((100, 100, 100), 5)


        pygame.display.flip()
        pygame.time.wait(10)
