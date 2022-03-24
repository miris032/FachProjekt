import math
import time
from pyqtgraph.Qt import QtCore, QtGui
from OpenGL.arrays import vbo
import pyqtgraph as pg
import pyqtgraph.opengl as gl
import scipy.ndimage as ndi
import numpy as np
import pyqtgraph
import sys
import readData
from numba import jit


'''create a GL View w'''
app = QtGui.QApplication([])
w = gl.GLViewWidget()
w.setWindowTitle('demo')
# w.setFixedSize(800, 600)
w.setBackgroundColor(pyqtgraph.mkColor(32, 32, 32))
w.setCameraPosition(distance=500)
w.show()

'''coordinate system'''
g = gl.GLGridItem()
g.scale(10, 10, 10)
g.setDepthValue(10)  # draw grid after surfaces since they may be translucent
w.addItem(g)

"""Cylinder"""
r = 7.5 * 10
h = 10 * 10
cylinder = gl.MeshData.cylinder(rows=10, cols=20, radius=[r, r], length=h)
m1 = gl.GLMeshItem(
    meshdata=cylinder,
    smooth=True,
    # smooth=False,
    # color=(1, 1, 1, 0.5),
    # shader="balloon",
    color=(0, 0, 0, 1),
)
#w.addItem(m1)

'''md = gl.MeshData.sphere(rows=20, cols=20, radius=75)
m2 = gl.GLMeshItem(meshdata=md, smooth=False, drawFaces=True, drawEdges=True, edgeColor=(0, 0, 0, 1), color=(0, 0, 0, 1))
m2.translate(0, 0, 100)
w.addItem(m2)'''


'''vertexes = np.array([[0, 0, 0], #0
                     [50, 0, 0], #1
                     [0, 50, 0], #2
                     [0, 0, 50], #3
                     [50, 50, 0], #4
                     [10, 10, 10], #5
                     [0, 10, 10], #6
                     [10, 0, 10]])#7



faces = np.array([[1,2,4], [1,0,4]])
circle = gl.GLMeshItem(vertexes=vertexes, faces=faces,
                     drawEdges=True, edgeColor=(0, 0, 0, 1), color=(0, 0, 0, 1))
w.addItem(circle)'''




"""get all positions of each fragment"""
def getPositionList(x, y):
    # grad = 15.9605 * 2
    grad = math.degrees(math.atan(2.145/2/7.5)) * 2
    sin = math.sin(math.radians(grad))
    cos = math.cos(math.radians(grad))
    positionList = [(x, y)]
    for i in range(22):
        Xnew = positionList[i][0] * cos - positionList[i][1] * sin
        Ynew = positionList[i][0] * sin + positionList[i][1] * cos
        positionList.append((Xnew, Ynew))
    return positionList




"""topography"""
dataList = np.array(readData.getData())
# dataList = np.transpose(dataList)
# arr = np.array_split(dataList, 7)
dataList2 = np.array(readData.getData2())


# 3+1个叠一起
arr = np.vstack((dataList, dataList, dataList, dataList2))
# print(arr.shape)
# (1506, 1373)

arr = np.array_split(arr, 2, axis=1)




# z1 = ndi.gaussian_filter(arr[0], (0.5, 0.5))

grad = math.degrees(math.atan(2.145/2/7.5)) * 2
positionList = getPositionList(-21.45/2, -75) # begin with the first position




p1 = gl.GLSurfacePlotItem(z=np.transpose(arr[0]), shader='shaded', color=(0.54, 0.32, 0.17, 1), computeNormals=True, smooth=False)
p1.scale(0.0105*3, 0.022*3, 8)
p1.rotate(90, 1, 0, 0)
p1.translate(positionList[0][0], positionList[0][1], 0)
w.addItem(p1)

p2 = gl.GLSurfacePlotItem(z=np.transpose(arr[1]), shader='shaded', color=(0.54, 0.32, 0.17, 1), computeNormals=True, smooth=False)
p2.scale(0.0105*3, 0.022*3, 8)
p2.rotate(90, 1, 0, 0)
p2.rotate(grad, 0, 0, 1)
p2.translate(positionList[1][0], positionList[1][1], 0)
w.addItem(p2)

p3 = gl.GLSurfacePlotItem(z=np.transpose(arr[0]), shader='shaded', color=(0.54, 0.32, 0.17, 1), computeNormals=True, smooth=False)
p3.scale(0.0105*3, 0.022*3, 8)
p3.rotate(90, 1, 0, 0)
p3.rotate(grad*2, 0, 0, 1)
p3.translate(positionList[2][0], positionList[2][1], 0)
w.addItem(p3)

