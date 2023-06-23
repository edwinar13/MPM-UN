
from PySide6.QtCore import (QFile, QTime,Signal, QObject)
from clases.Modelo.model_Mesh import ModelMesh
from clases.Modelo.model_MaterialPoint import ModelMaterialPoint
from clases.Modelo.model_ProjectCurrentRepository import ModelProjectCurrentRepository
import uuid

class ModelProjectCurrentOK():


    def __init__(self,scene, path_doc) -> None:
        super().__init__() 
        self.__scene = scene
        self.__path_doc = path_doc
        self.__name_doc = path_doc.split('/')[-1]
        self.__name = None
        self.__location = None
        self.__author = None 
        self.__description = None
        self.__gravity = None

        self.model_project_current_repository = ModelProjectCurrentRepository(self.__path_doc)

        self.items_models=[]
        self.meshs_models=[]
        self.material_point_models={}


        
        self.__initData()
        self.__initMesh()
        self.__initMaterialPoint()
        

    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS CONFIGURAR        ::::::::::::::::::::
	###############################################################################
    
    def __initData(self):
        # Informacion
        data = self.model_project_current_repository.readInformationDB()
        self.__name = data["NOMBREPROYECTO"]
        self.__location = data["LOCALIZACION"]
        self.__author = data["AUTOR"] 
        self.__description = data["DESCRIPCION"]
        # Configuracion
        data = self.model_project_current_repository.readConfigDB()
        self.__gravity = data["GRAVEDAD"]
    
    def __initMesh(self):
        meshs = self.model_project_current_repository.readMeshTriangularDB()
        for mesh in meshs:
            pass
        meshs = self.model_project_current_repository.readMeshRectangularDB()
        for mesh in meshs:
            pass
        return
        meshs = self.selectMeshDB()["TRIANGULARES"]
        for mesh_name in meshs:
            name = meshs[mesh_name]["name"]
            color = meshs[mesh_name]["color"]
            points = meshs[mesh_name]["points"]
            triangles = meshs[mesh_name]["triangles"]

            model_mesh = ModelMesh(name=name, color=color, points=points, triangles=triangles)
            self.meshs.append(model_mesh)

    def __initMaterialPoint(self):
        materials_points = self.model_project_current_repository.readMaterialPointhDB()
        for id_material_point in materials_points:
            name = materials_points[id_material_point]["NAME"]
            color = materials_points[id_material_point]["COLOR"]
            points = materials_points[id_material_point]["POINTS"]
            self.addMaterialPointToCurrentProject(
                id=id_material_point,
                name=name,
                color=color,
                points=points)


    ###############################################################################
	# ::::::::::::::::::::         GETTERS Y SETTERS           ::::::::::::::::::::
	###############################################################################  

    def getPathDoc(self):
        return self.__path_doc
    
    def getNameDoc(self):
        return self.__name_doc

    def getName(self):
        return self.__name
    
    def getLocation(self):
        return self.__location

    def getAuthor(self):
        return self.__author

    def getDescription(self):
        return self.__description
    
    def getGravity(self):
        return self.__gravity
    
    def getData(self):
        return[self.__name, self.__location, self.__author, self.__description, self.__gravity]
       

    ###############################################################################
    # ::::::::::::::::::::              GENERALES              ::::::::::::::::::::
    ###############################################################################

    # ::::::::::::::::::::                MALLAS               ::::::::::::::::::::


    # ::::::::::::::::::::           PUNTOS MATERIALES         ::::::::::::::::::::

    def createMaterialPoint(self, name, color, points):
        id = str(uuid.uuid4())
        self.model_project_current_repository.createMaterialPointDB(
            id_MP = id,
            name = name, 
            color = color, 
            points = points)
        self.addMaterialPointToCurrentProject(
                id=id,
                name=name,
                color=color,
                points=points)
        return id
    
    def addMaterialPointToCurrentProject(self,id, name, color, points):    
        model_material_point = ModelMaterialPoint(scene_draw=self.__scene,
                                                      model_project_current_repository=self.model_project_current_repository,
                                                      id=id,
                                                      name=name,
                                                      color=color,
                                                      points=points)
        self.material_point_models[id]=model_material_point        

    def getModelsPointsMaterials(self):
        return self.material_point_models
    
    def deleteMaterialPoint(self, id):
        self.model_project_current_repository.deleteMaterialPointDB(id)        
        removed_model_material_point = self.material_point_models.pop(id)
        removed_model_material_point.deleteMaterialPoint()
        del removed_model_material_point


    ###############################################################################
    # ::::::::::::::::::::          GUARDAR PROYECTO           ::::::::::::::::::::
    ###############################################################################

    def checkProjectChanges(self):
        return self.model_project_current_repository.checkProjectChanges()

    def saveDataDb(self):
        return self.model_project_current_repository.saveDataDb()
