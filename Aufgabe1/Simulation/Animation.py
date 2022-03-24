import numpy as np
import Werkstück
import Werkzeug

class Animation():

    def __init__(self,quader,zylinder,ablauf,counter):
        self.quader = quader
        self.zylinder = zylinder
        self.ablauf = ablauf
        self.counter = counter

    #Getter und Setter

    def getQuader(self):
        return self.quader

    def getZylinder(self):
        return self.zylinder

    def getAblauf(self):
        return self.ablauf

    def getCounter(self):
        return self.counter

    def setQuader(self,value):
        self.quader = value

    def setZylinder(self,value):
        self.zylinder = value

    def setAblauf(self,value):
        self.ablauf = value

    def setCounter(self,value):
        self.Counter = value

    # Methoden

    # Die Verschiebung aus der Liste Ablauf soll dem Zylinder und dem Quader
    # übergeben werden. Diese führen die Verschiebung aus und danach wird
    # der Schnitt berechnet und die Hüllkurven zurückgegeben

    def schritt(self):
        return 1