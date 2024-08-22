from enum import Enum
from PySide6.QtGui import QMouseEvent, QResizeEvent,QWindowStateChangeEvent
from PySide6.QtWidgets import QMainWindow, QWidget
from PySide6.QtCore import Qt,QPoint,Property

_N_=1000 # weight of x
def unit2id(ux,uy)->int:
    return (ux+1)*_N_+(uy+1)

def id2unit(id:int)->tuple[int,int]:
    return (id//_N_-1,id%_N_-1)

class GripPos(Enum):
                                    ## +-----------------------------------+
                                    ## | TOP_LEFT   | TOP     | TOP_RIGHT  |  
    TOP_LEFT     = unit2id(-1,-1)   ## |    -1,-1   |  0,-1   |    1,-1    |  
    TOP          = unit2id( 0,-1)   ## |------------+---------+------------|      axis:   o---> x
    TOP_RIGHT    = unit2id( 1,-1)   ## | LEFT       |         | RIGHT      |              |
    RIGHT        = unit2id( 1, 0)   ## |   -1, 0    |  0, 0   |    1, 0    |              v       
    BOTTOM_RIGHT = unit2id( 1, 1)   ## |------------+---------+------------|              y   
    BOTTOM       = unit2id( 0, 1)   ## | BOTTOM_LEFT|BOTTOM   |BOTTOM_RIGHT|    
    BOTTOM_LEFT  = unit2id(-1, 1)   ## |    -1, 1   |  0, 1   |    1, 1    |    
    LEFT         = unit2id(-1, 0)   ## +-----------------------------------+    

    @property
    def is_vertical_line(self)->bool:
        return self in [GripPos.LEFT,GripPos.RIGHT]
    @property
    def is_horizontal_line(self)->bool:
        return self in [GripPos.TOP,GripPos.BOTTOM]
    @property
    def is_corner(self)->bool:
        return self in [GripPos.TOP_LEFT,GripPos.TOP_RIGHT,GripPos.BOTTOM_LEFT,GripPos.BOTTOM_RIGHT]

    @property
    def unitVec(self)->tuple[int,int]:
        return id2unit(self.value)
    
    @classmethod
    def vec2unit(cls,x:int,y:int)->tuple[int,int]:
        return 0 if x==0 else x//abs(x) , 0 if y==0 else y//abs(y)
    
    @classmethod    
    def vec2pos(cls,x:int,y:int)->"GripPos":
        ux,uy=cls.vec2unit(x,y)
        return GripPos(unit2id(ux,uy))

    @property
    def cursorShape(self)->Qt.CursorShape:
        match self:
            case GripPos.TOP_LEFT | GripPos.BOTTOM_RIGHT:
                return Qt.CursorShape.SizeFDiagCursor
            case GripPos.TOP_RIGHT | GripPos.BOTTOM_LEFT:
                return Qt.CursorShape.SizeBDiagCursor
            case GripPos.TOP | GripPos.BOTTOM:
                return Qt.CursorShape.SizeVerCursor
            case GripPos.LEFT | GripPos.RIGHT:
                return Qt.CursorShape.SizeHorCursor
    #[end cursorShape]
#[end GripPos]

class ResizeGrip(QWidget):
    def __init__(self, parent:QWidget,gripPos:GripPos):
        super().__init__(parent)
        self.gripPos=gripPos
        self.par:FramelessWindow=parent
        self.raise_()
        self.setCursor(self.gripPos.cursorShape)
        self.resizing=False

    # uncomment to visualize resize grip, for debug
    # def paintEvent(self, event) -> None:
    #     from PySide6.QtGui import QColor
    #     from PySide6.QtWidgets import QStylePainter
    #     painter=QStylePainter(self)
    #     painter.fillRect(self.rect(),QColor(255,0,0,100))
    #     super().paintEvent(event)

    def mousePressEvent(self, event: QMouseEvent) -> None: # start resize
        if event.buttons() == Qt.MouseButton.LeftButton:
            self.resizing=True
        return super().mousePressEvent(event)
    def mouseReleaseEvent(self, event: QMouseEvent) -> None: # end resize
        if event.buttons() == Qt.MouseButton.LeftButton:
            self.resizing=False
        return super().mouseReleaseEvent(event)
    def mouseMoveEvent(self, event: QMouseEvent) -> None: # resize parent
        if event.buttons()==Qt.MouseButton.LeftButton and self.resizing:
            parent:QWidget=self.parent()
            event_delta = event.pos()
            ux,uy=self.gripPos.unitVec
            size_delta=QPoint(event_delta.x()*ux,event_delta.y()*uy)
            newWidth=max(parent.minimumWidth(),parent.width()+size_delta.x())
            newHeight=max(parent.minimumHeight(),parent.height()+size_delta.y())
            newTop=parent.pos().y()+event_delta.y() if uy==-1 and newHeight!=parent.height() else parent.pos().y()
            newLeft=parent.pos().x()+event_delta.x() if ux==-1 and newWidth!=parent.width() else parent.pos().x()
            parent.setGeometry(newLeft,newTop,newWidth,newHeight)
            event.accept()
        return super().mouseMoveEvent(event)
    
    def update_size(self):
        parent:QWidget=self.parent()
        if self.gripPos.is_vertical_line:
            self.setFixedWidth(self.par.gripWidth)
            self.setFixedHeight(parent.height()-2*self.par.gripWidth)
        elif self.gripPos.is_horizontal_line:
            self.setFixedWidth(parent.width()-2*self.par.gripWidth)
            self.setFixedHeight(self.par.gripWidth)
        else:# corner
            self.setFixedWidth(self.par.gripWidth)
            self.setFixedHeight(self.par.gripWidth)

    def follow_geometry(self):
        parent:QWidget=self.parent()
        self.update_size()
        ux,uy=self.gripPos.unitVec
        txMap={-1:0, 0: self.par.gripWidth, 1: parent.width()-self.par.gripWidth}
        tyMap={-1:0, 0: self.par.gripWidth, 1: parent.height()-self.par.gripWidth}
        tx=txMap[ux]
        ty=tyMap[uy]
        self.move(tx,ty)
        self.raise_()

class FramelessWindow(QMainWindow):
    '''Frameless Window with resize grips'''
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_properties()
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        # self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        # self.setAttribute(Qt.WidgetAttribute.WA_NoSystemBackground)
        self.init_grips()

    def init_grips(self):
        self.pos2grip:dict[GripPos,ResizeGrip]={}
        for gripPos in GripPos:
            grip=ResizeGrip(self,gripPos)
            self.pos2grip[gripPos]=grip
            grip.show()
            grip.follow_geometry()

    def changeEvent(self, event: QWindowStateChangeEvent) -> None:
        if event.type() == QWindowStateChangeEvent.Type.WindowStateChange:
            if self.isMaximized():
                [grip.hide() for grip in self.pos2grip.values()]
            else:
                [grip.show() for grip in self.pos2grip.values()]
        return super().changeEvent(event)
    def resizeEvent(self, event: QResizeEvent) -> None:
        super().resizeEvent(event)
        [grip.follow_geometry() for grip in self.pos2grip.values()]

    def init_properties(self):
        self._gripWidth=6

    def get_gripWidth(self)->int:
        return self._gripWidth
    def set_gripWidth(self,value:int)->None:
        self._gripWidth=value
        [grip.update_size() for grip in self.pos2grip.values()]

    gripWidth=Property(int,get_gripWidth,set_gripWidth,doc="Width of resize grips")