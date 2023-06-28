
from PySide6.QtCore import (Slot, Signal, QObject)
from clases.Vista.view_WidgetCardMesh import viewCardDrawMesh
from clases.Modelo.model_Mesh import ModelMeshTriangle

class ControllerCardMesh(QObject):

  
    signal_delete_mesh = Signal(str)

    def __init__(self, model_mesh:ModelMeshTriangle) -> None:
        super().__init__()

        self.model_mesh = model_mesh
        self.id, self.name, self.color, self.points, self.triangles = model_mesh.getData()

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

    @Slot(bool)
    def showHideMesh(self, value):
        self.model_mesh.showHideMesh(value)


    @Slot()
    def deleteMesh(self):
        self.signal_delete_mesh.emit(self.id)
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





