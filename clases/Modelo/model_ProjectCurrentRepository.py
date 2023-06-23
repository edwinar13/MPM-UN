
from PySide6.QtCore import (QFile)
import json
import os

class ModelProjectCurrentRepository():
    """
    Clase que representa un repositorio que interactua con la base de datos del proyecto actual.

    Args:
        path_project_current (str): Ruta del proyecto actual.

    Attributes:
        __path_db_project (str): Ruta de la base de datos del proyecto.
        __original_copy_db_project (dict): Copia original de la base de datos del proyecto.
        __unguarded_copy_db_project (dict): Copia no protegida de la base de datos del proyecto.
        __name_doc_py (str): Nombre del archivo del documento.

    """
    def __init__(self, path_project_current) -> None:
        super().__init__()

        self.__path_db_project = path_project_current
        self.__original_copy_db_project = None
        self.__unguarded_copy_db_project = None
        self.__name_doc_py = os.path.basename(__file__) 


        #inicializa las copias de la base de datos del proyecto
        self.__initDb()


    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS CONFIGURAR        ::::::::::::::::::::
	###############################################################################
    def __initDb(self):
        """
        Realiza una copia original de la base de datos del proyecto y otra original.

        """

        BD = self.__path_db_project
        if QFile.exists(BD):            
            with open(BD, 'r') as a: 
                self.__original_copy_db_project = json.load(a)
                a.close()

            with open(BD, 'r') as b: 
                self.__unguarded_copy_db_project = json.load(b)
                b.close()
        else:            
            print("[Doc: {}] No se encontró la base de datos de {}".format(self.__name_doc_py,BD))   
    
    # C R U D
    # CREATE: crear/agregar registro 
    # READ: leer registro 
    # UPDATE: actualizar registro
    # DELETE: eliminar registro 

   
    ###############################################################################
	# ::::::::::::::::::::        MÉTODOS DB INFORMACION       ::::::::::::::::::::
	###############################################################################   
    def readInformationDB(self): 
        """
        Lee la información básica almacenada en la base de datos del proyecto actual.

        Returns:
            dict: Diccionario con la información básica almacenada en la base de datos.
        """

        return self.__unguarded_copy_db_project['INFORMACION']
    
    def updateInformationDB(self, name_project=None, location=None,
                                 author=None,  description=None):
        """
        Actualiza la información la básica almacenada en la base de datos del proyecto actual.

        Args:
            name_project (str): Nombre del proyecto. (default= None)
            location (str): Localización del proyecto. (default= None)
            author (str): Autor del proyecto. (default= None)
            description (str): Descripción del proyecto. (default= None)

        Returns:
            bool: True si la actualización fue exitosa, False en caso contrario.

        """
        try:  
            if name_project != None:          
                self.__unguarded_copy_db_project['INFORMACION']['NOMBREPROYECTO']=name_project
            if location != None:          
                self.__unguarded_copy_db_project['INFORMACION']['LOCALIZACION']=location
            if author != None:        
                self.__unguarded_copy_db_project['INFORMACION']['AUTOR']=author
            if description != None:          
                self.__unguarded_copy_db_project['INFORMACION']['DESCRIPCION']=description
            
            return True
      
        except BaseException as err:
            print("[Doc: {}] Error al actualizar registro en <INFORMACION> de la base de datos".format(self.__name_doc_py))
            print("[Tipo: {}, Erro: {}]".format(type(err),err))
            return False 

    ###############################################################################
	# ::::::::::::::::::::      MÉTODOS DB CONFIGURACION       ::::::::::::::::::::
	###############################################################################   
    def readConfigDB(self):
        """
        Lee la configuración básica almacenada en la base de datos del proyecto actual.

        Returns:
            dict: Diccionario con la configuración básica almacenada en la base de datos.
        """
        return self.__unguarded_copy_db_project['CONFIGURACION']
    
    def updateConfigDB(self, gravity = None):        
        """Actualiza la configuración básica almacenada en la base de datos del proyecto actual.

        Args:
            gravity(float): Valor de la gravedad para el proyecto (default= None).

        Returns:
            bool: True si la actualización fue exitosa, False en caso contrario.

        """ 


        try:  
            if gravity != None:          
                self.__unguarded_copy_db_project['CONFIGURACION']['GRAVEDAD']=gravity
            return True
        except BaseException as err:
            print("[Doc: {}]  Error al actualizar registro en <CONFIGURACION> de la base de datos {}".format(self.__name_doc_py))
            print("[Tipo: {}, Erro: {}]".format(type(err),err))
            return False

    ###############################################################################
	# ::::::::::::::::::::        MÉTODOS DB ITEMSDIBUJO       ::::::::::::::::::::
	###############################################################################   
    
	# ::::::::::::::::::::        PUNTOS       ::::::::::::::::::::
    def createItemPointDrawDB(self, id_point, name, coordinates):
        try:           
            self.__unguarded_copy_db_project['ITEMSDIBUJO']['PUNTOS'][id_point]["NAME"]=name
            self.__unguarded_copy_db_project['ITEMSDIBUJO']['PUNTOS'][id_point]["COORDINATES"]=coordinates
            return True
        except BaseException as err:
            print("[Doc: {}] Error al agregar registro en <ITEMSDIBUJO> de la base de datos".format(self.__name_doc_py))
            print("[Tipo: {}, Erro: {}]".format(type(err),err))
            return False
        
    def readItemPointDrawDB(self):
        """
        Lee los items de dibujo (puntos) almacenados en la base de datos del proyecto actual.
        Returns:
            (dict): Diccionario con los items de dibujo (puntos) del proyecto.
        """

        return self.__unguarded_copy_db_project['ITEMSDIBUJO']['PUNTOS']
    
    def updateItemPointDrawDB(self, id_point, name=None, coordinates=None, lines=None):
        """Actualiza los items de dibujo (puntos) almacenados en la base de datos del proyecto actual.

        Args:
            
            id_point (str): id del item/punto. (default= None)
            name (str): nombre del item/punto. (default= None)
            coordinates (list): coordenadas del item/punto. (default= None)
            lines (list): lista de lineas asociadas al punto. (default= None)

        Returns:
            bool: True si la actualización fue exitosa, False en caso contrario.

        """ 
        try:  
            if  id_point in self.__unguarded_copy_db_project['ITEMSDIBUJO']['PUNTOS']:
                if name != None:          
                    self.__unguarded_copy_db_project['ITEMSDIBUJO']['PUNTOS'][id_point]["NAME"]=name
                if coordinates != None:          
                    self.__unguarded_copy_db_project['ITEMSDIBUJO']['PUNTOS'][id_point]["COORDINATES"]=coordinates
                if lines != None:          
                    self.__unguarded_copy_db_project['ITEMSDIBUJO']['PUNTOS'][id_point]["LINES"]=lines
            return True
        except BaseException as err:
            print("[Doc: {}] Error al actualizar registro en <ITEMSDIBUJO> de la base de datos".format(self.__name_doc_py))
            print("[Tipo: {}, Erro: {}]".format(type(err),err))
            return False
        
    def deleteItemPointDrawDB(self, id_point):
        """elimina el item de dibujo (puntos) de la copia sin guardar de la db del proyecto.
        Args:
            id_item_point (dic): id del item a eliminar.
        Returns:
            (bool): 
                : True >> si se agrega correctamente los items al proyecto
                : False >> si no se encontró la db del proyecto.
        """ 
        try:  
            if  id_point in self.__unguarded_copy_db_project['ITEMSDIBUJO']['PUNTOS']:
                del self.__unguarded_copy_db_project['ITEMSDIBUJO']['PUNTOS'][id_point]
           
            return True
        except BaseException as err:
            print("[Doc: {}] Error al eliminar registro en <ITEMSDIBUJO> de la base de datos".format(self.__name_doc_py))
            print("[Tipo: {}, Erro: {}]".format(type(err),err))
            return False
    
    # ::::::::::::::::::::        LINEAS       ::::::::::::::::::::
    def createItemLineDrawDB(self, id_line, name, id_start_point, id_end_point):
        try:                 
            self.__unguarded_copy_db_project['ITEMSDIBUJO']['LINEAS'][id_line]["NAME"]=name
            self.__unguarded_copy_db_project['ITEMSDIBUJO']['LINEAS'][id_line]["IDSTARTPOINT"]=id_start_point
            self.__unguarded_copy_db_project['ITEMSDIBUJO']['LINEAS'][id_line]["IDENDPOINT"]=id_end_point
            return True
        except BaseException as err:
            print("[Doc: {}] Error al agregar registro en <ITEMSDIBUJO> de la base de datos".format(self.__name_doc_py))            
            print("[Tipo: {}, Erro: {}]".format(type(err),err))
            return False
    
    def readItemLineDrawDB(self):

        """
        Lee los items de dibujo (lineas) almacenados en la base de datos del proyecto actual.
        Returns:
            (dict): Diccionario con los items de dibujo (lineas) del proyecto.
        """
        return self.__unguarded_copy_db_project['ITEMSDIBUJO']['LINEAS']
    
    def updateItemLineDrawDB(self, id_line, name=None, id_start_point=None, id_end_point=None):


        try:  
            if  id_line in self.__unguarded_copy_db_project['ITEMSDIBUJO']['LINEAS']:
                if name != None:          
                    self.__unguarded_copy_db_project['ITEMSDIBUJO']['LINEAS'][id_line]["NAME"]=name
                if id_start_point != None:          
                    self.__unguarded_copy_db_project['ITEMSDIBUJO']['LINEAS'][id_line]["IDSTARTPOINT"]=id_start_point
                if id_end_point != None:          
                    self.__unguarded_copy_db_project['ITEMSDIBUJO']['LINEAS'][id_line]["IDENDPOINT"]=id_end_point
            return True
        except BaseException as err:
            print("[Doc: {}] Error al actualizar registro en <ITEMSDIBUJO> de la base de datos".format(self.__name_doc_py))
            print("[Tipo: {}, Erro: {}]".format(type(err),err))
            return False
    
    def deleteItemLineDrawDB(self, id_line):
        try:  
   
            if  id_line in self.__unguarded_copy_db_project['ITEMSDIBUJO']['LINEAS']:
                del self.__unguarded_copy_db_project['ITEMSDIBUJO']['LINEAS'][id_line]
            
            return True
        except BaseException as err:
            print("[Doc: {}] Error al eliminar registro en <ITEMSDIBUJO> de la base de datos".format(self.__name_doc_py))
            print("[Tipo: {}, Erro: {}]".format(type(err),err))
            return False

    ###############################################################################
	# ::::::::::::::::::::        MÉTODOS DB MALLA       ::::::::::::::::::::
	############################################################################### 
    # ::::::::::::::::::::        TRIANGULARES       ::::::::::::::::::::
    def createMeshTriangularDB(self, id_Mesh, name, color, points, triangles):

        """
        "TRIANGULARES": {
            "edwin": {
                "name": "edwin",
                "color": "#ffffff",
                "points": [
                    [
                        19.83037775327739,
                        5.083209338442088
                    ]
                ],
                "triangles": [
                    [
                        77,
                        12,
                        148
                    ]
                ]
            },
        """
        try:  
          
            self.__unguarded_copy_db_project['MALLAS']['TRIANGULARES'][id_Mesh]["NAME"]=name
            self.__unguarded_copy_db_project['MALLAS']['TRIANGULARES'][id_Mesh]["COLOR"]=color
            self.__unguarded_copy_db_project['MALLAS']['TRIANGULARES'][id_Mesh]["POINTS"]=points
            self.__unguarded_copy_db_project['MALLAS']['TRIANGULARES'][id_Mesh]["TRIANGLES"]=triangles
            return True
        except BaseException as err:
            print("[Doc: {}] Error al agregar registro en <MALLAS> de la base de datos".format(self.__name_doc_py))
            print("[Tipo: {}, Erro: {}]".format(type(err),err))
            return False    
    
    def readMeshTriangularDB(self):
        """
        Lee las mallas (triangulares) almacenadas en la base de datos del proyecto actual.
        Returns:
            (dict): Diccionario con las mallas (triangulares) del proyecto.
        """   
        return self.__unguarded_copy_db_project['MALLAS']['TRIANGULARES']
    
    def updateMeshTriangularDB(self,id_Mesh, name=None, color=None, points=None, triangles=None):
        try:                  
            if id_Mesh in self.__unguarded_copy_db_project['MALLAS']['TRIANGULARES']:
                if name != None:   
                    self.__unguarded_copy_db_project['MALLAS']['TRIANGULARES'][id_Mesh]["NAME"]=name
                if color != None:   
                    self.__unguarded_copy_db_project['MALLAS']['TRIANGULARES'][id_Mesh]["COLOR"]=color
                if points != None:   
                    self.__unguarded_copy_db_project['MALLAS']['TRIANGULARES'][id_Mesh]["POINTS"]=points
                if triangles != None:   
                    self.__unguarded_copy_db_project['MALLAS']['TRIANGULARES'][id_Mesh]["TRIANGLES"]=triangles
            return True
        except BaseException as err:
            print("[Doc: {}] Error al actualizar registro en <MALLAS> de la base de datos".format(self.__name_doc_py))
            print("[Tipo: {}, Erro: {}]".format(type(err),err))
            return False    
    
    def deleteMeshTriangularDB(self, id_Mesh):
        """Elimina la malla en la copia sin guardar de la db del proyecto.

        Args:
            name (str): Nombre de la malla a eliminar (default= None).

        Returns:
            (bool): 
                : True >> si se agrega correctamente la malla al proyecto
                : False >> si no se encontró la db del proyecto.

        """         
 
        try:  

            if id_Mesh in self.__unguarded_copy_db_project['MALLAS']['TRIANGULARES']:
                del self.__unguarded_copy_db_project['MALLAS']['TRIANGULARES'][id_Mesh]
            return True
        except BaseException as err:
            print("[Doc: {}] Error al eliminar registro en <MALLAS> de la base de datos".format(self.__name_doc_py))
            print("[Tipo: {}, Erro: {}]".format(type(err),err))
            return False    

    # ::::::::::::::::::::        RECTANGULARES       ::::::::::::::::::::
    def createMeshRectangularDB(self, id_Mesh,  name, color, points, rectangles):
        try:  
        
            self.__unguarded_copy_db_project['MALLAS']['RECTANGULARES'][id_Mesh]["NAME"]=name
            self.__unguarded_copy_db_project['MALLAS']['RECTANGULARES'][id_Mesh]["COLOR"]=color
            self.__unguarded_copy_db_project['MALLAS']['RECTANGULARES'][id_Mesh]["POINTS"]=points
            self.__unguarded_copy_db_project['MALLAS']['RECTANGULARES'][id_Mesh]["RECTANGLES"]=rectangles
            return True
        except BaseException as err:
            print("[Doc: {}] Error al agregar registro en <MALLAS> de la base de datos".format(self.__name_doc_py))
            print("[Tipo: {}, Erro: {}]".format(type(err),err))
            return False    
    
    def readMeshRectangularDB(self):
        """
        Lee las mallas (rectangulares) almacenadas en la base de datos del proyecto actual.
        Returns:
            (dict): Diccionario con las mallas (rectangulares) del proyecto.
        """    
        return self.__unguarded_copy_db_project['MALLAS']['RECTANGULARES']
    
    def updateMeshRectangularDB(self,id_Mesh, name=None, color=None, points=None, rectangles=None):
        """
        triangle_type:
            TRIANGULARES
            RECTANGULARES
        """
        try:  
            if id_Mesh in self.__unguarded_copy_db_project['MALLAS']['RECTANGULARE']:
                if name != None:   
                    self.__unguarded_copy_db_project['MALLAS']['RECTANGULARES'][id_Mesh]["NAME"]=name
                if color != None:   
                    self.__unguarded_copy_db_project['MALLAS']['RECTANGULARES'][id_Mesh]["COLOR"]=color
                if points != None:   
                    self.__unguarded_copy_db_project['MALLAS']['RECTANGULARES'][id_Mesh]["POINTS"]=points
                if rectangles != None:   
                    self.__unguarded_copy_db_project['MALLAS']['RECTANGULARES'][id_Mesh]["RECTANGLES"]=rectangles
            return True
        except BaseException as err:
            print("[Doc: {}] Error al actualizar registro en <MALLAS> de la base de datos".format(self.__name_doc_py))
            print("[Tipo: {}, Erro: {}]".format(type(err),err))
            return False    
    
    def deleteMeshRectangularDB(self, id_Mesh):
        """Elimina la malla en la copia sin guardar de la db del proyecto.

        Args:
            name (str): Nombre de la malla a eliminar (default= None).

        Returns:
            (bool): 
                : True >> si se agrega correctamente la malla al proyecto
                : False >> si no se encontró la db del proyecto.

        """ 

        try:  

            if id_Mesh in self.__unguarded_copy_db_project['MALLAS']['RECTANGULARES']:
                del self.__unguarded_copy_db_project['MALLAS']['RECTANGULARES'][id_Mesh]
            return True
        except BaseException as err:
            print("[Doc: {}] Error al eliminar registro en <MALLAS> de la base de datos".format(self.__name_doc_py))
            print("[Tipo: {}, Erro: {}]".format(type(err),err))
            return False    

    ###############################################################################
	# ::::::::::::::::::::       MÉTODOS DB PUNTO MATERIAL     ::::::::::::::::::::
	###############################################################################   
    def createMaterialPointDB(self, id_MP, name, color, points):       
        #try:                 
        self.__unguarded_copy_db_project['PUNTOSMATERIAL'][id_MP] = {
            "NAME": name,
            "COLOR": color,
            "POINTS": points
        }
        self.saveDataDb()
        return True
        '''
        except BaseException as err:
            print("[Doc: {}] Error al agregar registro en <PUNTOSMATERIAL> de la base de datos".format(self.__name_doc_py))
            print("[Tipo: {}, Erro: {}]".format(type(err),err))
            return False    
        '''
    
    def readMaterialPointhDB(self):
        """
        Lee los puntos materiales almacenados en la base de datos del proyecto actual.
        Returns:
            (dict): Diccionario con los puntos materiales del proyecto.
        """ 
        return self.__unguarded_copy_db_project['PUNTOSMATERIAL']
    
    def updateMaterialPointDB(self,id_MP, name=None, color=None, points=None):
        try: 
            if id_MP in self.__unguarded_copy_db_project['PUNTOSMATERIAL']: 
                if name != None:                      
                    self.__unguarded_copy_db_project['PUNTOSMATERIAL'][id_MP]["NAME"]=name
                if color != None:   
                    self.__unguarded_copy_db_project['PUNTOSMATERIAL'][id_MP]["COLOR"]=color
                if points != None:   
                    self.__unguarded_copy_db_project['PUNTOSMATERIAL'][id_MP]["COLOR"]=points
            return True
        except BaseException as err:
            print("[Doc: {}] Error al actualizar registro en <PUNTOSMATERIAL> de la base de datos".format(self.__name_doc_py))
            print("[Tipo: {}, Erro: {}]".format(type(err),err))
            return False    
    
    def deleteMaterialPointDB(self, id_MP):
        try:            
            if id_MP in self.__unguarded_copy_db_project['PUNTOSMATERIAL']:
                del self.__unguarded_copy_db_project['PUNTOSMATERIAL'][id_MP]
            return True
        except BaseException as err:
            print("[Doc: {}] Error al eliminar registro en <PUNTOSMATERIAL> de la base de datos".format(self.__name_doc_py))
            print("[Tipo: {}, Erro: {}]".format(type(err),err))
            return False    
  
    ###############################################################################
	# ::::::::::::::::::::          MÉTODOS  GENERALES         ::::::::::::::::::::
	###############################################################################
    def checkProjectChanges(self):
        
        """ Verifica si hay cambios en el proyecto.

        Returns:
            (bool):
                : True >> si hay cambios en el proyecto
                : False >> si no hay cambios en el proyecto

        """

        if(self.__original_copy_db_project == self.__unguarded_copy_db_project):
            return False
        else:
            return True

    def saveDataDb(self):
        """Guarda la información de la copia sin guardar en la db del proyecto.
        
        Returns:
            (bool): 
                : True >> si se guardo correctamente en la base de datos
                : False >> si no se guardo correctamente en la base de datos

                
        """
        BD=self.__path_db_project


        if QFile.exists(BD):		  
            #try:
                # se guarda en el archivo
                with open(BD, 'w') as a:
                    a.write(json.dumps(self.__unguarded_copy_db_project)) 
                    a.close()
                            
                # se actualiza la copia original
                with open(BD, 'r') as b: 
                    self.__original_copy_db_project = json.load(b)
                    b.close()
                print("Guardo correctamente en la base de datos")   
                
                validacion=True
            
            #except BaseException as err:
            #    print("[Doc: {}]  Error al agregar registro en <CONFIGURACION> de la base de datos {}".format(self.__name_doc_py,BD))
            #    print("[Tipo: {}, Erro: {}]".format(type(err),err))
            #    validacion=False
            
        else:  
            print("[Doc: {}] No se encontró la base de datos de {}".format(self.__name_doc_py,BD))          
            validacion=False
        return validacion

    def projectSaveAs(self, new_path_file):  
        """Guarda la información de la copia sin guardar en la nueva ruta de la db del proyecto.

        Args:
            new_path_file(str): Ruta para crear el archivo.

        Returns:
            (bool): 
                : True >> si se guardo correctamente en la base de datos
                : False >> si no se guardo correctamente en la base de datos

        """

        BD=new_path_file	  
        try:
            # se guarda en el archivo
            with open(BD, 'w') as a:
                a.write(json.dumps(self.__unguarded_copy_db_project)) 
                a.close()
            print("Guardo como, correctamente en la base de datos")   
            
            validacion=True
        
        except BaseException as err:
            print("[Doc: {}]  Error al guardar como {}".format(self.__name_doc_py,BD))
            print("[Tipo: {}, Erro: {}]".format(type(err),err))
            validacion=False
        
        return validacion


