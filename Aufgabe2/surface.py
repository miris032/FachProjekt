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
    color=(0.1, 0.5, 1, 1),
    shader='shaded',
    glOptions="additive",
)
w.addItem(m1)

"""get all positions of each fragment"""
def getPositionList(x, y):
    # grad = 1.638212727*2
    grad = 1.595 * 2
    sin = math.sin(math.radians(grad))
    cos = math.cos(math.radians(grad))
    positionList = [(x, y)]
    for i in range(9):
        Xnew = positionList[i][0] * cos - positionList[i][1] * sin
        Ynew = positionList[i][0] * sin + positionList[i][1] * cos
        positionList.append((Xnew, Ynew))
    return positionList


"""topography"""
dataList = np.array(readData.getData())
dataList = np.transpose(dataList)
arr = np.array_split(dataList, 10)

# z1 = ndi.gaussian_filter(arr[0], (0.5, 0.5))
print(arr[0].shape)

grad = 1.638212727 * 2
positionList = getPositionList(-2.145, -75)



# @jit(parallel=True)
'''def aaa():
    p1 = gl.GLSurfacePlotItem(z=arr[0], shader='shaded', color=(0.1, 0.5, 1, 1))
    p1.scale(0.031, 0.031, 5)  # 0.066
    p1.rotate(90, 1, 0, 0)
    p1.translate(positionList[0][0], positionList[0][1], 0)
    for i in range(10):

        w.addItem(p1)

aaa()'''



start = time.time()

p1 = gl.GLSurfacePlotItem(z=arr[0], shader='shaded', color=(0.1, 0.5, 1, 1))
p1.scale(0.031, 0.031, 5)  # 0.066
p1.rotate(90, 1, 0, 0)
p1.translate(positionList[0][0], positionList[0][1], 0)
w.addItem(p1)

p2 = gl.GLSurfacePlotItem(z=arr[1], shader='shaded', color=(0.1, 0.5, 1, 1))
p2.scale(0.031, 0.031, 5)
p2.rotate(90, 1, 0, 0)
p2.rotate(grad, 0, 0, 1)
p2.translate(positionList[1][0], positionList[1][1], 0)
w.addItem(p2)

p3 = gl.GLSurfacePlotItem(z=arr[2], shader='shaded', color=(0.1, 0.5, 1, 1))
p3.scale(0.031, 0.031, 5)
p3.rotate(90, 1, 0, 0)
p3.rotate(grad*2, 0, 0, 1)
p3.translate(positionList[2][0], positionList[2][1], 0)
w.addItem(p3)

p4 = gl.GLSurfacePlotItem(z=arr[3], shader='shaded', color=(0.1, 0.5, 1, 1))
p4.scale(0.031, 0.031, 5)
p4.rotate(90, 1, 0, 0)
p4.rotate(grad*3, 0, 0, 1)
p4.translate(positionList[3][0], positionList[3][1], 0)
w.addItem(p4)

p5 = gl.GLSurfacePlotItem(z=arr[4], shader='shaded', color=(0.1, 0.5, 1, 1))
p5.scale(0.031, 0.031, 5)
p5.rotate(90, 1, 0, 0)
p5.rotate(grad*4, 0, 0, 1)
p5.translate(positionList[4][0], positionList[4][1], 0)
w.addItem(p5)

p6 = gl.GLSurfacePlotItem(z=arr[5], shader='shaded', color=(0.1, 0.5, 1, 1))
p6.scale(0.031, 0.031, 5)
p6.rotate(90, 1, 0, 0)
p6.rotate(grad*5, 0, 0, 1)
p6.translate(positionList[5][0], positionList[5][1], 0)
w.addItem(p6)

p7 = gl.GLSurfacePlotItem(z=arr[6], shader='shaded', color=(0.1, 0.5, 1, 1))
p7.scale(0.031, 0.031, 5)
p7.rotate(90, 1, 0, 0)
p7.rotate(grad*6, 0, 0, 1)
p7.translate(positionList[6][0], positionList[6][1], 0)
w.addItem(p7)

p8 = gl.GLSurfacePlotItem(z=arr[7], shader='shaded', color=(0.1, 0.5, 1, 1))
p8.scale(0.031, 0.031, 5)
p8.rotate(90, 1, 0, 0)
p8.rotate(grad*7, 0, 0, 1)
p8.translate(positionList[7][0], positionList[7][1], 0)
w.addItem(p8)

p9 = gl.GLSurfacePlotItem(z=arr[8], shader='shaded', color=(0.1, 0.5, 1, 1))
p9.scale(0.031, 0.031, 5)
p9.rotate(90, 1, 0, 0)
p9.rotate(grad*8, 0, 0, 1)
p9.translate(positionList[8][0], positionList[8][1], 0)
w.addItem(p9)

p10 = gl.GLSurfacePlotItem(z=arr[8], shader='shaded', color=(0.1, 0.5, 1, 1))
p10.scale(0.031, 0.031, 5)
p10.rotate(90, 1, 0, 0)
p10.rotate(grad*9, 0, 0, 1)
p10.translate(positionList[9][0], positionList[9][1], 0)
w.addItem(p10)

end = time.time()
print(f'Laufzeit: {end - start}s')








# Start Qt event loop unless running in interactive mode.
if __name__ == '__main__':

    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()

