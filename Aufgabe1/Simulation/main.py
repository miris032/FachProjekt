import Werkzeug
import Werkstück
import Animation
import readCSV
import numpy as np


def start(laengews, breite, hoehe, aufloesung, laengewz, durchmesser):

    ws = Werkstück.Werkstück(hoehe, laengews, breite, aufloesung)
    wz = Werkzeug.Werkzeug(laengewz, durchmesser, aufloesung)

    ablauf = readCSV.getPosFromCsv()
    animation = Animation.Animation(ws, wz, ablauf, 0)


