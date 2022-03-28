import itertools
import numpy as np


# n只能是偶数
def getPoints(n):
    pointsList = np.array(list(itertools.product(range(0, n, 1), repeat=3)))

    # 2D to 3D
    pointsList3D = pointsList.reshape((-1, n, 3))
    pointsList_deleteHalbs = np.split(pointsList3D, 2, axis=1)
    return pointsList_deleteHalbs[0]


def getEdges(n):
    pointList = getPoints(n)
    listNum, pointNumPerList = pointList.shape[0], pointList.shape[1]

    indexsList = list(range(0, listNum*pointNumPerList-1, 1))
    indexsList_2D = list()

    counter = 0

    for i in indexsList:
        if counter < pointNumPerList:
            edge = [i, i + 1]
            indexsList_2D.append(edge)
            counter += 1
        else:
            counter = 0


    return indexsList_2D





if __name__ == '__main__':
    '''liste = getPoints(6)
    print(liste)
    print(liste.shape)

    print(getEdges(6))'''

    pointsList = np.array(list(itertools.product(range(0, 6, 1), repeat=3)))
    print(pointsList)
