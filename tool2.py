import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math




def drawCoord(length):

    glBegin(GL_LINES)


    glColor4f(1.0, 1.0, 1.0, 0.005)
    for i in range(int(length)):
        glVertex3f(i, 0, 0)
        glVertex3f(i, length, 0)
        glVertex3f(0, i, 0)
        glVertex3f(length, i, 0)

        glVertex3f(0, i, 0)
        glVertex3f(0, i, length)
        glVertex3f(0, 0, i)
        glVertex3f(0, length, i)

        glVertex3f(0, 0, i)
        glVertex3f(length, 0, i)
        glVertex3f(i, 0, 0)
        glVertex3f(i, 0, length)


    # draw x, y, z axis
    glColor(1, 0, 0)
    glVertex3f(0, 0, 0)
    glVertex3f(length, 0, 0)

    glColor(0, 1, 0)
    glVertex3f(0, 0, 0)
    glVertex3f(0, length, 0)

    glColor(0, 0, 1)
    glVertex3f(0, 0, 0)
    glVertex3f(0, 0, length)

    glEnd()




def drawCone(radius, height, num_slices):
    r = radius
    h = height
    n = float(num_slices)


    circle_pts = []
    for i in range(int(n) + 1):
        angle = 2 * math.pi * (i/n)
        x = r * math.cos(angle)
        y = r * math.sin(angle)
        pt = (x, y)
        circle_pts.append(pt)



    # draw the cone
    glBegin(GL_TRIANGLE_FAN) # drawing the front circle
    glColor(1, 0.85, 0.72)
    glVertex(0, 0, h/2.0)
    for (x, y) in circle_pts:
        z = -h/2.0
        glVertex(x, y, -z)
    glEnd()


    glBegin(GL_LINES)
    glColor(1, 1, 1)
    glVertex3f(0, -2, -5)
    glVertex3f(0, 0, 5)
    glEnd()




def drawCylinder(startPosition, h):

    # begin with this position
    glTranslatef(startPosition[0], startPosition[1], startPosition[2])

    # draw the cylinder
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










if __name__ == '__main__':

    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0] / display[1]), 0, 50.0)
    glTranslatef(0, 0, -20)

    # camera position
    gluLookAt(3, 3, 3, 0, 0, 0, 0, 0, 1)

    # glEnable(GL_BLEND)

    x = 0
    y = 0
    z = 0

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        #glRotatef(1, 0, 1, 0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glPushMatrix()

        # move the cylinder
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            glTranslatef(0.1, 0, 0)
            x += 0.1
        elif keys[pygame.K_RIGHT]:
            glTranslatef(-0.1, 0, 0)
            x -= 0.1
        elif keys[pygame.K_UP]:
            glTranslatef(0, -0.1, 0)
            y -= 0.1
        elif keys[pygame.K_DOWN]:
            glTranslatef(0, 0.1, 0)
            y += 0.1
        elif keys[pygame.K_w]:
            glTranslatef(0, 0.1, 0)
            z += 0.1
        elif keys[pygame.K_s]:
            glTranslatef(0, -0.1, 0)
            z -= 0.1

        # drawCone(2, 10, 100)
        drawCylinder((x, y, z), 3)

        glPopMatrix()

        # draw the coordinate system
        drawCoord(10)





        pygame.display.flip()
        pygame.time.wait(10)





