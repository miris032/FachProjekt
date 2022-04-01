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
            #print(zeile1)
            #print(zeile2)
            #print(zeile3)
            # Prüfe ob beim LGS zwei vollständige Nullzeilen entstehen
            # Dann sind die Geraden parallel und es existieren unendlich viele Lösungen
            # Dann schneide die Gerade vom Werkstück an der Stelle der Spitze des Geradenstücks
            # vom Werkzeug
            if(zeile2[0] * zeile1[1] - zeile1[0]*zeile2[1] == 0):
                if(zeile3[0] * zeile1[1] - zeile1[0]*zeile3[1] == 0):
                    if(zeile2[0]*zeile1[2] - zeile1[0]*zeile2[2] == 0):
                        if(zeile3[0]*zeile1[2] - zeile1[0]*zeile3[2] == 0):
                            case = -1
                            if(self.richtungsvektor[0] != 0):
                                case = 0
                            elif(self.richtungsvektor[1] != 0):
                                case = 1

                            elif(self.richtungsvektor[2] != 0):
                                case = 2

                            schnitt = np.empty(2,dtype= float)
                            schnitt[0] = gerade.ortsvektor[case] + gerade.parameter[1]*gerade.richtungsvektor[case]

                            schnitt[1] = (schnitt[0]-self.ortsvektor[case]) / self.richtungsvektor[case]

                            if((schnitt[1] > 0)  + (schnitt[1] < 1)):
                                self.parameter[len(self.parameter)-1] = schnitt[1]


    # Prüft ob sich die Geraden schneiden und gibt bei erfolg den Parameter
    # zurück, und eine negative zahl bei nichterfolg
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
            print(zeile1)
            print(zeile2)
            print(zeile3)
            case = np.empty(2,dtype = float)
            case[0] = -1
            # Prüfe ob eine komplette Nullzeile exisitert, nur dann existiert eine Lösung
            if((zeile1 == np.zeros(3)).all()):
                if(zeile2[1] != 0):
                    case[0] = 1
                    case[1] = zeile2[2]/zeile2[1]
                elif(zeile3[1] != 0):
                    case[0] = 1
                    case[1] = zeile3[2]/zeile3[1]
            elif((zeile2 == np.zeros(3)).all()):
                if(zeile1[1] != 0):
                    case[0] = 2
                    case[1] = zeile1[2]/zeile1[1]
                elif(zeile3[1] != 0):
                    case[0] = 2
                    case[1] = zeile3[2]/zeile3[1]
            elif((zeile3 == np.zeros(3)).all()):
                if(zeile1[1] != 0):
                    case[0] = 1
                    case[1] = zeile1[2]/zeile1[1]
                elif(zeile2[1] != 0):
                    case[0] = 1
                    case[1] = zeile2[2]/zeile2[1]


            return case

    # Schneidet die Gerade am übergebenen Parameter
    # Wenn mehr als eine Lösung existiert soll die Gerade von Linie
    # gelöscht werden und zwei neue erstellt werden
    def schneideOrthogonal(self,parameter):
        if(parameter > 0 + parameter < 1):
            self.parameter[len(self.parameter)-1] = parameter



    # Bekommt 3D Array übergeben, mit Verschiebung (x,y,z)
    def verschiebe(self,value):
        self.ortsvektor[0] = self.ortsvektor[0] + value[0]
        self.ortsvektor[1] = self.ortsvektor[1] + value[1]
        self.ortsvektor[2] = self.ortsvektor[2] + value[2]

    # Gibt den Anfangs und Endpunkt der Linie aus
    def getKoordinaten(self):
        ausgabe = np.empty(len(self.parameter)*3,dtype = float)

        for i in range(0,len(ausgabe),3):
            ausgabe[i] = self.ortsvektor[0] + self.parameter[int(i/3)] * self.richtungsvektor[0]
            ausgabe[i+1] = self.ortsvektor[1] + self.parameter[int(i/3)] * self.richtungsvektor[1]
            ausgabe[i+2] = self.ortsvektor[2] + self.parameter[int(i/3)] *  self.richtungsvektor[2]

        return ausgabe