p4 = gl.GLSurfacePlotItem(z=np.transpose(arr[1]), shader='shaded', color=(0.54, 0.32, 0.17, 1), computeNormals=True, smooth=False)
p4.scale(0.0105*3, 0.022*3, 8)
p4.rotate(90, 1, 0, 0)
p4.rotate(grad*3, 0, 0, 1)
p4.translate(positionList[3][0], positionList[3][1], 0)
w.addItem(p4)

p5 = gl.GLSurfacePlotItem(z=np.transpose(arr[0]), shader='shaded', color=(0.54, 0.32, 0.17, 1), computeNormals=True, smooth=False)
p5.scale(0.0105*3, 0.022*3, 8)
p5.rotate(90, 1, 0, 0)
p5.rotate(grad*4, 0, 0, 1)
p5.translate(positionList[4][0], positionList[4][1], 0)
w.addItem(p5)

p6 = gl.GLSurfacePlotItem(z=np.transpose(arr[1]), shader='shaded', color=(0.54, 0.32, 0.17, 1), computeNormals=True, smooth=False)
p6.scale(0.0105*3, 0.022*3, 8)
p6.rotate(90, 1, 0, 0)
p6.rotate(grad*5, 0, 0, 1)
p6.translate(positionList[5][0], positionList[5][1], 0)
w.addItem(p6)

p7 = gl.GLSurfacePlotItem(z=np.transpose(arr[0]), shader='shaded', color=(0.54, 0.32, 0.17, 1), computeNormals=True, smooth=False)
p7.scale(0.0105*3, 0.022*3, 8)
p7.rotate(90, 1, 0, 0)
p7.rotate(grad*6, 0, 0, 1)
p7.translate(positionList[6][0], positionList[6][1], 0)
w.addItem(p7)

p8 = gl.GLSurfacePlotItem(z=np.transpose(arr[1]), shader='shaded', color=(0.54, 0.32, 0.17, 1), computeNormals=True, smooth=False)
p8.scale(0.0105*3, 0.022*3, 8)
p8.rotate(90, 1, 0, 0)
p8.rotate(grad*7, 0, 0, 1)
p8.translate(positionList[7][0], positionList[7][1], 0)
w.addItem(p8)

p9 = gl.GLSurfacePlotItem(z=np.transpose(arr[0]), shader='shaded', color=(0.54, 0.32, 0.17, 1), computeNormals=True, smooth=False)
p9.scale(0.0105*3, 0.022*3, 8)
p9.rotate(90, 1, 0, 0)
p9.rotate(grad*8, 0, 0, 1)
p9.translate(positionList[8][0], positionList[8][1], 0)
w.addItem(p9)

p10 = gl.GLSurfacePlotItem(z=np.transpose(arr[1]), shader='shaded', color=(0.54, 0.32, 0.17, 1), computeNormals=True, smooth=False)
p10.scale(0.0105*3, 0.022*3, 8)
p10.rotate(90, 1, 0, 0)
p10.rotate(grad*9, 0, 0, 1)
p10.translate(positionList[9][0], positionList[9][1], 0)
w.addItem(p10)

p11 = gl.GLSurfacePlotItem(z=np.transpose(arr[0]), shader='shaded', color=(0.54, 0.32, 0.17, 1), computeNormals=True, smooth=False)
p11.scale(0.0105*3, 0.022*3, 8)
p11.rotate(90, 1, 0, 0)
p11.rotate(grad*10, 0, 0, 1)
p11.translate(positionList[10][0], positionList[10][1], 0)
w.addItem(p11)

p12 = gl.GLSurfacePlotItem(z=np.transpose(arr[1]), shader='shaded', color=(0.54, 0.32, 0.17, 1), computeNormals=True, smooth=False)
p12.scale(0.0105*3, 0.022*3, 8)
p12.rotate(90, 1, 0, 0)
p12.rotate(grad*11, 0, 0, 1)
p12.translate(positionList[11][0], positionList[11][1], 0)
w.addItem(p12)

p13 = gl.GLSurfacePlotItem(z=np.transpose(arr[0]), shader='shaded', color=(0.54, 0.32, 0.17, 1), computeNormals=True, smooth=False)
p13.scale(0.0105*3, 0.022*3, 8)
p13.rotate(90, 1, 0, 0)
p13.rotate(grad*12, 0, 0, 1)
p13.translate(positionList[12][0], positionList[12][1], 0)
w.addItem(p13)

