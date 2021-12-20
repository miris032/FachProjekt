import sys
import pyqtgraph
from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph.opengl as gl
import numpy as np




## Create a GL View widget to display data 即w是主世界，需要往w里面陆续添加object
app = QtGui.QApplication([])
w = gl.GLViewWidget()

w.setWindowTitle('demo')
# w.setFixedSize(800, 600)
w.setBackgroundColor(pyqtgraph.mkColor(32, 32, 32))
w.setCameraPosition(distance=500)
w.show()

# 坐标系
g = gl.GLGridItem()
g.scale(20, 20, 10)
g.setDepthValue(10)  # draw grid after surfaces since they may be translucent
g.translate(0, 0, -32)
w.addItem(g)


data = np.fromfunction(psi, (100, 100, 200))
d2 = np.empty(data.shape + (4,), dtype=np.ubyte)

v = gl.GLVolumeItem(d2)
v.translate(-50, -50, -100)
w.addItem(v)








if __name__ == '__main__':

    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()