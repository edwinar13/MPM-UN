from clases.Modelo.model_ProjectCurrentRepository import ModelProjectCurrentRepository
from clases.Modelo.model_Mesh import ModelMeshBack
from clases.Vista.view_GraphicsResult import ViewGraphicsSceneResult, ViewGraphicsViewResult
from clases.items_GraphicsResult import (ItemResultAxisMeshBack, ItemResultGridMeshBack, ItemResultLabelGridMeshBack,
                                    ItemResultBaseMeshBack, ItemResultNode)
import random
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class ModelResult(QObject):
    
    signal_time_steps_changed = Signal(int)

    def __init__(self,scene_result:ViewGraphicsSceneResult, 
                view_result:ViewGraphicsViewResult,
                model_project_current_repository:ModelProjectCurrentRepository,
                model_mesh_back:ModelMeshBack,
                analysis_times, 
                result_nodes) -> None:

        self.scene_result = scene_result
        self.view_result = view_result
        self.model_mesh_back = model_mesh_back
        self.model_project_current_repository = model_project_current_repository

        self.__analysis_times = analysis_times
        self.__result_nodes= result_nodes
        self.__item_result_nodes=[]
        
        #crear item escena
        if len(self.__analysis_times) > 0:
            self.drawItemBasicScene()
            self.drawItemPointsScene()
            self.view_result.resetView()
            


              
    ###############################################################################
	# ::::::::::::::::::::         GETTERS Y SETTERS           ::::::::::::::::::::
	###############################################################################

    def getAnalysisTimes(self):
        return self.__analysis_times

    
    def getResultNodes(self):
        return self.__result_nodes
    
    def getResultNodeById(self, id_node):
        print(self.__result_nodes.keys())
        for result_node in self.__result_nodes:
            print("->",result_node)
        result_node = self.__result_nodes[str(id_node)]

    
        return result_node
    
    def getData(self):
        """return: 
        analysis_times, 
        graphics_times, 
        result_nodes]"""
        return[self.__analysis_times,
                self.__result_nodes]




    ###############################################################################
    # ::::::::::::::::::::              GENERALES              ::::::::::::::::::::
    ###############################################################################
    
    def  drawItemPointsScene(self):

        size_dx_mesh_back = self.model_mesh_back.getSizeDx()
        size_dy_mesh_back = self.model_mesh_back.getSizeDy()

        for node in self.__result_nodes:
            color_type = random.choices([1,2], weights=[70, 30], k=1)[0]
            radius = (min(size_dx_mesh_back,size_dy_mesh_back))/50
            node_result = ItemResultNode(radius,color_type, self.__result_nodes[node])
            self.__item_result_nodes.append(node_result)
            self.scene_result.addItem(node_result)
            node_result.setZValue(11)
            
        for node in self.__item_result_nodes:
            print("node",node)            
            #
            # 
            # 
            # 
            # 
            # 
            # 
            # node.signal_time_steps_changed.connect(self.timeStepsChanged)
            
            
    
    @Slot()    
    def timeStepsChanged(self, time_step):
        self.signal_time_steps_changed.emit(time_step)
        
        
        
    def advanceTime(self):
        print("►► advanceTime")
        for node in self.__item_result_nodes:
            node.advanceTime()
            
    def stopTime(self):
        print("# stopPauseTime")
        for node in self.__item_result_nodes:
            node.stopTime()
        
    def playPauseTime(self, scene_is_play):
        print(" || ►playPauseTime")
        for node in self.__item_result_nodes:
            node.playPauseTime(scene_is_play)
            
    def regressTime(self):
        print("◄◄ regressTime")
        for node in self.__item_result_nodes:
            node.regressTime()
            
            

    def drawItemBasicScene(self):
        
        w = self.model_mesh_back.getSizeDx()
        h = self.model_mesh_back.getSizeDy()
        x = 0
        y = 0
        
        base_mesh_back_result = ItemResultBaseMeshBack(x,y,w, h)
        self.scene_result.addItem(base_mesh_back_result)
        base_mesh_back_result.setZValue(1)
        base_mesh_back_result.setVisible(True)

        axis_mesh_back_result = ItemResultAxisMeshBack(x,y,w, h)
        self.scene_result.addItem(axis_mesh_back_result)
        axis_mesh_back_result.setZValue(10)

        label_mesh_back_result = ItemResultLabelGridMeshBack(self.scene_result,x,y,w, h)
        self.scene_result.addItem(label_mesh_back_result)
        label_mesh_back_result.setZValue(9)

        grid_mesh_back_result = ItemResultGridMeshBack(x,y,w, h)
        self.scene_result.addItem(grid_mesh_back_result)
        grid_mesh_back_result.setZValue(8)
        
        rect = self.scene_result.sceneRect()
        item = QGraphicsRectItem(rect)
        item.setPen(QPen(QColor("#aaa"), 0, Qt.DashLine))
        self.scene_result.addItem(item)


    
    def updateResult(self ):        
        self.drawItemBasicScene()
        self.drawItemPointsScene()
        #self.view_result.resetView()
        
    def updateResultTimes(self,analysis_times=None ):

        if analysis_times != None:
            self.__analysis_times = analysis_times


        self.model_project_current_repository.updateResultTimesDB(
            analysis_times=analysis_times,
            )

                
    def addResultNode(self, id_result_node, times = None, corx=None, cory=None,
             sigxx=None, sigyy=None, sigxy=None,
             epsxx=None, epsyy=None, epsxy=None ):        


        self.model_project_current_repository.createResultNodeDB(
            id_result_node=str(id_result_node), 
            times=times,
            corx=corx, 
            cory=cory,
            sigxx=sigxx, 
            sigyy=sigyy, 
            sigxy=sigxy,
            epsxx=epsxx, 
            epsyy=epsyy,
            epsxy=epsxy
        )

        self.__result_nodes = self.model_project_current_repository.readResultNodesDB()

   
        


                