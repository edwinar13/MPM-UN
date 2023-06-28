from clases.Modelo.model_ProjectCurrentRepository import ModelProjectCurrentRepository
from clases.items_GraphicsDraw import TextItem, LineItem
from clases.Vista.view_GraphicsDraw import QGraphicsScene


class ModelItemLine:

    def __init__(self, scene_draw:QGraphicsScene,model_project_current_repository:ModelProjectCurrentRepository,
                 id, name,  start_point, end_point) -> None:

        self.scene_draw = scene_draw
        self.model_project_current_repository = model_project_current_repository
        
        self.__id = id
        self.__name = name
        self.__start_point = start_point
        self.__end_point = end_point    


        



        text_name = TextItem(self.__name, 0,0)
        self.scene_draw.addItem(text_name)

        self.line_item = LineItem(id, name,start_point.getPointItem(),end_point.getPointItem() , text_name) 
        
        self.scene_draw.addItem(self.line_item)

        return




        self.dict_lines[name] = l

        point1 = self.dict_points[start_point]
        point2 = self.dict_points[end_point]
        point1.addAnchoredLine(l)
        point2.addAnchoredLine(l)





    ###############################################################################
	# ::::::::::::::::::::         GETTERS Y SETTERS           ::::::::::::::::::::
	###############################################################################
    def getLineItem(self):
        return self.line_item
    
    def getId(self):
        return self.__id

    def getName(self):
        return self.__name

    def getStartPoint(self):
        return self.__start_point

    def getEndPoint(self):
        return self.__end_point
    
    def getData(self):
        """return: id, name, color, points, triangles]"""
        return[self.__id, self.__name, self.__start_point, self.__end_point]
       
    ###############################################################################
    # ::::::::::::::::::::              GENERALES              ::::::::::::::::::::
    ###############################################################################
    def deleteLine(self):
        self.scene_draw.removeItem(self.line_item)
        self.scene_draw.removeItem(self.line_item.text_name)
        self.scene_draw.update()

        
    def updateLine(self,  id_line, name = None, id_start_point = None, id_end_point = None):

        if name != None:
            self.__name = name
        if id_start_point != None:
            self.__start_point = id_start_point
        if id_end_point != None:
            self.__end_point = id_end_point

        self.model_project_current_repository.updateItemLineDrawDB(
            id_line=id_line,
            name=name,
            id_start_point=id_start_point,
            id_end_point=id_end_point
        )     
    
    '''
    def showHideMesh(self, value):
        self.group_mesh.setVisible(value)
    


    def setColorItem(self, color):
        for item in self.group_mesh.childItems():
            if isinstance(item, TriangleMeshItem):
                item.setColor(color)
        self.scene_draw.update()
    
    def deleteMesh(self):

        for item in self.group_mesh.childItems():
            self.group_mesh.removeFromGroup(item)
            self.scene_draw.removeItem(item)
        self.scene_draw.removeItem(self.group_mesh)
        self.scene_draw.update()

    '''