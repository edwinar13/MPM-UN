class ModelMesh:

    def __init__(self, name, color, points, triangles) -> None:
        self.__name = name
        self.__color = color
        self.__points = points
        self.__triangles = triangles    


    ###############################################################################
	# ::::::::::::::::::::         GETTERS Y SETTERS           ::::::::::::::::::::
	###############################################################################


    def getName(self):
        return self.__name
    
    def getColor(self):
        return self.__color

    def getPoints(self):
        return self.__points

    def getTriangles(self):
        return self.__triangles
    
    def getData(self):
        return[self.__name, self.__color, self.__points, self.__triangles]
       
