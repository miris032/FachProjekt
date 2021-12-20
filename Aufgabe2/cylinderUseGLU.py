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

    glRotatef(0, 10, 0, 0)


def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    gluLookAt(3, 0, 3, 0, 0, 0, 0, 0, 1)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        #glRotatef(1, 1, 0, 0)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        drawCylinder((0, 0, 0), 1, 5)
        pygame.display.flip()
        pygame.time.wait(10)



if __name__ == '__main__':
    main()