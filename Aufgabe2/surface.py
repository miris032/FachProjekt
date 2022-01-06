from pyqtgraph.Qt import QtCore, QtGui
from OpenGL.arrays import vbo
import pyqtgraph as pg
import pyqtgraph.opengl as gl
import scipy.ndimage as ndi
import numpy as np
import pyqtgraph
import sys
import readData



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
g.scale(20, 20, 10)
g.setDepthValue(10)  # draw grid after surfaces since they may be translucent
w.addItem(g)


"""Cylinder"""
r = 7.5*10
h = 10*10
cylinder = gl.MeshData.cylinder(rows=10, cols=20, radius=[r, r], length=h)
m1 = gl.GLMeshItem(
    meshdata=cylinder,
    smooth=True,
    # smooth=False,
    color=(1, 1, 1, 0.5),
    # shader="balloon",
    glOptions="additive",
)
w.addItem(m1)


"""topography"""
dataList = np.array(readData.getData())
dataList = np.transpose(dataList)
arr = np.array_split(dataList, 10)

# z1 = ndi.gaussian_filter(arr[0], (0.5, 0.5))
p1 = gl.GLSurfacePlotItem(z=arr[0], shader='shaded', color=(0.1, 0.5, 1, 1))
p1.scale(2*16. / 490., 2*16. / 490., 20)
p1.rotate(90, 1, 0, 0)
p1.rotate(136, 0, 0, 1)
p1.translate(53, 53, 50)
w.addItem(p1)

p2 = gl.GLSurfacePlotItem(z=arr[1], shader='shaded', color=(0.1, 0.5, 1, 1))
p2.scale(2*16. / 490., 2*16. / 490., 20)
p2.rotate(90, 1, 0, 0)
p2.rotate(151, 0, 0, 1)
p2.translate(47, 58, 50)
w.addItem(p2)

p3 = gl.GLSurfacePlotItem(z=arr[2], shader='shaded', color=(0.1, 0.5, 1, 1))
p3.scale(2* 16. / 490., 2* 16. / 490., 20)
p3.rotate(90, 1, 0, 0)
p3.rotate(166, 0, 0, 1)
p3.translate(41, 63, 50)
w.addItem(p3)

p4 = gl.GLSurfacePlotItem(z=arr[3], shader='shaded', color=(0.1, 0.5, 1, 1))
p4.scale(2* 16. / 490., 2* 16. / 490., 20)
p4.rotate(90, 1, 0, 0)
p4.rotate(156, 0, 0, 1)
p4.translate(34, 66, 50)
w.addItem(p4)

p5 = gl.GLSurfacePlotItem(z=arr[4], shader='shaded', color=(0.1, 0.5, 1, 1))
p5.scale(2* 16. / 490., 2* 16. / 490., 20)
p5.rotate(90, 1, 0, 0)
p5.rotate(170, 0, 0, 1)
p5.translate(27, 70, 50)
w.addItem(p5)

p6 = gl.GLSurfacePlotItem(z=arr[5], shader='shaded', color=(0.1, 0.5, 1, 1))
p6.scale(2* 16. / 490., 2* 16. / 490., 20)
p6.rotate(90, 1, 0, 0)
p6.rotate(175, 0, 0, 1)
p6.translate(20, 72, 50)
w.addItem(p6)

p7 = gl.GLSurfacePlotItem(z=arr[6], shader='shaded', color=(0.1, 0.5, 1, 1))
p7.scale(2* 16. / 490., 2* 16. / 490., 20)
p7.rotate(90, 1, 0, 0)
p7.rotate(176, 0, 0, 1)
p7.translate(12, 73, 50)
w.addItem(p7)

p8 = gl.GLSurfacePlotItem(z=arr[7], shader='shaded', color=(0.1, 0.5, 1, 1))
p8.scale(2* 16. / 490., 2* 16. / 490., 20)
p8.rotate(90, 1, 0, 0)
p8.rotate(177, 0, 0, 1)
p8.translate(4, 74, 50)
w.addItem(p8)

p9 = gl.GLSurfacePlotItem(z=arr[8], shader='shaded', color=(0.1, 0.5, 1, 1))
p9.scale(2* 16. / 490., 2* 16. / 490., 20)
p9.rotate(90, 1, 0, 0)
p9.rotate(188, 0, 0, 1)
p9.translate(-4, 74, 50)
w.addItem(p9)

p10 = gl.GLSurfacePlotItem(z=arr[8], shader='shaded', color=(0.1, 0.5, 1, 1))
p10.scale(2* 16. / 490., 2* 16. / 490., 20)
p10.rotate(90, 1, 0, 0)
p10.rotate(192, 0, 0, 1)
p10.translate(-12, 73, 50)
w.addItem(p10)













# Start Qt event loop unless running in interactive mode.
if __name__ == '__main__':
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()




