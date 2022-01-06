import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

import math


def drawCylinder(startPosition, radius, height):
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






if __name__ == '__main__':
    pygame.init()
    display = (800, 600)
    scree = pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glShadeModel(GL_SMOOTH)
    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)

    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_AMBIENT, [0.5, 0.5, 0.5, 1])
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [1.0, 1.0, 1.0, 1])

    sphere = gluNewQuadric()

    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)

    glMatrixMode(GL_MODELVIEW)
    gluLookAt(18, 12, 12, 0, 0, 0, 0, 0, 1)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glEnable(GL_BLEND)
    viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)
    glLoadIdentity()

    # init mouse movement and center mouse on screen
    displayCenter = [scree.get_size()[i] // 2 for i in range(2)]
    mouseMove = [0, 0]
    pygame.mouse.set_pos(displayCenter)

    up_down_angle = 0.0
    paused = False
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN:
                    run = False
                if event.key == pygame.K_PAUSE or event.key == pygame.K_p:
                    paused = not paused
                    pygame.mouse.set_pos(displayCenter)
            if not paused:
                if event.type == pygame.MOUSEMOTION:
                    mouseMove = [event.pos[i] - displayCenter[i] for i in range(2)]
                pygame.mouse.set_pos(displayCenter)

        if not paused:
            # get keys
            keypress = pygame.key.get_pressed()
            # mouseMove = pygame.mouse.get_rel()

            # init model view matrix
            glLoadIdentity()

            # apply the look up and down
            up_down_angle += mouseMove[1] * 0.1
            glRotatef(up_down_angle, 1.0, 0.0, 0.0)




            # init the view matrix
            glPushMatrix()
            glLoadIdentity()

            # apply the movment
            if keypress[pygame.K_w]:
                glTranslatef(0, 0, 0.1)
            if keypress[pygame.K_s]:
                glTranslatef(0, 0, -0.1)
            if keypress[pygame.K_d]:
                glTranslatef(-0.1, 0, 0)
            if keypress[pygame.K_a]:
                glTranslatef(0.1, 0, 0)

            # apply the left and right rotation
            glRotatef(mouseMove[0] * 0.1, 0.0, 1.0, 0.0)

            # multiply the current matrix by the get the new view matrix and store the final vie matrix
            glMultMatrixf(viewMatrix)
            viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)

            # apply view matrix
            glPopMatrix()
            glMultMatrixf(viewMatrix)





            glLightfv(GL_LIGHT0, GL_POSITION, [1, -1, 1, 0])

            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

            glPushMatrix()

            drawCylinder((0, 0, 0), 0.8, 3)

            glPopMatrix()

            drawCoord((10, 15, 10), 1)

            pygame.display.flip()
            pygame.time.wait(10)

    pygame.quit()