p14 = gl.GLSurfacePlotItem(z=np.transpose(arr[1]), shader='shaded', color=(0.54, 0.32, 0.17, 1), computeNormals=True, smooth=False)
p14.scale(0.0105*3, 0.022*3, 8)
p14.rotate(90, 1, 0, 0)
p14.rotate(grad*13, 0, 0, 1)
p14.translate(positionList[13][0], positionList[13][1], 0)
w.addItem(p14)

p15 = gl.GLSurfacePlotItem(z=np.transpose(arr[0]), shader='shaded', color=(0.54, 0.32, 0.17, 1), computeNormals=True, smooth=False)
p15.scale(0.0105*3, 0.022*3, 8)
p15.rotate(90, 1, 0, 0)
p15.rotate(grad*14, 0, 0, 1)
p15.translate(positionList[14][0], positionList[14][1], 0)
w.addItem(p15)

p16 = gl.GLSurfacePlotItem(z=np.transpose(arr[1]), shader='shaded', color=(0.54, 0.32, 0.17, 1), computeNormals=True, smooth=False)
p16.scale(0.0105*3, 0.022*3, 8)
p16.rotate(90, 1, 0, 0)
p16.rotate(grad*15, 0, 0, 1)
p16.translate(positionList[15][0], positionList[15][1], 0)
w.addItem(p16)

p17 = gl.GLSurfacePlotItem(z=np.transpose(arr[0]), shader='shaded', color=(0.54, 0.32, 0.17, 1), computeNormals=True, smooth=False)
p17.scale(0.0105*3, 0.022*3, 8)
p17.rotate(90, 1, 0, 0)
p17.rotate(grad*16, 0, 0, 1)
p17.translate(positionList[16][0], positionList[16][1], 0)
w.addItem(p17)

p18 = gl.GLSurfacePlotItem(z=np.transpose(arr[1]), shader='shaded', color=(0.54, 0.32, 0.17, 1), computeNormals=True, smooth=False)
p18.scale(0.0105*3, 0.022*3, 8)
p18.rotate(90, 1, 0, 0)
p18.rotate(grad*17, 0, 0, 1)
p18.translate(positionList[17][0], positionList[17][1], 0)
w.addItem(p18)

p19 = gl.GLSurfacePlotItem(z=np.transpose(arr[0]), shader='shaded', color=(0.54, 0.32, 0.17, 1), computeNormals=True, smooth=False)
p19.scale(0.0105*3, 0.022*3, 8)
p19.rotate(90, 1, 0, 0)
p19.rotate(grad*18, 0, 0, 1)
p19.translate(positionList[18][0], positionList[18][1], 0)
w.addItem(p19)

p20 = gl.GLSurfacePlotItem(z=np.transpose(arr[1]), shader='shaded', color=(0.54, 0.32, 0.17, 1), computeNormals=True, smooth=False)
p20.scale(0.0105*3, 0.022*3, 8)
p20.rotate(90, 1, 0, 0)
p20.rotate(grad*19, 0, 0, 1)
p20.translate(positionList[19][0], positionList[19][1], 0)
w.addItem(p20)

p21 = gl.GLSurfacePlotItem(z=np.transpose(arr[0]), shader='shaded', color=(0.54, 0.32, 0.17, 1), computeNormals=True, smooth=False)
p21.scale(0.0105*3, 0.022*3, 8)
p21.rotate(90, 1, 0, 0)
p21.rotate(grad*20, 0, 0, 1)
p21.translate(positionList[20][0], positionList[20][1], 0)
w.addItem(p21)

p22 = gl.GLSurfacePlotItem(z=np.transpose(arr[1]), shader='shaded', color=(0.54, 0.32, 0.17, 1), computeNormals=True, smooth=False)
p22.scale(0.0105*3, 0.022*3, 8)
p22.rotate(90, 1, 0, 0)
p22.rotate(grad*21, 0, 0, 1)
p22.translate(positionList[21][0], positionList[21][1], 0)
w.addItem(p22)

p23 = gl.GLSurfacePlotItem(z=np.transpose(arr[0]), shader='shaded', color=(0.54, 0.32, 0.17, 1), computeNormals=True, smooth=False)
p23.scale(0.0105*3, 0.022*3, 8)
p23.rotate(90, 1, 0, 0)
p23.rotate(grad*22, 0, 0, 1)
p23.translate(positionList[22][0], positionList[22][1], 0)
w.addItem(p23)








# Start Qt event loop unless running in interactive mode.
if __name__ == '__main__':

    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()

