import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math
import sys



def draw_cylinder(radius, height, num_slices):
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

    glBegin(GL_TRIANGLE_FAN)#drawing the back circle
    glColor(1, 0.85, 0.72)
    glVertex(0, 0, h/2.0)
    for (x, y) in circle_pts:
        z = h/2.0
        glVertex(x, y, z)
    glEnd()

    glBegin(GL_TRIANGLE_FAN)#drawing the front circle
    glColor(1, 0.85, 0.72)
    glVertex(0, 0, h/2.0)
    for (x, y) in circle_pts:
        z = -h/2.0
        glVertex(x, y, z)
    glEnd()

    glBegin(GL_TRIANGLE_STRIP)#draw the tube
    glColor(1, 0.9, 0.7)
    for (x, y) in circle_pts:
        z = h/2.0
        glVertex(x, y, z)
        glVertex(x, y, -z)
    glEnd()



if __name__ == '__main__':

    """pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    rotation = 0.0
    while True:
        pygame.time.delay(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill((220, 220, 220))
        pygame.display.flip()"""

    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -20)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 1, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        draw_cylinder(2, 10, 100)

        pygame.display.flip()
        pygame.time.wait(10)








    """(width, height) = (800, 600)
    screen = pygame.display.set_mode((800, 600), OPENGL | DOUBLEBUF)
    screen.fill(color)
    clock = pygame.time.Clock()
    rotation = 0.0

    while True:

        pygame.time.delay(10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()



        rotation += 1.0
        glClear(GL_COLOR_BUFFER_BIT)
        glClear(GL_DEPTH_BUFFER_BIT)
        glEnable(GL_DEPTH_TEST)

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(30, float(width) / height, 1, 1000)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glTranslate(0, 0, -50)  # move back far enough to see this object
        glRotate(rotation, 0, 1, 0)  # NOTE: this is applied BEFORE the translation due to OpenGL multiply order

        draw_cylinder(2, 10, 100)
        pygame.display.flip()
        clock.tick(60)"""


