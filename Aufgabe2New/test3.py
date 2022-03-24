import pyqtgraph as pg
import numpy as np
import math
from pyqtgraph.Qt import QtCore, QtGui

class Graph(pg.GraphItem):
    def __init__(self):
        self.dragPoint = None
        self.dragOffset = None
        self.textItems = []
        pg.GraphItem.__init__(self)
        self.scatter.sigClicked.connect(self.onclick)
        self.data = lambda x: None
        self.text = lambda x: None

    def setData(self, **kwds):
        self.text = kwds.pop('text', [])
        self.data = kwds
        if 'pos' in self.data:
            npts = self.data['pos'].shape[0]
            self.data['data'] = np.empty(npts, dtype=[('index', int)])
            self.data['data']['index'] = np.arange(npts)
        self.settexts(self.text)
        self.updategraph()

    def settexts(self, text):
        for i in self.textItems:
            i.scene().removeItem(i)
        self.textItems = []
        for t in text:
            item = pg.TextItem(t)
            self.textItems.append(item)
            item.setParentItem(self)

    def updategraph(self):
        pg.GraphItem.setData(self, **self.data)
        for i, item in enumerate(self.textItems):
            item.setPos(*self.data['pos'][i])

    def mouseDragEvent(self, ev):
        if ev.button() != QtCore.Qt.LeftButton:
            ev.ignore()
            return

        if ev.isStart():
            # We are already one step into the drag.
            # Find the point(s) at the mouse cursor when the button was first
            # pressed:
            pos = ev.buttonDownPos()
            pts = self.scatter.pointsAt(pos)
            if len(pts) == 0:
                ev.ignore()
                return
            self.dragPoint = pts[0]
            ind = pts[0].data()[0]
            self.dragOffset = self.data['pos'][ind] - pos
        elif ev.isFinish():
            self.dragPoint = None
            return
        else:
            if self.dragPoint is None:
                ev.ignore()
                return

        ind = self.dragPoint.data()[0]
        self.data['pos'][ind] = ev.pos() + self.dragOffset
        self.updategraph()
        ev.accept()

    # Once a node on the graph is clicked, the clicked node should become the center of the graph
    def onclick(plot, points):
        x = 0
        y = 0
        x, y = points.ptsClicked[0]._data[0], points.ptsClicked[0]._data[1]     # position of the clicked point
        print('Clicked point is (' + str(x) + ', ' + str(y) + ')')


# Construct a unit radius circle for the graph
def plot_poincare_disc(graph_item_1, graph_item_2):
    # Two semicircles have been produced first and then joined later
    # As PyQtGraph needs a position matrix along with an adjacency matrix, hence pos and adj arrays

    # Semi-Circle 1
    pos1 = []
    adj1 = []
    length = 0
    # calculating y coordinates for 1000 evenly spaced points in (-1,1)
    for x in np.linspace(-1, 1, 1000):
        y = math.sqrt(1 - x ** 2)
        pos1.append([x, y])
        if len(pos1) > 1:
            adj1.append([length - 1, length])
        length = length + 1

    pos1 = np.array(pos1)
    adj1 = np.array(adj1)
    graph_item_1.setData(pos=pos1, adj=adj1, size=0.07)

    # Semi-circle 2
    pos2 = []
    adj2 = []
    length = 0
    # calculating y coordinates for 1000 evenly spaced points in (1,-1)
    for x in np.linspace(1, -1, 1000):
        y = -math.sqrt(1 - x ** 2)
        pos2.append([x, y])
        if len(pos2) > 1:
            adj2.append([length - 1, length])
        length = length + 1

    pos2 = np.array(pos2)
    adj2 = np.array(adj2)
    graph_item_2.setData(pos=pos2, adj=adj2, size=0.07)

if __name__ == '__main__':
    position = [(-0.5,0), (0.5,0)]
    adjacency = [(0,1)]

    w = pg.GraphicsWindow()
    w.setWindowTitle('Title of the window')
    v = w.addViewBox()
    v.setAspectLocked()
    g = Graph()
    v.addItem(g)

    g.setData(pos=np.array(position), adj=np.array(adjacency), pxMode=False, size=0.1)

    g2 = pg.GraphItem()
    #v.addItem(g2)
    g3 = pg.GraphItem()
    #v.addItem(g3)

    plot_poincare_disc(g2,g3)

    import sys

if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
    QtGui.QGuiApplication.instance().exec_()