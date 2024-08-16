from dataclasses import dataclass
from enum import Enum
from PySide6.QtGui import QMouseEvent, QColor,QResizeEvent,QWindowStateChangeEvent
from PySide6.QtWidgets import QMainWindow, QWidget,QGraphicsDropShadowEffect
from PySide6.QtCore import Qt,QPoint

@dataclass
class FramelessWindowConfig:
    GRIP_WIDTH: int = 8
    SHADOW: bool = True
    # GRIP_COLOR: QColor = field(default_factory=lambda: QColor(0,0,0,0))

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
    def __init__(self, parent:QWidget,gripPos:GripPos,flConfig:FramelessWindowConfig):
        super().__init__(parent)
        self.gripPos=gripPos
        self.flConfig=flConfig
        self.raise_()
        self.setCursor(self.gripPos.cursorShape)
        self.resizing=False

    # def paintEvent(self, event: QPaintEvent) -> None:
    #     painter=QStylePainter(self)
    #     painter.fillRect(self.rect(),self.flConfig.GRIP_COLOR)
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
            self.setFixedWidth(self.flConfig.GRIP_WIDTH)
            self.setFixedHeight(parent.height()-4*self.flConfig.GRIP_WIDTH+1)
        elif self.gripPos.is_horizontal_line:
            self.setFixedWidth(parent.width()-4*self.flConfig.GRIP_WIDTH+1)
            self.setFixedHeight(self.flConfig.GRIP_WIDTH)
        else:# corner
            self.setFixedWidth(self.flConfig.GRIP_WIDTH*2)
            self.setFixedHeight(self.flConfig.GRIP_WIDTH*2)

    def follow_geometry(self):
        parent:QWidget=self.parent()
        self.update_size()
        parCenterPoint=parent.rect().center()
        ux,uy=self.gripPos.unitVec
        ux=-1 if ux==0 else ux # for TOP,BOTTOM
        uy=-1 if uy==0 else uy # for LEFT,RIGHT
        tx=parCenterPoint.x()+ux*(parent.width()//2) - (self.width()-1 if ux==1 else 0) +(2*self.flConfig.GRIP_WIDTH if self.gripPos.is_horizontal_line else 0)
        ty=parCenterPoint.y()+uy*(parent.height()//2) - (self.height()-1 if uy==1 else 0) +(2*self.flConfig.GRIP_WIDTH if self.gripPos.is_vertical_line else 0)
        self.move(tx,ty)
        self.raise_()

class FramelessWindow(QMainWindow):
    '''Frameless Window with resize grips'''
    def __init__(self, parent=None,flConfig:FramelessWindowConfig=FramelessWindowConfig()):
        super(FramelessWindow, self).__init__(parent)
        self.flConfig=flConfig

        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        # self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        # self.setAttribute(Qt.WidgetAttribute.WA_NoSystemBackground)
        self.init_grips()
        self.init_shadow()

    def init_grips(self):
        self.pos2grip:dict[GripPos,ResizeGrip]={}
        for gripPos in GripPos:
            grip=ResizeGrip(self,gripPos,self.flConfig)
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
    
    def init_shadow(self):
        if self.flConfig.SHADOW:      # DROP SHADOW
            self.shadowWidget = QWidget(self)
            # self.shadowWidget.setGeometry(100,100,100,100)
            self.setCentralWidget(self.shadowWidget)
            # self.layout().setParent(self.shadowWidget)
            self.shadowWidget.show()
            self.shadowWidget.raise_()
            
            self.shadowWidget.setStyleSheet("background-color: rgba(0, 0, 0, 150);")
            self.shadow = QGraphicsDropShadowEffect(self)
            self.shadow.setBlurRadius(17)
            self.shadow.setXOffset(0)
            self.shadow.setYOffset(0)
            self.shadow.setColor(QColor(0, 0, 0, 150))
            # move self.layout to self.shadowWidget
            
            self.shadowWidget.setGraphicsEffect(self.shadow)