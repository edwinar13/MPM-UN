from clases.Modelo.model_ProjectCurrentRepository import ModelProjectCurrentRepository
from clases.Modelo.model_Mesh import ModelMeshBack
from clases.Vista.view_GraphicsResult import ViewGraphicsSceneResult, ViewGraphicsViewResult
from clases.items_GraphicsResult import (ItemResultAxisMeshBack, ItemResultGridMeshBack, ItemResultLabelGridMeshBack,
                                    ItemResultBaseMeshBack, ItemResultNode, ItemResultColorBar, TextResultItem, ItemResultTextLabel)
import random
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class ModelResult(QObject):
    
    signal_time_steps_changed = Signal(int)
    signal_time_steps_end = Signal()

    def __init__(self,scene_result:ViewGraphicsSceneResult, 
                view_result:ViewGraphicsViewResult,
                model_project_current_repository:ModelProjectCurrentRepository,
                model_mesh_back:ModelMeshBack,
                analysis_times,
                graphic_time, 
                result_min,
                result_max,
                result_nodes) -> None:
        super().__init__() 
        self.scene_result = scene_result
        self.view_result = view_result
        self.model_mesh_back = model_mesh_back
        self.model_project_current_repository = model_project_current_repository

        self.__analysis_times = analysis_times
        self.__graphic_time = graphic_time
        self.__result_nodes= result_nodes
        self.__item_result_nodes=[]
        self.__result_min = result_min
        self.__result_max = result_max
        
        self.base_mesh_back_result = None
        self.axis_mesh_back_result = None
        self.label_mesh_back_result = None
        self.grid_mesh_back_result = None
              

        
        
        #crear item escena
        if len(self.__analysis_times) > 0:
            self.clearSceneResult()
            self.drawItemBasicScene()
            self.drawItemPointsScene()
            self.view_result.resetView()
        
        self.timer = QTimer()
        self.timer.timeout.connect(self.advanceTime)
        self.setVelocity(50)
        self.time_view = 0
        self.no_data = len(self.__graphic_time)
            


              
    ###############################################################################
	# ::::::::::::::::::::         GETTERS Y SETTERS           ::::::::::::::::::::
	###############################################################################

    def getAnalysisTimes(self):
        return self.__analysis_times
    
    def getGrapihcsTimes(self):
        return self.__graphic_time

    
    def getResultNodes(self):
        return self.__result_nodes
    '''
    def getResultNodeById(self, id_node):
        print(self.__result_nodes.keys())
        for result_node in self.__result_nodes:
            print("->",result_node)
        result_node = self.__result_nodes[str(id_node)]    
        return result_node
    '''
    
    def getData(self) -> list:
        """return: 
        analysis_times, 
        graphics_times, 
        result_nodes]"""
        return[self.__analysis_times,self.__graphic_time,
                self.__result_nodes]




    ###############################################################################
    # ::::::::::::::::::::              GENERALES              ::::::::::::::::::::
    ###############################################################################
    
    def changedColorStyle(self, color_style, hue=0):
        for node in self.__item_result_nodes:
            node.setColorStyle(color_style, hue)            
        
        self.color_bar_result.setVisible(True)
        if color_style == "default":
            self.color_bar_result.setVisible(False)
        
        elif color_style == "Rojo-Azul":
            self.color_bar_result.setColorType(1)
        elif color_style == "Escala de grises":
            self.color_bar_result.setColorType(2)
        elif color_style == "Escala color":
            color = QColor.fromHsv(hue, 255, 255)
            self.color_bar_result.setColorType(3, color)
            
    
    
    def hideShowItemBasic(self,item, is_visible=True):
        """ 
        Args:
            item (_type_): opciones => base, axis, label, grid            
        """
        
        if item == "base":
            self.base_mesh_back_result.setVisible(not self.base_mesh_back_result.isVisible())
        elif item == "axis":
            self.axis_mesh_back_result.setVisible(not self.axis_mesh_back_result.isVisible())
        elif item == "label":
            self.label_mesh_back_result.setVisible(not self.label_mesh_back_result.isVisible())
        elif item == "grid":
            self.grid_mesh_back_result.setVisible(not self.grid_mesh_back_result.isVisible())
        elif item == "values":
            for node in self.__item_result_nodes:                               
                node.setVisibleValue(is_visible)



    
    def setSizePoints(self, size_points):
        for node in self.__item_result_nodes:
            node.setSizePoints(size_points)
        self.scene_result.update()
    
    def setSizeTexts(self, size_texts):
        for node in self.__item_result_nodes:
            node.setSizeTexts(size_texts)
        self.scene_result.update()
        
    def setTypeResult(self, type_result):
        for node in self.__item_result_nodes:   
            node.setTypeResult(type_result)   

        self.scene_result.update() 
        if type_result != "default": 
            min = self.__result_min[type_result.upper()]
            max = self.__result_max[type_result.upper()]
        else:
            min = 0
            max = 0
        self.color_bar_result.setTypeResult(type_result, max, min)
        
        
    def setVelocity(self, velocity):
        self.timer.setInterval(1000 / velocity) # intervalo en milisegundos

               
    def regressTime(self):        
        self.time_view -= 1        
        if self.time_view >= self.no_data:
            self.time_view = self.no_data - 1
            
        elif self.time_view < 0:
            self.time_view = 0
        for node in self.__item_result_nodes:
            node.regressTime(self.time_view)                 
        self.signal_time_steps_changed.emit(self.time_view)       
            
            
    def stopTime(self):
        self.timer.stop() 
        self.time_view = 0 
        for node in self.__item_result_nodes:
            node.stopTime()        
        self.signal_time_steps_changed.emit(self.time_view)
        
    def playPauseTime(self, scene_is_play):        
        if not scene_is_play:
            self.timer.stop()
        else:      
            self.timer.start() # intervalo en milisegundos
            
            
    def advanceTime(self):        
        self.time_view += 1
        if self.time_view >= self.no_data:
            self.playPauseTime(False)
            self.time_view = self.no_data - 1
            self.signal_time_steps_end.emit()
            
            
        elif self.time_view < 0:
            self.time_view = 0            
        for node in self.__item_result_nodes:
            node.advanceTime(self.time_view)
        self.signal_time_steps_changed.emit(self.time_view)
    
       
    
    def  drawItemPointsScene(self):       
        
        for node in self.__result_nodes:
            color_type = random.choices([1,2], weights=[70, 30], k=1)[0]
            radius = 0.05
            text = TextResultItem("temp", 0,0)
            self.scene_result.addItem(text)   
            text.setScale(0.01)         


            node_result = ItemResultNode(
                radius,
                color_type, 
                self.__graphic_time,
                self.__result_nodes[node], 
                self.__result_min,
                self.__result_max,
                text)
            
            self.__item_result_nodes.append(node_result)
            self.scene_result.addItem(node_result)
            node_result.setZValue(11)
            
           
    @Slot()    
    def timeStepsChanged(self, time_step):
        self.signal_time_steps_changed.emit(time_step)
        
        

            

        
 
        

    def drawItemBasicScene(self):
        w = self.model_mesh_back.getSizeDx()
        h = self.model_mesh_back.getSizeDy()
        x = 0
        y = 0

        self.axis_mesh_back_result = ItemResultAxisMeshBack(x,y,w, h)
        self.scene_result.addItem(self.axis_mesh_back_result)
        self.axis_mesh_back_result.setZValue(10)

        self.label_mesh_back_result = ItemResultLabelGridMeshBack(self.scene_result,x,y,w, h)
        self.scene_result.addItem(self.label_mesh_back_result)
        self.label_mesh_back_result.setZValue(9)

        self.grid_mesh_back_result = ItemResultGridMeshBack(x,y,w, h)
        self.scene_result.addItem(self.grid_mesh_back_result)
        self.grid_mesh_back_result.setZValue(8)
        
        self.base_mesh_back_result = ItemResultBaseMeshBack(x,y,w, h)
        self.scene_result.addItem(self.base_mesh_back_result)
        self.base_mesh_back_result.setZValue(100)
        self.base_mesh_back_result.setVisible(False)
        
        self.color_bar_result = ItemResultColorBar(x,y)
        self.scene_result.addItem(self.color_bar_result)
        self.color_bar_result.setZValue(100)
        self.color_bar_result.setScale(0.01)
        self.color_bar_result.setPos(x+w+(w/5),y)
        self.color_bar_result.setVisible(False)
        
        '''
        rect = self.scene_result.sceneRect()
        item = QGraphicsRectItem(rect)
        item.setPen(QPen(QColor("#aaa"), 0, Qt.DashLine))
        self.scene_result.addItem(item)
        '''


    def clearSceneResult(self):
        self.scene_result.clear()
        self.__item_result_nodes = []
        
        
    def updateResult(self ): 
        self.clearSceneResult()
        self.drawItemBasicScene()
        self.drawItemPointsScene()
        #self.view_result.resetView()
        
    def clearResult(self):
        self.model_project_current_repository.deleteAllResultDB()
        
    def updateResultTimes(self,analysis_times=None ):

        if analysis_times != None:
            self.__analysis_times = analysis_times


        self.model_project_current_repository.updateResultTimesDB(
            analysis_times=analysis_times,
            )
        
    def updateResultTimeGraphic(self, graphic_time):
        self.model_project_current_repository.updateResultTimeGraphicDB(
            graphic_time=graphic_time,
            )
    def updateResultMin(self, corx, cory, sigxx, sigyy, sigxy, epsxx, epsyy, epsxy):
        self.model_project_current_repository.updateResultMinDB(
            corx=corx,
            cory=cory,
            sigxx=sigxx,
            sigyy=sigyy,
            sigxy=sigxy,
            epsxx=epsxx,
            epsyy=epsyy,
            epsxy=epsxy
            )
    def updateResultMax(self, corx, cory, sigxx, sigyy, sigxy, epsxx, epsyy, epsxy):
        self.model_project_current_repository.updateResultMaxDB(
            corx=corx,
            cory=cory,
            sigxx=sigxx,
            sigyy=sigyy,
            sigxy=sigxy,
            epsxx=epsxx,
            epsyy=epsyy,
            epsxy=epsxy
            )
    

        

                
    def addResultNode(self, id_result_node, corx=None, cory=None,
             sigxx=None, sigyy=None, sigxy=None,
             epsxx=None, epsyy=None, epsxy=None ):        


        self.model_project_current_repository.createResultNodeDB(
            id_result_node=str(id_result_node), 
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

   
        


                