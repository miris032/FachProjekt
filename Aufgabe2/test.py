import math


def getPositionList(x, y):
    grad = 1.638212727*2
    sin = math.sin(math.radians(grad))
    cos = math.cos(math.radians(grad))
    positionList = [(x, y)]
    for i in range(9):
        Xnew = positionList[i][0] * cos - positionList[i][1] * sin
        Ynew = positionList[i][0] * sin + positionList[i][1] * cos
        positionList.append((Xnew, Ynew))
    return positionList


if __name__ == '__main__':
    print(getPositionList(-2.145, -75))
    """
    (2.144999999216686, -75.00000000002241)
    (6.427987637469273, -74.754812553658)
    (10.689961117398706, -74.26523921935824)
    (14.916987340416824, -73.53288049359854)
    (19.095247456317875, -72.56013057858969)
    (23.21108203939309, -71.35016955523346)
    (27.25103574336015, -69.90695298691047)
    (31.201901289123096, -68.23519898808695)
    (35.050762641559494, -66.34037280001569)
    """