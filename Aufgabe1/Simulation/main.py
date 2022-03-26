import Werkzeug
import Werkstück
import Animation
import readCSV
import numpy as np


def start(laengews, breite, hoehe, laengewz, durchmesser, aufloesung):
    ws = Werkstück.Werkstück(hoehe, laengews, breite, aufloesung)
    wz = Werkzeug.Werkzeug(laengewz, durchmesser, aufloesung)

    ablauf = readCSV.getPosFromCsv()

    for i in range(1, len(ablauf), 1):
        # wenn der abstand zum vorherigen Punkt des Werkzeugs zu groß ist, muss ein Zwischenschritt eingefügt werden
        if

    animation = Animation.Animation(ws, wz, ablauf, 0)


if __name__ == '__main__':
    start(70, 70, 30, 30, 8, 10)
