import numpy as np

class Linie():

    # Ortsvektor und Richtungsvektor = nparray[3], parameter = nparray[0,1]
    # Achtung: Richtungsvektor muss normiert werden
    def __init__(self,ortsvektor,richtungsvektor,parameter):
        self.ortsvektor = ortsvektor
        self.richtungsvektor = richtungsvektor
        self.parameter = parameter

    #Getter und Setter

    def getOrtsvektor(self):
        return self.ortsvektor

    def getRichtungsvektor(self):
        return self.richtungsvektor

    def getParameter(self):
        return self.parameter

    def setOrtsvektor(self, value):
        self.ortsvektor = value

    def setRichtungsvektor(self,value):
        self.richtungsvektor = value

    def setParameter(self,value):
        self.Parameter = value

    #Methoden

    def schneide(self, value):
        # Geraden sind parallel:
        if np.array_equal(self.richtungsvektor, value.richtungsvektor):
            return 1
        # Geraden schneiden sich im rechten Winkel:


    def verschiebe(self,value):
        self.ortsvektor[0] = self.ortsvektor[0] + value[0]
        self.ortsvektor[1] = self.ortsvektor[1] + value[1]
        self.ortsvektor[2] = self.ortsvektor[2] + value[2]

    def getKoordinaten(self):
        ausgabe = np.empty(len(self.parameter)*3,dtype = int)

        for i in range(0,len(ausgabe),3):
            ausgabe[i] = self.ortsvektor[0] + self.richtungsvektor[0]
            ausgabe[i+1] = self.ortsvektor[1] + self.richtungsvektor[1]
            ausgabe[i+2] = self.ortsvektor[2] + self.richtungsvektor[2]

        return ausgabe


