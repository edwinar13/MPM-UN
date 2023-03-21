from PySide6.QtCore import*
from PySide6.QtGui import*
from PySide6.QtWidgets import*


class TextItem(QGraphicsItem):

    TYPE = "Text"
    COLOR = QColor("#00ff55")
    HIGT = 10
    WIDTH = 40
    
    def __init__(self, x: float, y: float, width: float, height: float):
        QGraphicsItem.__init__(self)

        self.type = self.TYPE
        self.higt = self.HIGT
        self.width = self.WIDTH
        self.text = "fg"

        self.pen = QPen()



    def setColor(self, color):
        self.color = QColor(color)
        self.pen = QPen(self.color)

    def newPos(self, pos:QPointF|QPoint):
        self.coor = pos
        self.setPos(pos)

    def boundingRect(self):
        h = self.higt
        w = self.width        
        return QRectF(-0.1, -h,
                             w, h+3)

    def paint(self, painter: QPainter, option: 'QStyleOptionGraphicsItem', widget=None):
        painter.setPen(self.pen)
        painter.drawText(QPointF(0, 0), self.text)


algo1 = TextItem(1,1,1,1)
print(algo1)
