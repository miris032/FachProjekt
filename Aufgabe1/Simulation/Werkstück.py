import numpy as np
import Reihe
import Werkzeug

class Werkstück():

    def __init__(self,höhe,länge,breite,auflösung):
        self.höhe = höhe
        self.länge = länge
        self.breite = breite
        self.auflösung = auflösung
        self.dexelX = []
        self.dexelY = []
        self.dexelZ = []

       #Initialisiere die Dexel

        # Normalenvektoren erstellen
        normalX = np.array(self.breite,0,0)
        normalY = np.array(0,self.länge,0)
        normalZ = np.array(0,0,self.höhe)

        # Ebenen erstellen, auf die die Normalenvektoren aufgesetzt werden
        xyE = np.empty(auflösung*auflösung*3,dtype = float)
        xzE = np.empty(auflösung*auflösung*3,dtype = float)
        zyE = np.empty(auflösung*auflösung*3,dtype = float)

        counter = 0
        for i in range(0,auflösung,1):
            for j in range(0,auflösung,1):
                xyE[counter]= i * (1/auflösung) * breite
                xyE[counter+1]= j * (1/auflösung) * länge
                xyE[counter+1]= 0

                xzE[counter] = i * (1/auflösung) * breite
                xzE[counter] = 0
                xzE[counter] = i * (1/auflösung) * höhe

                zyE[counter]= 0
                zyE[counter+1]= j * (1/auflösung) * länge
                zyE[counter+1]= i * (1/auflösung) * höhe

                counter = counter + 3
        # Reihen erstellen
        xyE = np.reshape(xyE,(auflösung,auflösung))
        xzE = np.reshape(xzE,(auflösung,auflösung))
        zyE = np.reshape(xyE,(auflösung,auflösung))

        for i in range(0,len(xyE),1):
            self.dexelZ.append(Reihe(2,xyE[i],normalZ))
            self.dexelY.append(Reihe(2,xzE[i],normalY))
            self.dexelX.append(Reihe(2,zyE[i],normalX))




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
    # Verschiebe das Werkstück value -> np-array, 3D, dtype=float
    def verschiebe(self,value):
        for reihen in self.dexelX:
            reihen.verschiebe(value)
        for reihen in self.dexelY:
            reihen.verschiebe(value)
        for reihen in self.dexelZ:
            reihen.verschiebe(value)
    # Gibt die Koordinaten der Hülle des Werkzeuges aus
    def getHülle(self):
        ausgabe = np.array([], dtype = float)
        ausgabe = self.dexelX[0]

        for i in range(1,len(self.dexelX),1):
            ausgabe = np.concatenate(Reihe.getKoordinaten(self.dexelX[i]),ausgabe)
        for i in range(0,len(self.dexelY),1):
            ausgabe = np.concatenate(Reihe.getKoordinaten(self.dexelY[i]),ausgabe)
        for i in range(0,len(self.dexelZ),1):
            ausgabe = np.concatenate(Reihe.getKoordinaten(self.dexelZ[i]),ausgabe)

    # Schneide jede Gerade des Werkstücks mit jeder Reihe des Werkzeuges
    def schneide(self, werkz):

        for i in range(0,len(self.dexelX),1):
            for j in range(0,len(Werkzeug.getDexelX(werkz)),1):
                Reihe.schneide(self.dexelX[i],Werkzeug.getDexelX(werkz)[j])

        for i in range(0,len(self.dexelX),1):
            for j in range(0,len(Werkzeug.getDexelY(werkz)),1):
                Reihe.schneide(self.dexelX[i],Werkzeug.getDexelY(werkz)[j])

        for i in range(0,len(self.dexelX),1):
            for j in range(0,len(Werkzeug.getDexelZ(werkz)),1):
                Reihe.schneide(self.dexelX[i],Werkzeug.getDexelZ(werkz)[j])

        for i in range(0,len(self.dexelY),1):
            for j in range(0,len(Werkzeug.getDexelX(werkz)),1):
                Reihe.schneide(self.dexelX[i],Werkzeug.getDexelX(werkz)[j])

        for i in range(0,len(self.dexelY),1):
            for j in range(0,len(Werkzeug.getDexelY(werkz)),1):
                Reihe.schneide(self.dexelX[i],Werkzeug.getDexelY(werkz)[j])

        for i in range(0,len(self.dexelY),1):
            for j in range(0,len(Werkzeug.getDexelZ(werkz)),1):
                Reihe.schneide(self.dexelX[i],Werkzeug.getDexelZ(werkz)[j])


        for i in range(0,len(self.dexelZ),1):
            for j in range(0,len(Werkzeug.getDexelX(werkz)),1):
                Reihe.schneide(self.dexelX[i],Werkzeug.getDexelX(werkz)[j])

        for i in range(0,len(self.dexelZ),1):
            for j in range(0,len(Werkzeug.getDexelY(werkz)),1):
                Reihe.schneide(self.dexelX[i],Werkzeug.getDexelY(werkz)[j])

        for i in range(0,len(self.dexelZ),1):
            for j in range(0,len(Werkzeug.getDexelZ(werkz)),1):
                Reihe.schneide(self.dexelX[i],Werkzeug.getDexelZ(werkz)[j])







