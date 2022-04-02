import numpy as np
import math
import Linie
import Reihe

class Werkzeug():

    def __init__(self,höhe,breite,auflösung):
        self.höhe = höhe
        self.breite = breite
        self.auflösung = auflösung
        self.dexelX = []
        self.dexelY = []
        self.dexelZ = []

        # Normalenvektoren erstellen
        normalX = np.array(self.breite,0,0)
        normalY = np.array(0,self.breite,0)
        normalZ = np.array(0,0,self.höhe)

        kreis = np.empty(auflösung*2*3,dtype = float)

        for i in range(0,len(kreis),6):
            kreis[i]   = math.cos(((i/auflösung)*(math.pi*2))/(math.pi*2))
            kreis[i+1] = math.sin(((i/auflösung)*(math.pi*2))/(math.pi*2))
            kreis[i+2] = 0
            kreis[i+3] = math.cos(((i/auflösung)*(math.pi*2))/(math.pi*2) + math.pi)
            kreis[i+4] = math.sin(((i/auflösung)*(math.pi*2))/(math.pi*2) + math.pi)
            kreis[i+5] = 0



    # Getter und Setter

    def getHöhe(self):
        return self.Höhe

    def getBreite(self):
        return self.breite

    def getOrtsvektor(self):
        return self.ortsvektor

    def getDexelX(self):
        return self.dexelX

    def getDexelY(self):
        return self.dexelY

    def getDexelZ(self):
        return self.dexelZ

    def getGrenze(self):
        return self.grenze

    def setHöhe(self,value):
        self.höhe = value

    def setBreite(self, value):
        self.breite = value

    def setAuflösung(self, value):
        self.auflösung = value

    def setOrtsvektor(self,value):
        self.ortsvektor = value

    def setDexelX(self,value):
        self.dexelX = value

    def setDexelY(self,value):
        self.dexelY = value

    def setDexelZ(self,value):
        self.dexelZ = value

    def setGrenze(self,value):
        self.grenze = value

    # Methoden

    # Verschiebt das WErkstück um value, nparray 3D, dtype=float
    def verschiebe(self,value):
        for reihen in self.dexelX:
            reihen.verschiebe(value)
        for reihen in self.dexelY:
            reihen.verschiebe(value)
        for reihen in self.dexelZ:
            reihen.verschiebe(value)

    #Gibt die Koordinaten der Hülle des Werkzeuges aus
    def getHülle(self):
        ausgabe = np.array([], dtype = float)
        ausgabe = self.dexelX[0]

        for i in range(1,len(self.dexelX),1):
            ausgabe = np.concatenate(Reihe.getKoordinaten(self.dexelX[i]),ausgabe)
        for i in range(0,len(self.dexelY),1):
            ausgabe = np.concatenate(Reihe.getKoordinaten(self.dexelY[i]),ausgabe)
        for i in range(0,len(self.dexelZ),1):
            ausgabe = np.concatenate(Reihe.getKoordinaten(self.dexelZ[i]),ausgabe)

        return ausgabe

