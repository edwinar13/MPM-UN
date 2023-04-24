""" Este módulo contiene la clase Ui_DialogMsg, mostar mensajes."""
from PySide6.QtCore import (Signal,Qt,QSize)
from PySide6.QtGui import (QColor,QPixmap)
from PySide6.QtWidgets import ( QDialog, QGraphicsDropShadowEffect )
from ui import ui_dialog_msg

class DialogMsg(QDialog, ui_dialog_msg.Ui_DialogMsg):
    """Esta clase crea el QDIalog msg para mostar mensajes. 

    Args:
        type_message (int): Tipo de botones a mostrar (default = 0).
                     0: accept
                     1: cancel/notSave/save
                     2: not/yes
                     3: cancel/accept
        text_title (str): Título del mensaje (default = "").
        text_description (str): Descripción del mensaje (default = "").
        type_icon (int): Tipo de icono a mostrar  (default = 0).
                    0: warning
                    1: question
                    2: ok
                    3: error  
    Attributes:
        button_selected (str): Retorna el botón presionado.
        type_message (str): Tipo de botones a mostrar.
        text_title (str): ítulo del mensaje.
        text_description (str): Descripción del mensaje.
        type_icon (str): Tipo de icono a mostrar.

    Method:
        : setTypeMessage
        : setTextTitle
        : setTextDescription
        : setTypeIcon
        : getButtonSelected

    """    
 
    def __init__(self, parent = None, type_message = 0,text_title = "", text_description = "", type_icon = 0):
        super(DialogMsg, self).__init__(parent)
        self.setupUi(self)
        
        # Atributos
        self.__button_selected = ""
        self.__type_message = type_message
        self.__text_title = text_title
        self.__text_description = text_description
        self.__type_icon = type_icon
        
        # Configura la UI
        self.__configUi()

        # Establece los eventos de la UI
        self.__initEventUi()

    def showEvent(self, event):
        # Llamamos al showEvent de la clase base para asegurarnos de que se ejecuten las operaciones normales
        super().showEvent(event)

        # Anulamos los estilos del botón
        self.pushButton_yes.setStyleSheet('')

    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS CONFIGURAR UI       ::::::::::::::::::::
	###############################################################################
    def __configUi(self):
        """Configura la interface de usuario (ui).""" 

        #Ocultar barra ventana
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        #Sombra de ventana
        self.shadow_card = QGraphicsDropShadowEffect(self)
        self.shadow_card.setBlurRadius(10)
        self.shadow_card.setXOffset(0)
        self.shadow_card.setYOffset(0)
        self.shadow_card.setColor(QColor(0,0,0,100))
        self.frame_content.setGraphicsEffect(self.shadow_card)

        self.shadow_dialog = QGraphicsDropShadowEffect(self)
        self.shadow_dialog.setBlurRadius(15)
        self.shadow_dialog.setXOffset(0)
        self.shadow_dialog.setYOffset(0)
        self.shadow_dialog.setColor(QColor(255,255,255,100))
        self.frame_dialog.setGraphicsEffect(self.shadow_dialog)

        #ocultar botones
        self.pushButton_accept.setVisible(False)
        self.pushButton_cancel.setVisible(False)
        self.pushButton_notSave.setVisible(False)
        self.pushButton_not.setVisible(False)
        self.pushButton_yes.setVisible(False)
        self.pushButton_save.setVisible(False)

        # valores por defecto
        self.setTypeMessage(self.__type_message)
        self.setTextTitle(self.__text_title)
        self.setTextDescription(self.__text_description)
        self.setTypeIcon(self.__type_icon)

    def __initEventUi(self):
        """ Asigna las ranuras (Slot) a las señales (Signal).""" 

        # ::::::::::::::::::::      EVENTOS DRAW MENU DATA     ::::::::::::::::::::
        self.pushButton_accept.clicked.connect(self.__clickedPushButtonAccept)
        self.pushButton_cancel.clicked.connect(self.__clickedPushButtonCancel)
        self.pushButton_notSave.clicked.connect(self.__clickedPushButtonNotSave)
        self.pushButton_not.clicked.connect(self.__clickedPushButtonNot)
        self.pushButton_yes.clicked.connect(self.__clickedPushButtonYes)
        self.pushButton_save.clicked.connect(self.__clickedPushButtonSave)
        self.toolButton_exit.clicked.connect(self.__clickedToolButtonExit)

    ###############################################################################
	# ::::::::::::::::::::           GETTERS Y SETTERS         ::::::::::::::::::::
	###############################################################################
    def setTypeMessage(self, type_message:int):
        """Establece el tipo de mensaje a mostrar.

        Args:
            type_message (int): Tipo de botones a mostrar 
                        0: accept
                        1: cancel/notSave/save
                        2: not/yes
                        3: cancel/accept

        """
        self.__type_message=type_message
        self.___selectTypeMessage(type_message)
    
    def setTextTitle(self, text_title:str):
        """Establece el título del mensaje.

        Args:
            text_title (str): Título del mensaje

        """
        self.__text_title=text_title
        self.label_text.setText(text_title)
    
    def setTextDescription(self, text_description:str):
        """Establece la descripción del mensaje.

        Args:
            text_description (str): Descripción del mensaje 

        """
        self.__text_description=text_description
        self.textBrowser_description.setText(text_description)
    
    def setTypeIcon(self, type_icon:int):
        """Establece el icono a mostrar.

        Args:

            type_icon (int): Tipo de icono a mostrar
                        0: warning
                        1: question
                        2: ok
                        3: error 

        """
        self.__type_icon=type_icon
        self.___showIcon(type_icon)

    def getButtonSelected(self):
        """Obtiene el botón presionado.

        Returns:
            (str): Retorna el nombre del botón presionado

        """
        return self.__button_selected
    
    ###############################################################################
	# ::::::::::::::::::::          MÉTODOS  DE EVENTOS        ::::::::::::::::::::
	###############################################################################
    ''' Métodos para los eventos de los botones '''

    def __clickedPushButtonAccept(self):
        """ Establece como botón deseleccionado accept.""" 
        self.__button_selected = "accept"
        self.accept()

    def __clickedPushButtonCancel(self):
        """ Establece como botón deseleccionado cancel.""" 
        self.__button_selected = "cancel"   
        self.accept()

    def __clickedPushButtonNotSave(self):
        """Establece como botón deseleccionado not save.""" 
        self.__button_selected = "not save"
        self.accept()

    def __clickedPushButtonNot(self):
        """Establece como botón deseleccionado not.""" 
        self.__button_selected = "not"
        self.accept()

    def __clickedPushButtonYes(self):
        """Establece como botón deseleccionado yes.""" 
        self.__button_selected = "yes"
        self.accept()

    def __clickedPushButtonSave(self):
        """Establece como botón deseleccionado exit.""" 
        self.__button_selected = "save"
        self.accept()

    def __clickedToolButtonExit(self):
        """Establece como botón deseleccionado exit.""" 
        self.__button_selected = "exit"
        self.accept()

    def keyPressEvent(self, event):
        """Establece como botón deseleccionado exit cuando se da  en ESC.""" 
        if event.key() == Qt.Key_Escape:
            self.__button_selected = "exit"
            self.accept()
        else:
            pass

    ###############################################################################
	# ::::::::::::::::::::         MÉTODOS  GENERALES         ::::::::::::::::::::
	###############################################################################
    
    def ___hideButton(self):
        """Oculta todos los botones."""                

        self.pushButton_accept.setVisible(False)
        self.pushButton_cancel.setVisible(False)
        self.pushButton_notSave.setVisible(False)
        self.pushButton_not.setVisible(False)
        self.pushButton_yes.setVisible(False)
        self.pushButton_save.setVisible(False)

    
    def ___selectTypeMessage(self, type_message:int):
        """Muetra los botones seleccionados.

        Args:
            type_message (int): Tipo de botones a mostrar 
                        0: accept
                        1: cancel/notSave/save
                        2: not/yes
                        3: cancel/accept

        """
        self.___hideButton()
        if type_message == 0:
            self.pushButton_accept.setVisible(True)            
            self.pushButton_accept.setShortcut("Enter")
            self.pushButton_accept.setFocus()
        elif type_message == 1:
            self.pushButton_cancel.setVisible(True)
            self.pushButton_notSave.setVisible(True)
            self.pushButton_save.setVisible(True)            
            self.pushButton_save.setShortcut("Enter")
            self.pushButton_save.setFocus()
        elif type_message == 2:
            self.pushButton_not.setVisible(True)
            self.pushButton_yes.setVisible(True)            
            self.pushButton_yes.setShortcut("Enter")
            self.pushButton_yes.setFocus()
        elif type_message == 3:
            self.pushButton_cancel.setVisible(True)
            self.pushButton_accept.setVisible(True)            
            self.pushButton_accept.setShortcut("Enter")
            self.pushButton_accept.setFocus()
        else:
            pass
        self.adjustSize()

    def ___showIcon(self,type_icon:int ):
        """Muestra el icono seleccionado.

        Args:

            type_icon (int): Tipo de icono a mostrar
                        0: warning
                        1: question
                        2: ok
                        3: error 

        """
        if type_icon == 0:
            self.label_icon.setPixmap(QPixmap(u"recursos/iconos/iconos_msg/warning.svg"))  
        elif type_icon == 1:
            self.label_icon.setPixmap(QPixmap(u"recursos/iconos/iconos_msg/question.svg"))  
        elif type_icon == 2:
            self.label_icon.setPixmap(QPixmap(u"recursos/iconos/iconos_msg/ok.svg"))  
        elif type_icon == 3:
            self.label_icon.setPixmap(QPixmap(u"recursos/iconos/iconos_msg/error.svg")) 
        else:
            pass
    
    ###############################################################################
	# ::::::::::::::::::::      REIMPLANTACIÓN DE MÉTODOS     ::::::::::::::::::::
	###############################################################################

