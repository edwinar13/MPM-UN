
""" Este módulo contiene controlador de la vista pagina home """
from PySide6.QtCore import ( QFile, Slot)
from clases.Vista.view_PageDraw import  ViewPageDraw
from clases.Modelo.model_Projects import ModelProject
import typing

 
class ControllerPageDraw():

    def __init__(self, controller_main) -> None:    

        self.controller_main = controller_main 
        self.controller_card_projects = []

        #Crea la vista MainWindow
        self.view_page_draw = ViewPageDraw()
       

    def getView(self):
        return self.view_page_draw
  