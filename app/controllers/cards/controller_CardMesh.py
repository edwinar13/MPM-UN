
from PySide6.QtCore import (Slot, Signal, QObject)
from views.cards.view_WidgetCardMesh import viewCardDrawMesh
from models.model_Mesh import ModelMeshTriangle, ModelMeshQuadrilateral
from models.model_ProjectCurrent import ModelProjectCurrent

class ControllerCardMesh(QObject):

    signal_msn = Signal(str)
    signal_delete_mesh = Signal(list)
    signal_edit_mesh= Signal() 

    def __init__(self, model_mesh:ModelMeshTriangle|ModelMeshQuadrilateral, model_current_project:ModelProjectCurrent) -> None:
        super().__init__()

        self.model_mesh = model_mesh
        self.model_current_project = model_current_project
        self.id, self.name, self.color, self.points, self.elements = model_mesh.getData()
        if  isinstance(model_mesh, ModelMeshTriangle):
            self.type = "TRIANGLE"
            
        elif  isinstance(model_mesh, ModelMeshQuadrilateral):
            self.type = "QUADRILATERAL"
   
        self.__initCard()
        self.__initEvent()

    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS CONFIGURAR        ::::::::::::::::::::
	###############################################################################
    def __initCard(self):
        self.view_card_mesh = viewCardDrawMesh(self)
        self.view_card_mesh.showData(name = self.name, color = self.color)
    
    def __initEvent(self):
        """ Asigna las ranuras (Slot) a las señales (Signal). """ 
        self.view_card_mesh.signal_hide_show_mesh.connect(self.showHideMesh)
        self.view_card_mesh.signal_delete_mesh.connect(self.deleteMesh)
        self.view_card_mesh.signal_update_mesh.connect(self.updateMesh)

    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS  SIGNAL/SLOT        ::::::::::::::::::::
	###############################################################################
    @Slot(bool)
    def showHideMesh(self, value):
        self.model_mesh.showHideMesh(value)
        self.view_card_mesh.ShowHideMesh(value)



    @Slot(bool)
    def showHideLabel(self, value):
        self.model_mesh.showHideLabel(value)

    @Slot()
    def deleteMesh(self):        
        #verificar que no este asigando a un MP
        models_materials_points = self.model_current_project.getModelsPointsMaterials()
        for id_model_material_point in models_materials_points:
            model_material_point = models_materials_points[id_model_material_point]
            
            name_MP =model_material_point.getName()
            id_mesh_to_MP = model_material_point.getMeshBase().getId()

            if id_mesh_to_MP == self.id:                
                self.signal_msn.emit("Malla esta asignada a un MP [{}]".format(name_MP))
                return
        
        self.view_card_mesh.deleteCardView()
        self.signal_delete_mesh.emit([self.type, self.id])
        del self


    @Slot()
    def updateMesh(self):        
        self.name = self.view_card_mesh.getName()
        self.color = self.view_card_mesh.getColor()
        self.model_mesh.updateMesh(
            id_mesh = self.id,
            name=self.name,
            color=self.color
            )
        self.signal_edit_mesh.emit()





