import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import Axes3D

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
    def schneideOrthogonal(self,parameter):
        if(parameter>0 + parameter <1):
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
    

class Reihe():

    # richtung = Ausrichtung des Normalenvektors, Zahl: 0 ist x-Richtung, 1 ist y-Richtung, 2 ist z-Richtung
    # row = Koordinaten der Reihe, Array der Länge 3, (x,y,z)
    # normal = Normalenvektor, Array der Länge 3, (x,y,z)
    # reih = Liste von Geraden, wird aktuell in initialize erstellt

    def __init__(self, richtung, row, normal):
        self.richtung = richtung
        self.row = row
        self.normal = normal
        self.schar = []
        print("hier")
        print(type(schar))
        print("hier")
       
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

        for gerade in self.schar:
            ausgabe = np.concatenate(ausgabe,Linie.getKoordinaten(gerade))
            

        return ausgabe

    # Verschiebt alle Gerade der Reihe um value, value ist ein Array der Größe 3, (x,y,z)

    def verschiebe(self, value):
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

    

if __name__ == '__main__':
    
    rvektorX = np.array([1,0,0])
    rvektorY = np.array([0,1,0])
    rvektorY2 = np.array([0,-1,0])
    rvektorZ = np.array([0,0,1])
    ort1 = np.array([0,0,0])
    ort2 = np.array([0,0,0])
    ort3 = np.array([0,0,0])
    ort4 = np.array([0,1.5,0])
    parameter1 = np.array([0,1], dtype = float)
    parameter2 = np.array([0,1],dtype = float)
    parameter3 = np.array([0,1],dtype = float)
    parameter4 = np.array([0,1], dtype = float)
    gerade1 = Linie(ort1, rvektorX, parameter1, 0)
    gerade2 = Linie(ort2,rvektorY,parameter2,1)
    gerade3 = Linie(ort3, rvektorZ,parameter3,2)
    gerade4 = Linie(ort4, rvektorY2,parameter4,1)
    
    #Hier der Code für die Testcases Linie
    
    Linie.schneideParallel(gerade2,gerade4)
    print(Linie.hatSchnittpunkt(gerade1,gerade3))
    
    versuch = Linie.getKoordinaten(gerade1)
    versuch = np.append(versuch,Linie.getKoordinaten(gerade2))
    versuch = np.append(versuch,Linie.getKoordinaten(gerade3))
    versuch = np.append(versuch,Linie.getKoordinaten(gerade4))
    
    x = np.empty(int(len(versuch)/3), dtype =float)
    y = np.empty(int(len(versuch)/3), dtype =float)
    z = np.empty(int(len(versuch)/3), dtype =float)
    
    #Hier der Code für die Testcases Reihe
    r = np.array([0,0,0,0.5,0,0,1,0,0,1.5,0,0,2,0,0],dtype =float)
    schar = Reihe(2,r,rvektorZ)
    versuch2 = Reihe.getKoordinaten(schar)

    
    for i in range(0,len(versuch),3):
        x[int(i/3)] = versuch[i]
        y[int(i/3)] = versuch[i+1]
        z[int(i/3)] = versuch[i+2]
        
    soa = np.reshape(versuch,(4,6))
    #print(versuch)
    #print(x)
    #print(y)
    #print(z)
    print(soa)
    
    X, Y, Z, U, V, W= zip(*soa)
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.quiver(X, Y, Z, U, V, W)
    ax.set_xlim([-2, 2])
    ax.set_ylim([-2, 2])
    ax.set_zlim([-2, 2])
    #ax = plt.axes(projection="3d")
    #ax.plot3D(x, y, z, 'red')
    #ax.scatter3D(x, y, z, c=z, cmap='cividis');
    plt.show()

