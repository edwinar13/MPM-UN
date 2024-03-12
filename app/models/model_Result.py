from models.model_ProjectCurrentRepository import ModelProjectCurrentRepository
from models.model_Mesh import ModelMeshBack
from views.view_GraphicsResult import ViewGraphicsSceneResult, ViewGraphicsViewResult
from utils.items_GraphicsResult import (ItemResultAxisMeshBack, ItemResultGridMeshBack, ItemResultLabelGridMeshBack,
                                    ItemResultBaseMeshBack, ItemResultNode, ItemResultColorBar, TextResultItem, ItemResultTextLabel)
import random
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class ModelResult(QObject):
    
    signal_time_steps_changed = Signal(int)
    signal_time_steps_end = Signal()
    signal_reset_result = Signal()

    def __init__(self,scene_result:ViewGraphicsSceneResult, 
                view_result:ViewGraphicsViewResult,
                model_project_current_repository:ModelProjectCurrentRepository,                
                data_base,
                properties,
                point_materials,
                mesh_back,
                boundarys,
                data_times,         
                analysis_times,
                graphic_time, 
                result_min,
                result_max,
                result_nodes) -> None:
        super().__init__() 
        

        self.scene_result = scene_result
        self.view_result = view_result
        self.model_project_current_repository = model_project_current_repository


        if mesh_back != None:
            self.model_mesh_back = ModelMeshBack(
                scene_draw=scene_result,
                model_project_current_repository=model_project_current_repository,
                size_dx=mesh_back['SIZEDX'],
                size_dy=mesh_back['SIZEDY'],
                size_element=mesh_back['SIZEELEMENT'],
                color_style=mesh_back['COLOR'],
                points=mesh_back['POINTS'],
                quadrilaterals=mesh_back['QUADRILATERALS'],
                points_boundary_top=mesh_back['POINTSBOUNDARYTOP'],
                points_boundary_bottom=mesh_back['POINTSBOUNDARYBOTTOM'],
                points_boundary_left=mesh_back['POINTSBOUNDARYLEFT'],
                points_boundary_right=mesh_back['POINTSBOUNDARYRIGHT'],
                nodes_boundary_top=mesh_back['NODESBOUNDARYTOP'],
                nodes_boundary_bottom=mesh_back['NODESBOUNDARYBOTTOM'],
                nodes_boundary_left=mesh_back['NODESBOUNDARYLEFT'],
                nodes_boundary_right=mesh_back['NODESBOUNDARYRIGHT']
                
            )      
        

        self.__data_base = data_base
        self.__properties = properties
        self.__point_materials = point_materials
        self.__boundarys = boundarys
        self.__data_times = data_times      
        
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
    def getDataBase(self):
        return self.__data_base
    
    def getProperties(self):
        return self.__properties
    
    def getPointMaterials(self):
        return self.__point_materials
    
    def getMeshBack(self):
        return self.model_mesh_back.getData()
    
    def getBoundarys(self):
        return self.__boundarys
    
    def getDataTimes(self):        
        return self.__data_times   


    def getAnalysisTimes(self):
        return self.__analysis_times
    
    def getGrapihcsTimes(self):
        return self.__graphic_time

    
    def getResultNodes(self):
        return self.__result_nodes

    
    def getData(self) -> list:
        """return: 
        {    
            "DATA_BASE": self.__data_base,
            "PROPERTIES": self.__properties,
            "POINT_MATERIALS": self.__point_materials,
            "MESH_BACK": self.model_mesh_back.getData(),
            "BOUNDARYS": self.__boundarys,
            "DATA_TIMES": self.__data_times,
            "ANALYSIS_TIMES": self.__analysis_times,
            "GRAPHIC_TIME": self.__graphic_time,
            "RESULT_MIN": self.__result_min,
            "RESULT_MAX": self.__result_max,
            "RESULT_NODES": self.__result_nodes     
        }
        """
        #return[self.__data_base, self.__properties, self.__point_materials, self.model_mesh_back.getData(), self.__boundarys, self.__data_times, self.__analysis_times, self.__graphic_time, self.__result_min, self.__result_max, self.__result_nodes]
        return {
            "DATA_BASE": self.__data_base,
            "PROPERTIES": self.__properties,
            "POINT_MATERIALS": self.__point_materials,
            "MESH_BACK": self.model_mesh_back.getData(),
            "BOUNDARYS": self.__boundarys,
            "DATA_TIMES": self.__data_times,
            "ANALYSIS_TIMES": self.__analysis_times,
            "GRAPHIC_TIME": self.__graphic_time,
            "RESULT_MIN": self.__result_min,
            "RESULT_MAX": self.__result_max,
            "RESULT_NODES": self.__result_nodes            
        }      




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
        
        #self.scene_result.drawBoundingRects()
        
    
       
    
    def  drawItemPointsScene(self):     
        
        size_mesh_back = self.model_mesh_back.getSizeDx()  
        
        for node in self.__result_nodes:
            color_type = random.choices([1,2], weights=[70, 30], k=1)[0]
            radius = size_mesh_back/60
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
        points = self.model_mesh_back.getPoints()
        cuadrilaterals = self.model_mesh_back.getQuadrilaterals()    
        points_boundary_top,points_boundary_bottom ,points_boundary_left ,points_boundary_right = self.model_mesh_back.getBoundaryPoints()
                
        self.axis_mesh_back_result = ItemResultAxisMeshBack(x,y,w, h)
        self.scene_result.addItem(self.axis_mesh_back_result)
        self.axis_mesh_back_result.setZValue(10)
        self.label_mesh_back_result = ItemResultLabelGridMeshBack(self.scene_result,x,y,w, h,
                                                                  points_boundary_top,
                                                                  points_boundary_bottom, 
                                                                  points_boundary_left, 
                                                                  points_boundary_right)
        self.scene_result.addItem(self.label_mesh_back_result)
        self.label_mesh_back_result.setZValue(9)
        
        self.grid_mesh_back_result = ItemResultGridMeshBack(x,y,w, h, points, cuadrilaterals )
        self.scene_result.addItem(self.grid_mesh_back_result)
        self.grid_mesh_back_result.setZValue(8)
        
        self.base_mesh_back_result = ItemResultBaseMeshBack(x,y,w, h)
        self.scene_result.addItem(self.base_mesh_back_result)
        self.base_mesh_back_result.setZValue(100)
        self.base_mesh_back_result.setVisible(False)
        

        self.color_bar_result = ItemResultColorBar(x,y)
        self.scene_result.addItem(self.color_bar_result)
        self.color_bar_result.setZValue(100)
        
        scale_bar = h/250 
        self.color_bar_result.setScale(scale_bar)
        self.color_bar_result.setPos(x+w+(w/5),y)
        self.color_bar_result.setVisible(False)


    def clearSceneResult(self):
        self.scene_result.clear()
        self.__item_result_nodes = []
        
        
    def updateResult(self ): 
        self.clearSceneResult()
        self.drawItemBasicScene()
        self.drawItemPointsScene()
        self.signal_reset_result.emit()
        
        #self.view_result.resetView()
        
        
    # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    # ::::::::::::::::::::              BASE DE DATOS              ::::::::::::::::::::
    # :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    
    
    def clearResult(self):
        self.model_project_current_repository.deleteAllResultDB()
        
    
    def updateResultDataBase(self, gravity, dampfac):
        self.__data_base = {
            'GRAVEDAD': gravity,
            'DAMPFAC': dampfac
        }
        self.model_project_current_repository.updateResultDataBaseDB(
             gravity=gravity,
             dampfac=dampfac
            )


    def updateResultMeshBack(self, size_dx, size_dy, size_element,color,points,quadrilaterals,points_boundary_top,points_boundary_bottom,points_boundary_left,points_boundary_right,nodes_boundary_top,nodes_boundary_bottom,nodes_boundary_left,nodes_boundary_right):

        self.model_mesh_back = ModelMeshBack(
            scene_draw=self.scene_result,
            model_project_current_repository=self.model_project_current_repository,
            size_dx=size_dx,
            size_dy=size_dy,
            size_element=size_element,
            color_style=color,
            points=points,
            quadrilaterals=quadrilaterals,
            points_boundary_top=points_boundary_top,
            points_boundary_bottom=points_boundary_bottom,
            points_boundary_left=points_boundary_left,
            points_boundary_right=points_boundary_right,
            nodes_boundary_top=nodes_boundary_top,
            nodes_boundary_bottom=nodes_boundary_bottom,
            nodes_boundary_left=nodes_boundary_left,
            nodes_boundary_right=nodes_boundary_right
        )
        
        self.model_project_current_repository.updateResultMeshBackDB(
            size_dx=size_dx,
            size_dy=size_dy,
            size_element=size_element,
            color=color,
            points=points,
            quadrilaterals=quadrilaterals,
            points_boundary_top=points_boundary_top,
            points_boundary_bottom=points_boundary_bottom,
            points_boundary_left=points_boundary_left,
            points_boundary_right=points_boundary_right,
            nodes_boundary_top=nodes_boundary_top,
            nodes_boundary_bottom=nodes_boundary_bottom,
            nodes_boundary_left=nodes_boundary_left,
            nodes_boundary_right=nodes_boundary_right
            )



    
    def updateResultDataTimes(self, id_material, courant_number, analysis_time, fps, dt_analysis, dt_graphic, analysis_steps, graphic_steps, speed_cp, time_reached):
        self.__data_times = {
            'MATERIAL': id_material,
            'NUMEROCOURANT': courant_number,
            'TIEMPOANALISIS': analysis_time,
            'FPS': fps,
            'DTANALISIS': dt_analysis,
            'DTGRAFICAR': dt_graphic,
            'PASOSANALISIS': analysis_steps,
            'PASOSGRAFICAR': graphic_steps,
            'VELOCIDADCP': speed_cp,
            'TIEMPOALCANZADO': time_reached
        }
        self.model_project_current_repository.updateResultDataTimesDB(
            id_material=id_material,
            courant_number=courant_number,
            analysis_time=analysis_time,
            fps=fps,
            dt_analysis=dt_analysis,
            dt_graphic=dt_graphic,
            analysis_steps=analysis_steps,
            graphic_steps=graphic_steps,
            speed_cp=speed_cp,
            time_reached=time_reached
            )


    def updateResultTimes(self,analysis_times=None ):
 
        if analysis_times != None:
            self.__analysis_times = analysis_times

        self.model_project_current_repository.updateResultTimesDB(
            analysis_times=analysis_times,
            )
        
    def updateResultTimeGraphic(self, graphic_time):
        if graphic_time != None:
            self.__graphic_time = graphic_time
            self.no_data = len(graphic_time)
        
        self.model_project_current_repository.updateResultTimeGraphicDB(
            graphic_time=graphic_time,
            )
        
        
    def updateResultMin(self, corx, cory, sigxx, sigyy, sigxy, epsxx, epsyy, epsxy):
        self.__result_min ={
            'CORX': corx,
            'CORY': cory,
            'SIGXX': sigxx,
            'SIGYY': sigyy,
            'SIGXY': sigxy,
            'EPSXX': epsxx,
            'EPSYY': epsyy,
            'EPSXY': epsxy
        }
        
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
        self.__result_max ={
            'CORX': corx,
            'CORY': cory,
            'SIGXX': sigxx,
            'SIGYY': sigyy,
            'SIGXY': sigxy,
            'EPSXX': epsxx,
            'EPSYY': epsyy,
            'EPSXY': epsxy
        }     
        
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


        self.model_project_current_repository.addResultNodeDB(
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
        

    def addResultProperty(self, id_property, name, modulus_elasticity, poisson_ratio, cohesion, friction_angle, density,  angle_dilatancy):

        self.__properties[id_property] = {
            "NAME": name,
            "MODULOELASTICIDAD": modulus_elasticity,        #E KPa
            "RELACIONPOISSON": poisson_ratio,               #v -/-
            "COHESION": cohesion,                           #C' KPa
            "ANGULOFRICCION": friction_angle,               #Phi °
            "DENSIDAD": density,                            #P kg/m3
            "ANGULODILATANCIA": angle_dilatancy             #Psi °
        }

        self.model_project_current_repository.addResultPropertyDB(
            id_property=id_property,
            name=name,
            modulus_elasticity=modulus_elasticity,
            poisson_ratio=poisson_ratio,
            cohesion=cohesion,
            friction_angle=friction_angle,
            density=density,
            angle_dilatancy=angle_dilatancy
            )
        

    def addResultPointMaterial(self, id_MP, name, color, points,id_property):
        self.__point_materials[id_MP] = {
            "NAME": name,
            "COLOR": color,
            "POINTS": points,
            "IDPROPIEDAD": id_property
        }

        self.model_project_current_repository.addResultPointMaterialDB(
            id_MP=id_MP,
            name=name,
            color=color,
            points=points,
            id_property=id_property
            )

     
    def addResultBoundary(self, id_boundary, name, nodes, points,restrictionX, restrictionY):
        self.__boundarys[id_boundary] = {
            "NAME": name,
            "NODES": nodes,
            "POINTS": points,
            "Tx": restrictionX,
            "Ty": restrictionY
        }

        self.model_project_current_repository.addResultBoundaryDB(
            id_boundary=id_boundary,
            name=name,
            nodes=nodes,
            points=points,
            restrictionX=restrictionX,
            restrictionY=restrictionY
            )
    
