import Werkzeug
import Werkstück
import Animation
import readCSV
import numpy as np


def start(laengeWs, breite, hoehe, aufloesung, laengeWz, durchmesser):
    ws = Werkstück(hoehe, laengeWs, breite, aufloesung)
    wz = Werkzeug(laengeWz, durchmesser, aufloesung)

    ablauf = readCSV.getPosFromCsv()
    animation = Animation(ws, wz, ablauf, 0)


