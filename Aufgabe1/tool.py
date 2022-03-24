import itertools
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


    def drawCylinder(self, startPosition, radius, height):
        r = radius
        h = height
        # n = float(num_slices)
        n = 50

        glTranslatef(startPosition[0], startPosition[1], startPosition[2])

        circle_pts = []
        for i in range(int(n) + 1):
            angle = 2 * math.pi * (i / n)
            x = r * math.cos(angle)
            y = r * math.sin(angle)
            pt = (x, y)
            circle_pts.append(pt)

        glBegin(GL_TRIANGLE_STRIP)  # draw the tube
        glColor3f(1, 0.85, 0.72)
        for (x, y) in circle_pts:
            z = h / 2.0
            glVertex(x, y, z)
            glVertex(x, y, -z)
        glEnd()

        glBegin(GL_TRIANGLE_FAN)  # drawing the front circle
        glColor(1, 0, 0)
        glVertex(0, 0, h / 2.0)
        for (x, y) in circle_pts:
            z = h / 2.0
            glVertex(x, y, z)
        glEnd()


        """glBegin(GL_TRIANGLE_FAN)  # drawing the back circle
        glColor(0, 0, 1)
        glVertex(0, 0, h / 2.0)
        for (x, y) in circle_pts:
            z = -h / 2.0
            glVertex(x, y, z)
        glEnd()"""




def drawCoord(tup, dicht):

    glBegin(GL_LINES)

    glColor4f(1.0, 1.0, 1.0, 0.1)
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


def calDistance(p1, p2):
    return math.sqrt(math.pow((p2[0] - p1[0]), 2) + math.pow((p2[1] - p1[1]), 2) + math.pow((p2[2] - p1[2]), 2))




if __name__ == '__main__':

    pygame.init()
    display = (800, 600)
    scree = pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0] / display[1]), 0, 50.0)
    glTranslatef(0, 0, -20)

    "set the camera position"
    gluLookAt(180, 120, 120, 0, 40, 0, 0, 0, 1)

    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glEnable(GL_BLEND)

    "make a new tool: tool01"
    tool01 = tool(1, 30, 8, 0, 2)

    (x, y, z) = (0, 0, 0)
    movementList = readCSV.getPosFromCsv()



    displayCenter = [scree.get_size()[i] // 2 for i in range(2)]
    mouseMove = [0, 0]
    pygame.mouse.set_pos(displayCenter)

    up_down_angle = 0.0
    paused = False
    run = True
    while run:

        for i in range(len(movementList)):

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        quit()

                "keep the mouse always in the center of screen"
                '''if not paused:
                    if event.type == pygame.MOUSEMOTION:
                        mouseMove = [event.pos[i] - displayCenter[i] for i in range(2)]
                    pygame.mouse.set_pos(displayCenter)'''


            keypress = pygame.key.get_pressed()  # Move using WASD

            if keypress[pygame.K_w]:
                glTranslatef(2, 0, 0)
            if keypress[pygame.K_s]:
                glTranslatef(-2, 0, 0)
            if keypress[pygame.K_d]:
                glTranslatef(0, -2, 0)
            if keypress[pygame.K_a]:
                glTranslatef(0, 2, 0)

            """mouseMove = pygame.mouse.get_rel()
            glRotatef(mouseMove[0] * 0.1, 0.0, 1.0, 0.0)"""






            "draw all the points"
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            glPushMatrix()

            glEnable(GL_POINT_SMOOTH)
            glPointSize(5)
            glBegin(GL_POINTS)
            glColor4f(1.0, 1.0, 1.0, 0.3)

            arr = list(itertools.product(range(0, 100, 10), repeat=3))
            for j in range(len(arr)):
                glVertex3d(arr[j][0], arr[j][1], arr[j][2])

            glEnd()


            "move the cylinder"
            tool01.drawCylinder((x, y, z), tool01.getSchneidenlaenge(), tool01.getDurchmesser())






            "print position info"
            # print(i, ": ", (x, y, z))

            x = movementList[i][0]
            y = movementList[i][1]
            z = movementList[i][2]
            x1 = movementList[i+1][0]
            y1 = movementList[i+1][1]
            z1 = movementList[i+1][2]
            #glTranslatef(x, y, z)

            "speed control"
            distance = calDistance((x1, y1, z1), (x, y, z))
            speed = movementList[i][3]
            t = distance / speed
            time.sleep(t * 60)


            glPopMatrix()

            "set all cubes"
            '''#drawAllCubes()
            Cube()
            glTranslatef(10, 0, 0)
            glFlush()'''






            "draw the coordinate system"
            drawCoord((100, 150, 100), 5)




            pygame.display.flip()
            pygame.time.wait(10)

