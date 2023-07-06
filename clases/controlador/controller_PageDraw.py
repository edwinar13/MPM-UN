
""" Este módulo contiene controlador de la vista pagina home """
from PySide6.QtCore import ( QFile, Slot, QObject,QPointF)

from clases.general_functions import isNumber
from clases.Vista.view_PageDraw import  ViewPageDraw
from clases.Modelo.model_ProjectCurrent import ModelProjectCurrent


from clases.Controlador.controller_graphicsDraw import ControllerGraphicsDraw

from clases.Controlador.controller_MenuData import ControllerMenuData
from clases.Controlador.controller_MenuMesh import ControllerMenuMesh
from clases.Controlador.controller_MenuPointMaterial import ControllerMenuPointMaterial
from clases.Controlador.controller_MenuBoundary import ControllerMenuBoundary
import math


class ControllerPageDraw(QObject):

    def __init__(self, controller_main) -> None:    
        super().__init__()

        self.controller_main = controller_main 


        
        self.current_project = None

        #Crea la vista page draw
        self.view_page_draw = ViewPageDraw()

        self.controller_graphics_draw = ControllerGraphicsDraw()

        self.view_page_draw.setViewGraphicsWidget(self.controller_graphics_draw.getView1())
        self.view_page_draw.setViewGraphicsWidget(self.controller_graphics_draw.getView2())
        
        self.viewsTwo()


        # crea el controlador de los menus 
        self.controller_menu_data = ControllerMenuData()
        self.controller_menu_mesh = ControllerMenuMesh()
        self.controller_menu_pointMaterial = ControllerMenuPointMaterial()
        self.controller_menu_boundary = ControllerMenuBoundary()

        self.view_page_draw.setMenuWidget("data", self.controller_menu_data.getView())
        self.view_page_draw.setMenuWidget("mesh", self.controller_menu_mesh.getView())
        self.view_page_draw.setMenuWidget("pointMaterial", self.controller_menu_pointMaterial.getView())
        self.view_page_draw.setMenuWidget("boundary", self.controller_menu_boundary.getView())

        self.controller_main.view_main_window.signal_action_menu_viewDraw.connect(self.actionMenuSup)
        
        self.view_page_draw.signal_zoom_draw.connect(self.zoomDraw)
        self.view_page_draw.signal_end_draw_geometry.connect(self.endDrawGeometry)
        self.view_page_draw.signal_end_draw_mesh.connect(self.endDrawMesh)
        self.view_page_draw.signal_deselect_draw_geometry.connect(self.deselectDrawGeometry)
  

        self.controller_menu_mesh.signal_new_mesh.connect(self.addMesh)
        self.controller_menu_mesh.signal_edit_mesh.connect(self.editMesh)
        self.controller_menu_mesh.signal_end_draw_geometry.connect(self.endDrawGeometry)

        
        self.controller_graphics_draw.signal_msn_console.connect(self.msnConsoleView)
        self.controller_graphics_draw.signal_msn_label_console.connect(self.msnLabelConsole)
        self.controller_graphics_draw.signal_end_draw_geometry.connect(self.endDrawGeometry)


        self.view_page_draw.signal_command_console.connect(self.commandConsole)

    def buttonStatusBar(self, ToolButton_mode):
        self.controller_graphics_draw.modeButtonStatusBar(ToolButton_mode)


    @Slot()
    def addMesh(self):
        self.controller_menu_pointMaterial.setListBaseMeshView()
    
    @Slot()
    def editMesh(self):
        self.controller_menu_pointMaterial.setListBaseMeshView()
    


    @Slot(list)
    def commandConsole(self, data):
        """Método presionar enter en el line edit de la consola para ejecutar el comando."""

        data_consola = data[0]
        current_command = data[1]
        descrip_command = data[2]

        
        commands =     ["point", "line",  "erase", "move", "copy", "rotate", "zoom", "views", "import", "intersection"]
        commands_min = ["p",     "l",     "er",   "mo",   "co",    "ro",      "z",    "v", "im", "in"]
        
        #se ejecuta si la entrada es un comando
        if ((data_consola in commands) or (data_consola in commands_min)) and current_command == "" :
            if data_consola in commands:
                index = commands.index(data_consola)
            elif  data_consola in commands_min:
                index = commands_min.index(data_consola)

            command = commands[index]

            if command == "point" :
                self.current_project.commandPoint({"step":1, "data":None})        

            elif command == "line" :
                self.current_project.commandLine({"step":1, "data":None})    

            elif command == "move" :
                self.current_project.commandMove({"step":1, "data":None})    

            elif command == "copy" :
                self.current_project.commandCopy({"step":1, "data":None})    

            elif command == "rotate" :
                self.current_project.commandRotate({"step":1, "data":None})    
                
            elif command == "erase" :
                self.current_project.commandErase({"step":1, "data":None})    

            elif command == "import" :
                self.current_project.commandImport({"step":1, "data":None})    

            elif command == "intersection" :
                self.current_project.commandIntersection({"step":1, "data":None})    

            elif command == "zoom" :
                self.msnLabelAndView([command,"[Extents Window] <E>:", None])

            elif command == "views" :
                self.msnLabelAndView([command,"[1 2] <1>:",None])
        
        #se ejecuta si ya hay un comando activo
        elif current_command in commands:



            #exit: salir de la edición de objeto
            if (data_consola.lower() == "e" or data_consola.lower() == "exit") and "Exit" in descrip_command:
                self.endDrawGeometry()

            #se ejecuta si la entrada es una opcion de vistas
            elif current_command == "views" and descrip_command == "[1 2] <1>:":
                
                if data_consola == "" or data_consola == "1":
                    self.view_page_draw.isTwoViewsVisible = False                 
                elif data_consola == "2":
                    self.view_page_draw.isTwoViewsVisible = True                  
                else:
                    return
                self.viewsTwo()
                self.endDrawGeometry() 
                          

            
            #se ejecuta si la entrada es una opcion de zoom
            elif current_command == "zoom" and descrip_command == "[Extents Window] <E>:":
                
                if data_consola == "" or data_consola.lower() == "e":    
                    self.zoomDraw("ZoomExtend")
           
                elif data_consola == "w":
                    self.zoomDraw("ZoomWindow")
                    self.msnConsoleView(["Command","_zoomWindow"])
                    self.msnLabelAndView(["zoom","Window",None])
                    return
                else:
                    return

                self.endDrawGeometry() 

                

            #se ejecuta si la entrada es una opcion de mover
            elif current_command == "move":

                selected_items = len(self.current_project.getSelectedItems())
                
                if  descrip_command == "Seleccione un elemento [Exit]:" and data_consola == "" and selected_items > 0:                                    
                    self.current_project.commandMove({"step":3, "data":None})
                  

                elif descrip_command == "Ingrese el primer punto [Exit]:" and selected_items > 0:
                    
                    point_vertex_ant = self.controller_graphics_draw.getPointVertexAnt()
                    input_point = data_consola.split(",")
                    point  = self.pointFromConsole(input_point, point_vertex_ant)
                    if point == None:
                        return
                    self.current_project.commandMove({"step":4, "data":point})


                    

                elif descrip_command == "Ingrese el segundo punto [Exit]:" and selected_items > 0:
                    point_ant = self.controller_graphics_draw.getPointVertexAnt()
                    input_point = data_consola.split(",")
                    point  = self.pointFromConsole(input_point, point_ant)
                    if point == None:
                        return
                    self.current_project.commandMove({"step":5, "data":[[point_ant.x(),point_ant.y()],
                                                        point]})
                    
                else:
                    return

            #se ejecuta si la entrada es una opcion de copiar
            elif current_command == "copy":                              
                
                selected_items = len(self.current_project.getSelectedItems())                
                point_ant = self.controller_graphics_draw.getPointVertexAnt()
                input_point = data_consola.split(",")
                point  = self.pointFromConsole(input_point, point_ant)

                if  descrip_command == "Seleccione un elemento [Exit]:" and data_consola == "" and selected_items > 0:                                    
                    self.current_project.commandCopy({"step":3, "data":None})

                elif descrip_command == "Ingrese el primer punto [Exit]:" and selected_items > 0:
                    if point == None:
                        return
                    self.current_project.commandCopy({"step":4, "data":point})
             

                elif descrip_command == "Ingrese el segundo punto [Exit]:" and selected_items > 0:
                    if point == None:
                        return
                    self.current_project.commandCopy({"step":5, "data":[[point_ant.x(),point_ant.y()],
                                                        point]})
                    self.view_page_draw.lineEdit_console.setText("")
                    
                else:
                    return
                    
            #se ejecuta si la entrada es una opcion de rotar
            elif current_command == "rotate":

                selected_items = len(self.current_project.getSelectedItems())
                
                if  descrip_command == "Seleccione un elemento [Exit]:" and data_consola == "" and selected_items > 0:                                    
                    self.current_project.commandRotate({"step":3, "data":None})
                  

                elif descrip_command == "Ingrese el punto base [Exit]:" and selected_items > 0:
                    
                    point_vertex_ant = self.controller_graphics_draw.getPointVertexAnt()
                    input_point = data_consola.split(",")
                    point  = self.pointFromConsole(input_point, point_vertex_ant)
                    if point == None:
                        return
                    self.current_project.commandRotate({"step":4, "data":point})
                    

                elif descrip_command == "Ingrese el ángulo [Exit]:" and selected_items > 0:
                    point_ant = self.controller_graphics_draw.getPointVertexAnt() 
                    input_angle = data_consola
   
                    if not isNumber(input_angle):
                        return
                    input_angle = float(input_angle)



                    self.current_project.commandRotate({"step":5, "data":
                                            [[point_ant.x(),point_ant.y()],
                                                        input_angle]
                                        })
                    
                else:
                    return

            #se ejecuta si la entrada es una opcion de borrar
            elif current_command == "erase":

                selected_items = len(self.current_project.getSelectedItems())                
                if  descrip_command == "Seleccione un elemento [Exit]:" and data_consola == "" and selected_items > 0:                                    
                    self.current_project.commandErase({"step":3, "data":None})

            #se ejecuta si la entrada es una opcion de interseccion
            elif current_command == "intersection":
                selected_items = len(self.current_project.getSelectedItems())   
                            
                if  descrip_command == "Seleccione un elemento [Exit]:" and data_consola == "":# and selected_items == 2:                                    
                    self.current_project.commandIntersection({"step":3, "data":None})
                else:
                    self.msnConsoleView(["Error","Selecciona dos líneas"])



            #se ejecuta si la entrada es una opcion de punto
            elif current_command == "point":
                input_point = data_consola.split(",")
                point_ant = self.controller_graphics_draw.getPointVertexAnt()
                point  = self.pointFromConsole(input_point, point_ant)
                point_ant = self.controller_graphics_draw.getPointVertexAnt()
                if point == None:
                    return
                self.current_project.commandPoint({"step":2, "data": point})
                self.view_page_draw.lineEdit_console.setText("")

            #se ejecuta si la entrada es una opcion de linea
            elif current_command == "line":
                input_point = data_consola.split(",")
                point_ant = self.controller_graphics_draw.getPointVertexAnt()
                point  = self.pointFromConsole(input_point, point_ant)
                if point == None:
                    return
                
                if descrip_command == "Ingrese el primer punto [Exit]:" and point_ant == None:
                    if point == None:
                        return
                    self.current_project.commandLine({"step":2, "data":point})
      
                elif descrip_command == "Ingrese el siguiente punto [Exit]:" and point_ant != None:
                    if point == None:
                        return
                    self.current_project.commandLine({"step":3, "data":[[point_ant.x(),point_ant.y()],
                                                        point]})
                                 
                    self.view_page_draw.lineEdit_console.setText("")
                    
                else:
                    return

            else:
                return


        else:
            print("demas opciones")



    def pointFromConsole(self, input, point_prev):
        """
        Esta función toma una entrada `input` de consola, procesa su tipo y devuelve una nueva coordenada `point`
        en función de la entrada y la coordenada anterior `point_prev`.

        Args:
            input (list): una lista que contiene una o más entradas de consola en función del tipo de entrada.
                Puede contener coordenadas, distancias, ángulos, dx-dy, etc.
            point_prev (list): una lista que contiene una coordenada previa que se utilizará como referencia para
                calcular la siguiente coordenada.

        Returns:
            list: una lista que contiene dos valores: `x` e `y`, que representan la nueva coordenada calculada.


        Ejemplos:
            # Calcular una coordenada para una distancia y un ángulo con respecto a una coordenada previa (10, 10).
            >>> pfc = pointFromConsole(["@45", "5"], [10, 10])
            >>> print(pfc)
            [13.535898384862247, 13.535898384862247]

            # Calcular una coordenada para una distancia X y una distancia Y con respecto a una coordenada previa (10, 10).
            >>> pfc = pointFromConsole(["#3", "4"], [10, 10])
            >>> print(pfc)
            [13.0, 14.0]

            # Calcular una coordenada para una sola coordenada.
            >>> pfc = pointFromConsole(["7"], None)
            >>> print(pfc)
            [7.0, 7.0]
        """


        # Si es el primer punto y se recibe un solo valor input=x=y
        
        if len(input) == 1 and point_prev == None:
            x = input[0]
            if isNumber(x):
                x = float(x)
                y = x
            else:
                return None

        # Si es el segundo punto y se recibe un solo valor input=dist
        elif len(input) == 1 and point_prev!= None:
            dist = input[0]
            if isNumber(dist):
                point_vertex = self.controller_graphics_draw.getPointVertex()
                x, y = self.pointInLine(point_prev, point_vertex,float(dist))
                

            else:
                return None
    
        # Si es el segundo punto y se recibe angulo y distancia input=@angulo,dist
        elif len(input) == 2 and input[0][0] == "@" and point_prev!= None:
            angle = input[0][1:]
            dist = input[1]
            if isNumber(angle) and isNumber(dist):
                angle = float(angle)
                dist = float(dist)
                dx = dist * math.cos(math.radians(angle))
                dy = dist * math.sin(math.radians(angle))
                x = point_prev.x() + dx
                y = point_prev.y() + dy                        
            else:
                return None

        # Si es el segundo punto y se recibe distancia X y distancia Y input=#dx,dy
        elif len(input) == 2 and input[0][0] == "#" and point_prev!= None:
            dx = input[0][1:]
            dy = input[1]
            if isNumber(dx) and isNumber(dy):
                x = point_prev.x() + float(dx)
                y = point_prev.y() + float(dy)                        
            else:
                return None
                
        # Si es el segundo punto y se recibe coordenada input=x,y
        elif len(input) == 2:
            x = input[0]
            y = input[1]
            if isNumber(x) and isNumber(y):
                x = float(x)
                y = float(y) 
            else: 
                return None

        # en los demas casos ejem: texto
        else:
            return None

        point=[x,y]
        return point



    def pointInLine(self, p1:QPointF, p2:QPointF, dist_i):
        """
        Devuelve las coordenadas de un punto en la línea que va desde p1 hasta p2,
        a una distancia determinada desde p1.

        Args:
            p1: QPointF. Punto de inicio de la línea.
            p2: QPointF. Punto final de la línea.
            dist_i: float. Distancia desde p1 hasta el punto que se quiere calcular.

        Returns:
            Tuple[float, float]: Coordenadas del punto en la línea, como una tupla de dos floats (x, y).

        Raises:
            ValueError: Si p1 y p2 son el mismo punto o dist_i es menor o igual a cero.

        Example:
            --------
            >>> p1 = QPointF(1, 1)
            >>> p2 = QPointF(5, 5)
            >>> dist_i = 2.89
            >>> self.pointInLine(p1, p2, dist_i)
            (3.00111219075793, 3.00111219075793)

        """
        

        x = None
        y = None
        dx = p2.x() - p1.x()  
        dy = p2.y() - p1.y()
        if dx >= 0: 
            signX = 1
        else:
            signX = -1
        if dy >= 0: 
            signY = 1
        else:
            signY = -1  
        try: 
            theta = math.atan(dx/dy) 
        except ZeroDivisionError:
            theta = math.radians(90)
        
        dxi = abs(dist_i * math.sin(theta)) * signX
        dyi = abs(dist_i * math.cos(theta)) * signY
        x = p1.x() + dxi
        y = p1.y() + dyi

        return (x, y)

    @Slot(list)
    def msnLabelAndView(self,data):  
        """
        tercer dato:
            type_msn=none colocar el msn en consola y view
            type_msn=1 view
        
        """      
        command = data[0]
        input = data[1]
        type_msn=data[2]
        if type_msn == None:
            self.msnConsoleView(["Command","_{}".format(command)])
            self.msnLabelConsole([command, input])
        if type_msn == 1:
            self.msnConsoleView([command,input])
        if type_msn == 2:
            self.msnLabelConsole([command, input])
        if type_msn == 3:
            self.endDrawGeometry()



    @Slot(bool)
    def endDrawGeometry(self, show_msn=True):
        self.controller_graphics_draw.endDrawGeometry()
        self.view_page_draw.endDrawGeometry(show_msn)

    @Slot(bool)
    def endDrawMesh(self, show_msn=True):
        self.controller_menu_mesh.endDrawMesh()





    @Slot(list)
    def msnLabelConsole(self,data):
        command = data[0]
        input = data[1]
        self.view_page_draw.msnLabelConsole(command, input)



    @Slot(list)
    def msnConsoleView(self,data):
        type_msn = data[0]
        msn = data[1]
        self.view_page_draw.msnConsoleView(type_msn, msn)




    @Slot(int)
    def selectLineMesh(self, no_lines):
        selected_objects = self.controller_graphics_draw.getSelectedObjects()
        self.controller_menu_mesh.selectLineMesh(no_lines, selected_objects)


 

    @Slot(bool)
    def deselectDrawGeometry(self, shift_pressed ):
        self.current_project.deselectDrawGeometry(shift_pressed)
        

    @Slot(str)
    def zoomDraw(self,type_zoom):
        self.controller_graphics_draw.zoomDraw(type_zoom)
    
    def settingDraw(self,setting_update):
        self.controller_graphics_draw.settingDraw(setting_update)
    
    def viewsTwo(self):
        self.view_page_draw.viewsTwo()

    def undo(self):   
        """ """
        self.current_project.undo()


    def redo(self):   
        """ """
        self.current_project.redo()

           
    def getView(self):
        return self.view_page_draw
    
    def setCurrentProject(self, model_current_project:ModelProjectCurrent):
        self.current_project = model_current_project
        self.controller_menu_data.setCurrentProject(model_current_project)
        self.controller_menu_mesh.setCurrentProject(model_current_project)
        self.controller_menu_pointMaterial.setCurrentProject(model_current_project)

        self.current_project.signal_msn_label_view.connect(self.msnLabelAndView)
        self.view_page_draw.setUndoStack(self.current_project.getUndoStack())

    
    @Slot(str)
    def selectMenu(self, menu):

        self.view_page_draw.showHideDrawMenu(menu)
       

    @Slot(list)
    def actionMenuSup(self,data):       

        action = data[0]
        value = data[1]

        if action == "ShowHideOrigin":
            self.controller_graphics_draw.modeOriginDraw(value)
        elif action == "ShowHideAxis":
            self.controller_graphics_draw.modeAxisDraw(value)
        elif action == "ShowHideGrid":
            self.controller_graphics_draw.modeGridDraw(value)
        elif action == "ShowHideConsole":
            self.view_page_draw.modeConsoleDraw(value)
        elif action == "ShowHideLabel":
            self.controller_graphics_draw.modeLabelDraw(value)



