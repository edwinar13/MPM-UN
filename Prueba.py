from PySide6.QtCore import*
from PySide6.QtGui import*
from PySide6.QtWidgets import*
import numpy as np
import sys


class  MainWindow(QMainWindow):
    def __init__(self ) -> None:
        super().__init__()

        self.undoStack = QUndoStack(self)
        self.createActions()
        self.createMenus()
        self.createUndoView()
        self.diagramScene = DiagramScene()
        pixmapBrush = QBrush(QPixmap(":/images/cross.png").scaled(30, 30))
        self.diagramScene.setBackgroundBrush(pixmapBrush)
        self.diagramScene.setSceneRect(QRect(0, 0, 500, 500))
        self.diagramScene.itemMoved.connect(
                self.itemMoved)
        self.setWindowTitle("Undo Framework")
        view = QGraphicsView(self.diagramScene)
        self.setCentralWidget(view)
        self.resize(700, 500)

    def createActions(self):
        editMenu = menuBar().addMenu(tr("Edit"))
        editMenu.addAction(self.undoAction)
        editMenu.addAction(self.redoAction)
        editMenu.addSeparator()
        editMenu.addAction(self.deleteAction)
        editMenu.aboutToShow.connect(
        self.itemMenuAboutToShow)
        editMenu.aboutToHide.connect(
        self.itemMenuAboutToHide) 
    def createMenus(self):
        pass
   

    def createUndoView(self):
        undoView = QUndoView(self.undoStack)
        undoView.setWindowTitle(tr("Command List"))
        undoView.show()
        undoView.setAttribute(Qt.WA_QuitOnClose, False)

    def createActions(self):
        self.deleteAction = QAction(tr("Delete Item"), self)
        self.deleteAction.setShortcut(tr("Del"))
        self.deleteAction.triggered.connect(self.deleteItem)
        self.undoAction = self.undoStack.createUndoAction(self, tr("Undo"))
        self.undoAction.setShortcuts(QKeySequence.Undo)
        self.redoAction = self.undoStack.createRedoAction(self, tr("Redo"))
        self.redoAction.setShortcuts(QKeySequence.Redo)

    def itemMoved(self, movedItem,):
        oldPosition = QPointF()
        self.undoStack.push(MoveCommand(movedItem, oldPosition))

    def deleteItem(self):
        if self.diagramScene.selectedItems().isEmpty():
            return
        deleteCommand = DeleteCommand(self.diagramScene)
        self.undoStack.push(deleteCommand)

    def itemMenuAboutToHide(self):
        self.deleteAction.setEnabled(True)

    def itemMenuAboutToShow(self):
        self.deleteAction.setEnabled(not self.diagramScene.selectedItems().isEmpty())



    def addBox(self):
        addCommand = AddCommand(self.DiagramItem::Box, diagramScene)
        self.undoStack.push(addCommand)
    def addTriangle(self):

        addCommand = AddCommand(self.DiagramItem::Triangle,()
                                                diagramScene)
        self.undoStack.push(addCommand)





'''

# public
    MainWindow()
# public slots
    def itemMoved(movedDiagram, moveStartPosition):
# private slots
    def deleteItem():
    def addBox():
    def addTriangle():
    def about():
    def itemMenuAboutToShow():
    def itemMenuAboutToHide():
# private
    def createActions():
    def createMenus():
    def createUndoView():

deleteAction = None()
addBoxAction = None()
addTriangleAction = None()
undoAction = None()
redoAction = None()
exitAction = None()
aboutAction = None()
fileMenu = None()
editMenu = None()
itemMenu = None()
helpMenu = None()
diagramScene = None()
undoStack = None()
undoView = None()
'''

class DiagramScene (QGraphicsScene):
    def __init__ (self ) -> None:
        super().__init__()

'''
    Q_OBJECT
# public
    DiagramScene(QObject parent = None)
# signals
    def itemMoved(movedItem, movedFromPosition):
# protected
    def mousePressEvent(event):
    def mouseReleaseEvent(event):
# private
    movingItem = None()
    oldPos = QPointF()
'''



