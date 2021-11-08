import pygame
from OpenGL.GLUT import glutSolidCylinder, glutInit
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math



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
        glVertex(x, y, z)
    glEnd()


    glBegin(GL_LINES)
    glColor(1, 1, 1)
    glVertex3f(0, -2, -5)
    glVertex3f(0, 0, 5)
    glEnd()




def drawCylinder():
    return 1


def drawCoord(length):
    glBegin(GL_LINES)


    glColor4f(1.0, 1.0, 1.0, 0.5)
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



def move():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        glTranslatef(0.5, 0, 0)
    elif keys[pygame.K_RIGHT]:
        glTranslatef(-0.5, 0, 0)
    elif keys[pygame.K_UP]:
        glTranslatef(0, -0.5, 0)
    elif keys[pygame.K_DOWN]:
        glTranslatef(0, 0.5, 0)





if __name__ == '__main__':

    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0] / display[1]), 0, 50.0)
    glTranslatef(0.0, 0.0, -20)

    # cam position
    gluLookAt(3, 3, 3, 0, 0, 0, 0, 0, 1)

    # glEnable(GL_BLEND)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # glRotatef(1, 0, 1, 0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glPushMatrix()
        move()
        drawCone(2, 10, 100)
        glPopMatrix()


        drawCoord(12)





        pygame.display.flip()
        pygame.time.wait(10)





