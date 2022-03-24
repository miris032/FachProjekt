import numpy as np

class Linie():

    # Ortsvektor und Richtungsvektor = nparray[3], parameter = nparray[0,1]
    # Achtung: Richtungsvektor muss normiert werden
    def __init__(self,ortsvektor,richtungsvektor,parameter, richtung):
        self.ortsvektor = ortsvektor
        self.richtungsvektor = richtungsvektor
        self.parameter = parameter
        self.richtung = richtung

    #Getter und Setter

    def getOrtsvektor(self):
        return self.ortsvektor

    def getRichtungsvektor(self):
        return self.richtungsvektor

    def getParameter(self):
        return self.parameter

    def getRichtung(self):
        return self.richtung

    def setOrtsvektor(self, value):
        self.ortsvektor = value

    def setRichtungsvektor(self,value):
        self.richtungsvektor = value

    def setParameter(self,value):
        self.Parameter = value

    def setRichtung(self,value):
        self.richtung = value

    #Methoden

    def schneide(self, gerade):
        # Geraden sind parallel:
        if self.richtung == gerade.richtung:
            zeile1 = np.empty(3, dtype= float)
            zeile2 = np.empty(3, dtype= float)
            zeile3 = np.empty(3, dtype= float)

            zeile1[1] = 0 - self.richtungsvektor[0]
            zeile2[1] = 0 - self.richtungsvektor[1]
            zeile3[1] = 0 - self.richtungsvektor[2]

            zeile1[0] = gerade.richtungsvektor[0]
            zeile2[0] = gerade.richtungsvektor[1]
            zeile3[0] = gerade.richtungsvektor[2]

            zeile1[2] = self.ortsvektor[0] - gerade.ortsvektor[0]
            zeile2[2] = self.ortsvektor[1] - gerade.ortsvektor[1]
            zeile3[2] = self.ortsvektor[2] - gerade.ortsvektor[2]

            if()
        # Geraden schneiden sich im rechten Winkel:


    def verschiebe(self,value):
        self.ortsvektor[0] = self.ortsvektor[0] + value[0]
        self.ortsvektor[1] = self.ortsvektor[1] + value[1]
        self.ortsvektor[2] = self.ortsvektor[2] + value[2]

    def getKoordinaten(self):
        ausgabe = np.empty(len(self.parameter)*3,dtype = float)

        for i in range(0,len(ausgabe),3):
            ausgabe[i] = self.ortsvektor[0] + self.parameter[i/3] * self.richtungsvektor[0]
            ausgabe[i+1] = self.ortsvektor[1] + self.parameter[i/3] * self.richtungsvektor[1]
            ausgabe[i+2] = self.ortsvektor[2] + self.parameter[i/3] *  self.richtungsvektor[2]

        return ausgabe


