
from PySide6.QtCore import (Slot, Signal, QObject)
from clases.Vista.view_WidgetCardMesh import viewCardDrawMesh
 
class ControllerCardMesh(QObject):

    signal_hide_show_mesh = Signal(list)
    signal_delete_mesh = Signal(str)
    signal_update_mesh = Signal(dict)

    def __init__(self, mesh) -> None:
        super().__init__()

        print(mesh)
        self.name, self.color, self.points, self.triangles = mesh.getData()
        self.view_card_mesh = viewCardDrawMesh(
                                self,
                                points=self.points,
                                triangles=self.triangles,
                                cardNameMesh=self.name,
                                cardColorMesh=self.color,
                                )

        self.view_card_mesh.signal_hide_show_mesh.connect(self.showHideMesh)
        self.view_card_mesh.signal_delete_mesh.connect(self.deleteMesh)
        self.view_card_mesh.signal_update_mesh.connect(self.updateMesh)

    @Slot(bool)
    def showHideMesh(self, value):
        self.signal_hide_show_mesh.emit([self.name, value])


    @Slot()
    def deleteMesh(self):
        self.signal_delete_mesh.emit(self.name)


    @Slot(dict)
    def updateMesh(self, data):
        self.signal_update_mesh.emit(data)






