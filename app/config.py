import os

from PySide6.QtCore import QObject, QSettings, Signal

# Carpeta app/resources, sin depender del directorio desde el que se ejecute la app
RESOURCES_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "resources")

class ConfigManager(QObject):
    signalThemeChanged = Signal(str)

    _instance = None  # Variable de clase para almacenar la instancia única

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.init_manager()
        return cls._instance

    def init_manager(self):
        # Inicializa un objeto QSettings para almacenar las configuraciones de la aplicación
        self.settings = QSettings("UNAL", "MPM-UN app")

        # Obtén el valor actual del tema o establece un valor predeterminado si no existe
        self.currentTheme = self.settings.value("theme", "light")

    def setTheme(self, theme):
        # Establece el tema y guarda la configuración
        if theme != self.currentTheme:
            self.currentTheme = theme
            self.settings.setValue("theme", theme)
            self.signalThemeChanged.emit(theme)

    def getTheme(self):
        # Retorna el tema actual
        return self.currentTheme
    
config_manager = ConfigManager()