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

    def schneideParallel(self, gerade):
        # Fall1: Geraden sind parallel
        # Erstelle das Lineare Gleichungssystem
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
            # Prüfe ob beim LGS zwei vollständige Nullzeilen entstehen
            # Dann sind die Geraden parallel und es existieren unendlich viele Lösungen
            # Dann schneide die Gerade vom Werkstück an der Stelle der Spitze des Geradenstücks
            # vom Werkzeug
            if(zeile2[0] * zeile1[1] - zeile1[0]*zeile2[1] == 0):
                if(zeile3[0] * zeile1[1] - zeile1[0]*zeile3[1] == 0):
                    if(zeile2[0]*zeile1[3] - zeile1[0]*zeile2[2] == 0):
                        if(zeile3[0]*zeile1[3] - zeile1[0]*zeile3[2] == 0):
                    schnitt = np.empty(2,dtype= float)
                    schnitt[0] = gerade.ortsvektor[0] + gerade.parameter[1] * gerade.richtungsvektor[0]
                    schnitt[1] = (schnitt[0] - self.ortsvektor[0]) / self.richtungsvektor[0]
                    if((schnitt[1] > 0)  + (schnitt[1] < 1)):
                        self.parameter[len(self.parameter)] = schnitt[1]

    # Prüft ob sich die Geraden schneiden und gibt bei erfolg den Parameter
    # zurück, ansonsten eine große Zahl
    def hatSchnittpunkt(self,gerade):

        if self.richtung != gerade.richtung:
            #Erstelle das Lineare Gleichungssystem
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
            # Prüfe mit dem Determinantenkriterium ob eine Lösung existiert
            if(zeile1[0]*zeile2[1] - zeile1[1]*zeile2[0] != 0):
                if(zeile1[0]*zeile3[1] - zeile1[1]*zeile3[0] != 0):
                    solution1 = (zeile2[0] * zeile1[1] - zeile1[0]*zeile2[1])/(zeile2[0]*zeile1[2]-zeile1[0]*zeile2[2])
                    solution2 = (zeile3[0] * zeile1[1] - zeile1[0]*zeile3[1])/(zeile3[0]*zeile1[2]-zeile1[0]*zeile3[2])
                if(solution1 == solution2):
                    return solution1
                else:
                    return 100000000000000000000000

    # Schneidet die Gerade am übergebenen Parameter
    def schneideOrthogonal1(self,parameter):
        self.parameter[len(self.parameter)] = parameter

    # Teilt die gerade in zwei neue Teile auf
    def schneideOrthogonal2(self, parameter1,parameter2):
        count1 = -1
        count2 = -1

        for i in range(0,len(self.parameter),1):
            if((parameter1 > self.parameter[i] )+(parameter1 < self.parameter[i+1])):
                count1 = i+1
            if((parameter1 > self.parameter[i] )+(parameter1 < self.parameter[i+1])):
                count2 = i+1

        para = np.empty(len(self.parameter)+2,dtype= float)

        count = 0
        for i in range(len(self.parameter)):
            if(i == count1):
                para[i+count] = parameter1
                count = count + 1
            elif(i == count2):
                para[i+count] = parameter2
                count = count + 1
            else:
                para[i+count] = self.parameter[i]




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


