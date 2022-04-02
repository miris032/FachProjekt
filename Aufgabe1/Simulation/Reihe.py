import numpy as np
import Linie


class Reihe():

    # richtung = Ausrichtung des Normalenvektors, Zahl: 0 ist x-Richtung, 1 ist y-Richtung, 2 ist z-Richtung
    # row = Koordinaten der Reihe, Array der Länge 3, (x,y,z)
    # normal = Normalenvektor, Array der Länge 3, (x,y,z)
    # reih = Liste von Geraden, wird aktuell in initialize erstellt
    # Schar der Geraden

    def __init__(self, richtung, row, normal):
        self.richtung = richtung
        self.row = row
        self.normal = normal
        self.schar = []

        #initialisiere die Geraden
        for i in range(0,len(row),3):
            self.schar.append(Linie([row[i],row[i+1],row[i+2]],normal,np.array([0,1],dtype=float),richtung))



    # Getter und Setter

    def getRow(self):
        return self.row

    def getRichtung(self):
        return self.richtung

    def getNormal(self):
        return self.normal

    def getSchar(self):
        return self.schar

    def setRichtung(self, value):
        self.richtung = value

    def setRow(self, value):
        self.row = value

    def setNormal(self,value):
        self.normal = value

    def setSchar(self,value):
        self.schar = value

    # Methoden

    # Gibt alle Koordinaten der Reihe in einem Array zurück:
    # (x1,y1,z1,x2,y2,z2,x3,y3,z3,.....,xn,yn,zn) -> hat n Koordinaten

    def getKoordinaten(self):
        ausgabe = np.empty([], dtype=float)
        count = 0
        for gerade in self.schar:
            if(count == 0):
                ausgabe = Linie.getKoordinaten(gerade)
                count = count + 1
            if(count > 0):
                ausgabe = np.concatenate((ausgabe,Linie.getKoordinaten(gerade)))


        return ausgabe

    # Verschiebt alle Gerade der Reihe um value, value ist ein Array der Größe 3, (x,y,z)

    def verschiebe(self, value):
        for gerade in self.schar:
            Linie.verschiebe(gerade,value)

    # Schnitt einer Geraden mit einer Reihe
    # Es werden nur die Koordinaten der Geraden verändert
    # Die Koordinaten der Reihe bleiben
    # Also: Reihe -> Vom Werkstück, Gerade -> Vom Multidexelboard
    # geraden aus schar werden geschnitten

    def schneide(self, scharr):
        if(self.richtung == scharr.richtung):
            for gerade in np.asarray(self.schar):
                for geraden in np.asarray(Reihe.getSchar(scharr)):
                    Linie.schneideParallel(gerade,geraden)
        else:
            # Fall 1: Nur ein Schnittpunkt, dann schneide
            # Fall 2: Zwei Schnittpunkte:
            # Lösche Gerade aus self.schar
            # Füge zwei neue Geraden an dieser Stelle ein
            param = np.array([-1000000,-100000,-1000000], dtype = float)
            logic = np.array([-1000000,-100000], dtype = float)
            counter = 0
            position = -1
            for gerade in self.schar:
                position = position +1
                param[0] = -1000000
                param[1] = -1000000
                counter = 0
                for geraden in Reihe.getSchar(scharr):
                    logic = Linie.hatSchnittpunkt(gerade,geraden)
                    if(logic[0] > -1):
                        param[counter] = logic[1]
                        param[2] = position
                        counter = 1
                if(param[1] == -1000000):
                    Linie.schneideOrthogonal(gerade, param[0])
                elif(param[0] != -1000000 + param[1] != -1000000):
                    g1 = Linie(Linie.getOrtsvektor(gerade),Linie.getRichtungsvektor(gerade),np.array([0,min(param[0],param[1])],dtype=float))
                    g2 = Linie(Linie.getOrtsvektor(gerade),Linie.getRichtungsvektor(gerade),np.array([0,max(param[0],param[1])],dtype=float))
                    del self.schar[position]
                    self.schar.insert(position-1,g1)
                    self.schar.insert(position-1,g2)



