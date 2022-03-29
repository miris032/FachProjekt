import Werkzeug
import Werkstück
import Animation
import readCSV
import numpy as np


def abstand(p1, p2, p3, q1, q2, q3):
    ergebnis = np.sqrt((q1 - p1) ** 2 + (q2 - p2) ** 2 + (q3 - p3) ** 2)
    return ergebnis


def gerade(p1, p2, p3, q1, q2, q3):
    vektoren = []
    ov = [p1, p2, p3]
    rv = [q1 - p1, q2 - p2, q3 - p3]
    vektoren.append(ov)
    vektoren.append(rv)
    return vektoren


def start(laengews, breite, hoehe, laengewz, durchmesser, aufloesung):
    ws = Werkstück.Werkstück(hoehe, laengews, breite, aufloesung)
    wz = Werkzeug.Werkzeug(laengewz, durchmesser, aufloesung)

    ablauf = readCSV.getPosFromCsv()

    for i in range(0, len(ablauf) - 1, 1):
        # wenn der abstand zum vorherigen Punkt des Werkzeugs zu groß ist, muss ein Zwischenschritt eingefügt werden
        distanz = abstand(ablauf[i][0], ablauf[i][1], ablauf[i][2], ablauf[i + 1][0], ablauf[i + 1][1],
                          ablauf[i + 1][2])
        if distanz > (durchmesser / 2):
            split = 2
            toolarge = True
            while toolarge:
                distanz = distanz / 2
                split = split + 1
                if distanz <= (durchmesser / 2):
                    toolarge = False

            factor = 1 / split
            geradengl = gerade(ablauf[i][0], ablauf[i][1], ablauf[i][2], ablauf[i + 1][0], ablauf[i + 1][1],
                               ablauf[i + 1][2])
            temp = []
            temp[0][0] = geradengl[0][0] + factor * geradengl[1][0]
            temp[0][1] = geradengl[0][1] + factor * geradengl[1][1]
            temp[0][2] = geradengl[0][2] + factor * geradengl[1][2]
            temp[0][3] = ablauf[i][3]
            temp[0][4] = ablauf[i][4]
            ablauf.insert(i + 1, temp)

    animation = Animation.Animation(ws, wz, ablauf, 0)


if __name__ == '__main__':
    start(70, 70, 30, 30, 8, 10)
