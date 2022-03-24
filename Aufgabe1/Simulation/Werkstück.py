import numpy as np
import Reihe

class Werkstück():

    def __init__(self,höhe,länge,breite,auflösung,ortsvektor,dexelX,dexelY,dexelZ,grenze):
        self.höhe = höhe
        self.länge = länge
        self.breite = breite
        self.auflösung = auflösung
        self.ortsvektor = ortsvektor
        self.dexelX = dexelX
        self.dexelY = dexelY
        self.dexelZ = dexelZ
        self.grenze = grenze

    # Getter und Setter

    def getHöhe(self):
        return self.Höhe

    def getLänge(self):
        return self.länge

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

    def setLänge(self,value):
        self.länge = value

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

    def verschiebe(self):
        return 1

    def getHülle(self):
        return 1

    def schneide(self):
        return 1

    #Hier sollen die Dexel erstellt werden

    def initialisiere(self):

        ini = np.empty(self.auflösung * self.auflösung)
        para = 0

        normalX = np.empty(3, dtype= float)
        normalX[0] = self.länge
        normalX[1] = 0
        normalX[2] = 0

        normalY = np.empty(3, dtype= float)
        normalY[0] = 0
        normalY[1] = self.breite
        normalY[2] = 0

        normalZ = np.empty(3, dtype= float)
        normalZ[0] = 0
        normalZ[1] = 0
        normalZ[2] = self.höhe

        for i in range(0,self.auflösung,1):
            for j in range(0,self.auflösung,1):
                ini[i+i*j] =







