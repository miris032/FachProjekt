# Hier soll das CSV Dokument eingelsen werden und
# in Verschiebungen umgerechnet werden, die dann an Animation übergeben werden

# Hier soll das Werkstück und das Werkzeug erstellt werden und an Animation
# übergeben werden

# Hier soll die Funktion Step und matplotlib benutzt werden um eine
# 3D Animation zu erstellen

import numpy as np
import Werkstück
import Werkzeug
import Animation

class Simulation():

    def __init__(self, ablauf):
        self.zylinder = Werkzeug(30,8,10,0.1991,0.3660,100,0,0,0,0)
        self.quader = Werkstück(70,30,30,10,0,0,0,0,0,0,0)
        self.animation = Animation(self.quader, self.zylinder, ablauf, 0 )
