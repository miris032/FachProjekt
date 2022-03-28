import itertools

import pygame as pg
from pygame.locals import *
import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *
from Aufgabe1.simulations import drawCoord
from Aufgabe1New import pointsGenerator
from Aufgabe1New.pointsGenerator import getEdges

cubeVertices = ((0,0,0), (0,0,2), (0,0,4), (0,0,6),
                (0,5,0), (0,5,2), (0,5,4), (0,5,6),
                (5,0,0), (5,0,2), (5,0,4), (5,0,6),
                (5,5,0), (5,5,2), (5,5,4), (5,5,6))
cubeVertices = np.array(cubeVertices)

cubeEdges = ((0,1), (1,2), (2,3),
             (4,5), (5,6), (6,7),
             (8,9), (9,10), (10,11),
             (12,13), (12,13), (14,15))
cubeEdges = np.array(cubeEdges)


Vertices_3D = pointsGenerator.getPoints(4)
pointsList = np.array(list(itertools.product(range(0, 2, 1), repeat=3)))
edges = np.array([[0,1], [2,3], [4,5], [6,7]])



def drawWires():
    glBegin(GL_LINES)
    for Edge in edges:
        for pointsList in Edge:
            glVertex3fv(cubeVertices[pointsList])
    glEnd()


def get_diff2d(A, B):
    nrows, ncols = A.shape
    dtype = {'names': ['f{}'.format(i) for i in range(ncols)], 'formats': ncols * [A.dtype]}
    arr = np.setdiff1d(A.copy().view(dtype), B.copy().view(dtype))
    return arr


def getCuttedPointIndex(pos):
    global cubeVertices
    if (pos in cubeVertices):
        return cubeVertices.tolist().index(list(pos))
def cut(pos):
    global cubeVertices
    if(pos in cubeVertices):
        cubeVertices = get_diff2d(cubeVertices, np.array(pos))
        return cubeVertices




def main():
    pg.init()
    display = (800, 600)
    pg.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0, 0.0, -5)
    gluLookAt(10, 00, 00, 0, 0, 0, 0, 0, 1)

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()

        #glRotatef(1, 1, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        #solidCube()
        drawWires()
        #drawCoord((150, 150, 150), 5)

        pg.display.flip()
        pg.time.wait(10)




def main2():
    print(cubeVertices)
    length = len(cubeVertices)
    print(length)
    print("----------打印初始所有点和点的个数")
    print()

    pos = (3, 3, 2)
    cuttedIndex = getCuttedPointIndex(pos)
    print(cuttedIndex)
    cut(pos)
    print("----------打印被切掉的点的index")
    print()

    print(cubeVertices)
    print("----------打印剩下的所有点")
    print()

    indexList = list(range(0, length))
    print(indexList)
    indexList.remove(cuttedIndex)
    print(indexList)





if __name__ == "__main__":
    print(pointsList)
    print(edges)
    main()

    # main2()
    #print(Vertices_3D)





