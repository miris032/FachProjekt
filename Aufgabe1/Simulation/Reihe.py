import numpy as np
import Linie

class Reihe():

    def __init__(self, richtung, row):
        self.richtung = richtung
        self.row = row

    #Getter und Setter

    def getRow(self):
        return self.row

    def getRichtung(self):
        return self.richtung

    def setRichtung(self, value):
        self.richtung = value

    def setRow(self,value):
        self.row = value

    # Methoden

    def getKoordinaten(self):
        ausgabe = np.empty(len(self.row)*3,dtype = int)
        count = 0
        for gerade in self.row:
            fill = gerade.getKoordinaten()
            ausgabe[count] = fill[count]
            ausgabe[count + 1] = fill[count + 1]
            ausgabe[count + 2] = fill[count + 2]
            count = count + 3

        return ausgabe

    def verschiebe(self,value):
        for gerade in self.row:
            gerade.verschiebe(value)

    def schneide(self, value):
        for gerade in self.row:
            value.schneide(gerade)