class AddCommand(QUndoCommand):

    def __init__ (self, addType, scene ):
        AddCommand.__init__(self)
        self.myGraphicsScene = scene

        itemCount = 0
        self.myDiagramItem = DiagramItem(addType)
        self.initialPosition = QPointF((itemCount * 15) % int(scene.width()),
                                (itemCount * 15) % int(scene.height()))
        scene.update()
        itemCount = itemCount + 1
        self.setText(QObject.tr("Add %1")
            .arg(createCommandString(self.myDiagramItem, initialPosition)))

    def undo(self):
        self.myGraphicsScene.removeItem(self.myDiagramItem)
        self.myGraphicsScene.update()

    def redo(self):

        self.myGraphicsScene.addItem(self.myDiagramItem)
        self.myDiagramItem.setPos(self.initialPosition)
        self.myGraphicsScene.clearSelection()
        self.myGraphicsScene.update()


'''
# public
    AddCommand(DiagramItem.DiagramType addType, QGraphicsScene graphicsScene,
               parent = None)
    ~AddCommand()
    def undo():
    def redo():
# private
    myDiagramItem = DiagramItem()
    myGraphicsScene = QGraphicsScene()
    initialPosition = QPointF()
'''



class DeleteCommand(QUndoCommand):

    def __init__(self, scene, parent):
        super().__init__(parent)
        self.myGraphicsScene = scene
        list = self.myGraphicsScene.selectedItems()
        list.first().setSelected(False)
        self.myDiagramItem = DiagramItem(list.first())
        self.setText(QObject.tr("Delete %1")
            .arg(createCommandString(self.myDiagramItem, self.myDiagramItem.pos())))

    def undo(self):
        self.myGraphicsScene.addItem(self.myDiagramItem)
        self.myGraphicsScene.update()  
    def redo(self):
        self.myGraphicsScene.removeItem(self.myDiagramItem)  

    '''

# public
    DeleteCommand = explicit(QGraphicsScene graphicsScene, QUndoCommand parent = None)
    def undo():
    def redo():
# private
    myDiagramItem = DiagramItem()
    myGraphicsScene = QGraphicsScene()
'''

class MoveCommand(QUndoCommand):
    def __init__(self, diagramItem, oldPos, parent):
        super().__init__(parent)
        self.myDiagramItem = diagramItem
        self.myOldPos=(oldPos)
        self.newPos=(diagramItem.pos())

    def undo(self):

        self.myDiagramItem.setPos(self.myOldPos)
        self.myDiagramItem.scene().update()
        self.setText(QObject.tr("Move %1")
            .arg(createCommandString(self.myDiagramItem, self.newPos)))
    def redo(self):

        self.myDiagramItem.setPos(self.newPos)
        self.setText(QObject.tr("Move %1")
            .arg(createCommandString(self.myDiagramItem, self.newPos)))

    def mergeWith(self, command):

        moveCommand = MoveCommand(command)
        item = moveCommand.myDiagramItem
        if self.myDiagramItem != item:
            return False
        newPos = item.pos()
        self.setText(QObject.tr("Move %1")
            .arg(createCommandString(self.myDiagramItem, newPos)))
        return True





if __name__ == "__main__":

    Q_INIT_RESOURCE(undoframework)
    app = QApplication(argv, args)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())

'''
# public
    enum { Id = 1234 }
    MoveCommand(DiagramItem diagramItem, QPointF oldPos,
                parent = None)
    def undo():
    def redo():
    mergeWith = bool(QUndoCommand command)
    int id() override { return Id; }
# private
    myDiagramItem = DiagramItem()
    myOldPos = QPointF()
    newPos = QPointF()
'''


def main():
    
    app = QApplication([]) if QApplication.instance() is None else QApplication.instance()
    app.setStyle(QStyleFactory.create('Fusion'))
    d =  DrawWidget(QImage("first.png"), 10)
    d.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()