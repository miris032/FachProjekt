import numpy as np
import Linie

class Reihe():

    # richtung = Ausrichtung des Normalenvektors, Zahl: 0 ist z-Richtung, 1 ist y-Richtung, 2 ist x-Richtung
    # row = Koordinaten der Reihe, Array der Länge 3, (x,y,z)
    # normal = Normalenvektor, Array der Länge 3, (x,y,z)
    # reih = Liste von Geraden, wird aktuell in initialize erstellt


    def __init__(self, richtung, row, normal):
        self.richtung = richtung
        self.row = row
        self.normal = normal
        self.reih

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

    # Gibt alle Koordinaten der Reihe in einem Array zurück:
    # (x1,y1,z1,x2,y2,z2,x3,y3,z3,.....,xn,yn,zn) -> hat n Koordinaten

    def getKoordinaten(self):
        ausgabe = np.empty(len(self.row)*3,dtype = float)
        count = 0
        for gerade in self.row:
            fill = gerade.getKoordinaten()
            ausgabe[count] = fill[count]
            ausgabe[count + 1] = fill[count + 1]
            ausgabe[count + 2] = fill[count + 2]
            count = count + 3

        return ausgabe

    # Verschiebt alle Gerade der Reihe um value, value ist ein Array der Größe 3, (x,y,z)

    def verschiebe(self,value):
        for gerade in self.row:
            gerade.verschiebe(value)

    # Schnitt einer Geraden mit einer Reihe
    # Es werden nur die Koordinaten der Geraden verändert
    # Die Koordinaten der Reihe bleiben
    # Also: Reihe -> Vom Werkstück, Gerade -> Vom Multidexelboard

    def schneide(self, value):
        for gerade in self.row:
            value.schneide(gerade)

    # Hier werden die Geraden der Reihe erstellt
    # An jede der übergebenen Koordinaten in row
    # wird ein Richtungsvektor (normal) angesetzt
    # mit den Parametern 0, 1 hält man die Koordinaten
    # richtung beschreibt wie oben ob es Richtung x-Achse oder .. zeigt

    def initialize(self):
        count = 0
        ortsvektor = np.empty(3,dtype = float)
        parameter = np.empty(2, dtype = float)
        parameter[0] = 0
        parameter[1] = 1
        for i in range(0,len(self.row),1):
            ortsvektor[0] = self.row[count]
            ortsvektor[1] = self.row[count+1]
            ortsvektor[2] = self.row[count+2]
            count = count + 3
            self.reih.append(Linie(ortsvektor,self.normal, parameter, self.richtung))





