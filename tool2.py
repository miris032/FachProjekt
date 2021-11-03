import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math



def draw_cylinder(radius, height, num_slices):
    r = radius
    h = height
    n = float(num_slices)

    #gluLookAt(0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 1)

    circle_pts = []
    for i in range(int(n) + 1):
        angle = 2 * math.pi * (i/n)
        x = r * math.cos(angle)
        y = r * math.sin(angle)
        pt = (x, y)
        circle_pts.append(pt)



    # draw the cone
    glBegin(GL_TRIANGLE_FAN)#drawing the front circle
    glColor(1, 0.85, 0.72)
    glVertex(0, 0, h/2.0)
    for (x, y) in circle_pts:
        z = -h/2.0
        glVertex(x, y, z)
    glEnd()


    glBegin(GL_LINES)
    glColor(0, 1, 0)
    glVertex3f(0, -2, -5)
    glVertex3f(0, 0, 5)
    glEnd()




if __name__ == '__main__':

    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0] / display[1]), 0, 50.0)
    glTranslatef(0.0, 0.0, -20)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 0, 1, 0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)


        draw_cylinder(2, 10, 100)

        pygame.display.flip()
        pygame.time.wait(10)




