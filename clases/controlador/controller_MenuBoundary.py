from PySide6.QtCore import (Slot,Signal, QObject,QPointF,QLineF)
from clases.Vista.view_WidgetDrawMenuBoundary import ViewWidgetDrawMenuBoundary
from clases.Modelo.model_ProjectCurrent import ModelProjectCurrent
from clases.Controlador.controller_CardBoundary import ControllerCardBoundary

class ControllerMenuBoundary(QObject):

    signal_end_draw_geometry = Signal()

    def __init__(self) -> None:
        super().__init__()
        #Crea la vista menu Boundary
        self.view_menu_boundary = ViewWidgetDrawMenuBoundary()
        self.model_current_project = None
        self.list_controller_card=[]

        self.__initEvent()
        self.showHideBoundaries(False)

    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS CONFIGURAR        ::::::::::::::::::::
	###############################################################################


    def __initEvent(self):
        """ Asigna las ranuras (Slot) a las señales (Signal). """ 
        self.view_menu_boundary.signal_select_point_mesh.connect(self.signalSelectPointMesh)
        self.view_menu_boundary.signal_new_boundary_automatic.connect(self.newBoundaryAutomatic)
        self.view_menu_boundary.signal_new_boundary_manual.connect(self.newBoundaryManual)
        self.view_menu_boundary.signal_show_hide_boundaries.connect(self.showHideBoundaries)        
        self.view_menu_boundary.signal_show_hide_labels.connect(self.showHideLabels)
        

    def setCurrentProject(self,model_current_project:ModelProjectCurrent):
        self.model_current_project = model_current_project        
        self.model_current_project.signal_select_point_back.connect(self.selectPointMesh)

        

    def configDrawMenuBoundary(self):
        
        self.view_menu_boundary.removeCardBoundary()
        self.list_controller_card=[]

        models_boundaries = self.model_current_project.getModelsBoundaries()
        for id_boundary in models_boundaries:
            self.createBoundaryCard(models_boundaries[id_boundary])

        
    def getView(self):
        return self.view_menu_boundary


    def createBoundaryCard(self, model_boundary):
        controller_card_boundary = ControllerCardBoundary( model_boundary = model_boundary)
        self.view_menu_boundary.addCardBoundary(controller_card_boundary.view_card_boundary)
        controller_card_boundary.signal_delete_boundary.connect(self.deleteBoundary)
        self.list_controller_card.append(controller_card_boundary)




    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS  SIGNAL/SLOT        ::::::::::::::::::::
	###############################################################################
    
    # ::::::::::::::::::::         MÉTODOS  VISTA        ::::::::::::::::::::

      
    @Slot(bool)
    def showHideBoundaries(self, show_boundaries):

        for controller in self.list_controller_card:
            controller.showHideBoundary(show_boundaries)
        
        	
    @Slot(bool)
    def showHideLabels(self, show_label):     
        for controller in self.list_controller_card:
            controller.showHideLabel(show_label)

    @Slot()
    def signalSelectPointMesh(self):
        self.signalEndDrawGeometry()
        #self.model_current_project.commandMeshSelectLine({"step":1, "data":None}) 
        self.model_current_project.commandBoundarySelectPoint({"step":1, "data":None}) 

  

    @Slot()
    def newBoundaryAutomatic(self):
        restriction_automatic = self.view_menu_boundary.getTxTyAutomatic()

        restriction_automatic_top = restriction_automatic["Top"]
        restriction_automatic_bottom = restriction_automatic["Bottom"]
        restriction_automatic_left = restriction_automatic["Left"]
        restriction_automatic_right = restriction_automatic["Right"]       

        points_top, points_bottom ,points_left ,points_right = self.model_current_project.getBoundaryPointsMeshBack()    
        nodes_top, nodes_bottom ,nodes_left ,nodes_right = self.model_current_project.getBoundaryNodeMeshBack()   
        

        if  restriction_automatic_top[0] or restriction_automatic_top[1]:        
            id_top= self.model_current_project.createBoundary(
                                                        name ="boundary_top",
                                                        nodes=nodes_top,
                                                        points = points_top,
                                                        restrictionX = restriction_automatic_top[0],
                                                        restrictionY = restriction_automatic_top[1]                                                    
                                                        )
            model_boundary_top = self.model_current_project.getModelsBoundaries()[id_top]
            self.createBoundaryCard(model_boundary_top)
            

        if  restriction_automatic_bottom[0] or restriction_automatic_bottom[1]:
            id_bottom = self.model_current_project.createBoundary(
                                                        name ="boundary_bottom",
                                                        nodes=nodes_bottom,
                                                        points = points_bottom,
                                                        restrictionX = restriction_automatic_bottom[0],
                                                        restrictionY = restriction_automatic_bottom[1]                                                    
                                                        )
            model_boundary_bottom = self.model_current_project.getModelsBoundaries()[id_bottom]
            self.createBoundaryCard(model_boundary_bottom)

        if  restriction_automatic_left[0] or restriction_automatic_left[1]:
            id_left = self.model_current_project.createBoundary(
                                                        name ="boundary_left",
                                                        nodes=nodes_left,
                                                        points = points_left,
                                                        restrictionX = restriction_automatic_left[0],
                                                        restrictionY = restriction_automatic_left[1]                                                    
                                                        )
            model_boundary_left = self.model_current_project.getModelsBoundaries()[id_left]
            self.createBoundaryCard(model_boundary_left)
                        
        if  restriction_automatic_right[0] or  restriction_automatic_right[1]:
            id_right = self.model_current_project.createBoundary(
                                                        name ="boundary_right",
                                                        nodes=nodes_right,
                                                        points = points_right,
                                                        restrictionX = restriction_automatic_right[0],
                                                        restrictionY = restriction_automatic_right[1]                                                    
                                                        )
            

            model_boundary_right = self.model_current_project.getModelsBoundaries()[id_right]
            self.createBoundaryCard(model_boundary_right)

        self.view_menu_boundary.endBoundary1()
        self.endDrawBoudary()


    @Slot()
    def newBoundaryManual(self):



        name_boundary =self.view_menu_boundary.getName()
        selected_objects = self.model_current_project.getSelectedObjects() 
        restriction_Tx = self.view_menu_boundary.getTx()
        restriction_Ty = self.view_menu_boundary.getTy()



         
        if name_boundary == "":
            self.view_menu_boundary.msnAlertName(True, "Revisa el nombre  de la restricción")
            return     
        else:
            self.view_menu_boundary.msnAlertName(False)


        if len(selected_objects) <= 0 :
            self.view_menu_boundary.msnAlertSelected(True, "Selecciona más de un elemento")
            return
        else:
            self.view_menu_boundary.msnAlertSelected(False)

        if not restriction_Tx and not restriction_Ty :
            self.view_menu_boundary.msnAlertRestriction(True, "Selecciona la restricción en X o Y")
            return
        else:
            self.view_menu_boundary.msnAlertRestriction(False)



        points=[]
        for point in selected_objects:
            coor = point.getPoint()
            points.append([point.getPoint().x(),point.getPoint().y()]) 
        nodes = []
        id_boundary = self.model_current_project.createBoundary(
                                                    name =name_boundary,
                                                    nodes=nodes,
                                                    points = points,
                                                    restrictionX = restriction_Tx,
                                                    restrictionY = restriction_Ty                                                    
                                                    )
        
        

        model_boundary = self.model_current_project.getModelsBoundaries()[id_boundary]
        self.createBoundaryCard(model_boundary)

        self.view_menu_boundary.endBoundary2()
        self.endDrawBoudary()
      

    # ::::::::::::::::::::         MÉTODOS  CURRENT        ::::::::::::::::::::
	
    @Slot(int)
    def selectPointMesh(self, no_points):
        self.view_menu_boundary.setNoSelectPointsMesh(no_points)

    

    # ::::::::::::::::::::         MÉTODOS  CARD        ::::::::::::::::::::

    @Slot(str)
    def deleteBoundary(self, id):
        self.model_current_project.deleteBoundary(id)
        


    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS  GENERALES         ::::::::::::::::::::
	###############################################################################



    def endDrawBoudary(self):
        self.model_current_project.endBoundarySelectPoint()
        self.selectPointMesh(0)


    def signalEndDrawGeometry(self):
            self.signal_end_draw_geometry.emit()


