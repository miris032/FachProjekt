import numpy

class multidexelboard():

    def __init__(self, resolution, height, width, depth, x, y, z):
        # In wie viele Teile soll das Werkstück zerlegt werden
        self.resolution = resolution
        # Tiefe des Werkstücks
        self.depth = depth
        # Höhe des Werkstücks
        self.height = height
        # Breite des Werkstücks
        self.width = width
        # Koordinaten des Werkstücks -> Unterste, vorderste und linkeste Ecke
        self.x = x
        self.y = y
        self.z = z
        # Speicher für die Koordinaten auf denen die Normalenvektoren gesetzt werden
        self.coordinates = numpy.empty(0)
        # Normalenvektor der Ebenen und Parameterliste:
        self.normal_X = numpy.empty(0)
        self.parameter_X = numpy.empty(0)
        self.normal_Y = numpy.empty(0)
        self.parameter_Y = numpy.empty(0)
        self.normal_Z = numpy.empty(0)
        self.parameter_Z = numpy.empty(0)
        self.parameter_list = numpy.empty(0)
        # Speicher der Animationskoordinaten
        self.animation = numpy.empty(0)


        # Getter und Setter

    def getResolution(self):
        return self.resolution

    def setResolution(self, value):
        if not isinstance(value, float):
            raise ValueError('Resolution must be float!')
        self.resolution = value

    def getDepth(self):
        return self.depth

    def setDepth(self, value):
        if not isinstance(value, float):
            raise ValueError('Depth must be float!')
        self.depth = value

    def getY(self):
        return self.y

    def setY(self, value):
        if not isinstance(value, float):
            raise ValueError('Y must be float!!')
        self.y = value

    def getHeight(self):
        return self.Height

    def setHeight(self, value):
        if not isinstance(value, float):
            raise ValueError('Height must be float!')
        self.Height = value

    def getWidth(self):
        return self.width

    def setWidth(self, value):
        if not isinstance(value, float):
            raise ValueError('Width must be float!')
        self.width = value

    def getX(self):
        return self.x

    def setX(self, value):
        if not isinstance(value, float):
            raise ValueError('X must be float!')
        self.x = value

    # Methoden des Werstückes

    #Achtung in korrekter Reihenfolge Eingeben x,y,z
    def set_Coordinate(self, value):
        numpy.append(self.coordinates, value)

    def getAnimation(self):
        return self.animation

    # Initialisert das Mutlidexelboard mit der korrekten Schrittweise
    # Auf den Ebenen werden die Normalenvektoren angesetzt

    def initialize_Multidexelboard(self):

        # Koordinaten in der x-y-Ebene
        for i in range(0, self.resolution, 3):
            for j in range(0, self.resolution, 3):
                numpy.append(self.coordinates, i*self.width/self.resolution)
                numpy.append(self.coordinates, j*self.depth/self.resolution)
                numpy.append(self.coordinates, 0)
                numpy.append(self.parameter_list,2)
                numpy.append(self.parameter_list,0)
                numpy.append(self.parameter_list,self.resolution)

        #Normalenvektor und Parameter

        numpy.append(self.normal_Z, 0)
        numpy.append(self.normal_Z, 0)
        numpy.append(self.normal_Z, self.height/self.resolution)
        numpy.append(self.parameter_Z, 0)
        numpy.append(self.parameter_Z, self.resolution)

        # Koordinaten in der y-z-Ebene:
        for i in range(0, self.resolution, 3):
            for j in range(0, self.resolution, 3):
                numpy.append(self.coordinates, 0)
                numpy.append(self.coordinates, i*self.depth/self.resolution)
                numpy.append(self.coordinates, j*self.height/self.resolution)
                numpy.append(self.parameter_list,2)
                numpy.append(self.parameter_list,0)
                numpy.append(self.parameter_list,self.resolution)

                #Normalenvektor und Parameter

        numpy.append(self.normal_X, 0)
        numpy.append(self.normal_X, 0)
        numpy.append(self.normal_X, self.width/self.resolution)
        numpy.append(self.parameter_X, 0)
        numpy.append(self.parameter_X, self.resolution)

        # Koordinate in der x-z-Ebene:
        for i in range(0, self.resolution, 3):
            for j in range(0, self.resolution, 3):
                numpy.append(self.coordinates, i*self.width/self.resolution)
                numpy.append(self.coordinates, 0)
                numpy.append(self.coordinates,  j*self.height/self.resolution)
                numpy.append(self.parameter_list,2)
                numpy.append(self.parameter_list,0)
                numpy.append(self.parameter_list,self.resolution)

        #Normalenvektor und Parameter

        numpy.append(self.normal_Y, 0)
        numpy.append(self.normal_Y, 0)
        numpy.append(self.normal_Y, self.depth/self.resolution)
        numpy.append(self.parameter_Y, 0)
        numpy.append(self.parameter_Y, self.resolution)

    # Erstellt die Koordinaten für die Animation
    def create_animation(self):
        pointer = 0
        for i in range(0,self.coordinates.size,3):
            for j in range(pointer+1, self.parameter_list[pointer]):
                if self.coordinates[i] == 0:
                    numpy.append(self.animation, self.coordinates[i] + j*self.normal_X[0])
                    numpy.append(self.animation, self.coordinates[i+1] + j*self.normal_X[1])
                    numpy.append(self.animation, self.coordinates[i+2] + j*self.normal_X[2])
                elif self.coordinates[i+1] == 0:
                    numpy.append(self.animation, self.coordinates[i] + j*self.normal_Y[0])
                    numpy.append(self.animation, self.coordinates[i+1] + j*self.normal_Y[1])
                    numpy.append(self.animation, self.coordinates[i+2] + j*self.normal_Y[2])
                elif self.coordinates[i+2] == 0:
                    numpy.append(self.animation, self.coordinates[i] + j*self.normal_Z[0])
                    numpy.append(self.animation, self.coordinates[i+1] + j*self.normal_Z[1])
                    numpy.append(self.animation, self.coordinates[i+2] + j*self.normal_Z[2])

            pointer = pointer + self.parameter_list[pointer] + 1


            # Verschieben des Werkstückes
    def set_X_Offset(self,value):
        for i in range(0,self.animation.size,3):
            self.animation[i] = self.animation[i] + value

    def set_Y_Offset(self,value):
        for i in range(1,self.animation.size,3):
            self.animation[i] = self.animation[i] + value

    def set_Z_Offset(self,value):
        for i in range(2,self.animation.size,3):
            self.animation[i] = self.animation[i] + value