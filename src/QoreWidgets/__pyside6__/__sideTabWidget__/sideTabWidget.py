from dataclasses import dataclass

from PySide6.QtWidgets import QTabWidget, QTabBar, QPushButton,QWidget,QStylePainter,QStyleOptionTab,QStyleOptionButton,QStyle
from PySide6.QtCore import QRect,QPropertyAnimation,QEasingCurve,QParallelAnimationGroup,QSize,Qt,Signal,Slot
from PySide6.QtGui import QPainter, QIcon ,QPaintEvent
from ... import rc

@dataclass
class SideTabConfig:
    PADDING = 15
    ICON_SIZE = 30
    MAX_TEXT_WIDTH = 80
    DURATION = 400

    MENU_TEXT="Menu"
    MENU_ICON=QIcon(":/icons/menu")

    @property
    def FOLD_WIDTH(self)->int:
        return self.ICON_SIZE + 2*self.PADDING
    @property
    def EXPAND_WIDTH(self)->int:
        return self.MAX_TEXT_WIDTH + 2*self.PADDING + self.ICON_SIZE + 2*self.PADDING
    
def draw_tab(stConfig:SideTabConfig, icon:QIcon, text:str,painter:QPainter, tabRect:QRect):
    #draw the icon
    iconSize = icon.actualSize(QSize(stConfig.ICON_SIZE, stConfig.ICON_SIZE)) 
    iconRect = QRect(
        tabRect.left() + stConfig.PADDING,
        tabRect.top() + (tabRect.height() - iconSize.height()) // 2, 
        iconSize.width(),
        iconSize.height()
    )
    
    icon.paint(painter, iconRect, Qt.AlignmentFlag.AlignVCenter| Qt.AlignmentFlag.AlignLeft)
    #draw the text
    textRect = QRect(
        iconRect.right() + stConfig.PADDING*2,
        tabRect.top(),  # Adjust the top position as needed
        tabRect.width()- iconRect.width() - 3*stConfig.PADDING,
        tabRect.height()
    )
    painter.drawText(
        textRect,
        Qt.AlignmentFlag.AlignVCenter| Qt.AlignmentFlag.AlignLeft | Qt.TextFlag.TextDontClip,
        text
    )
    
class SideTabBar(QTabBar):

    foldStateChanged=Signal(bool)

    def __init__(self, parent: QWidget | None = ..., stConfig:SideTabConfig=...) -> None:
        super().__init__(parent)
        self.fold=True
        self.stConfig=stConfig
        targetWidth=stConfig.EXPAND_WIDTH if not self.fold else stConfig.FOLD_WIDTH
        self.setMinimumWidth(targetWidth)
        self.setMaximumWidth(targetWidth)

        self.init_animation()

    def init_animation(self):
        self.animation_max = QPropertyAnimation(self, b"maximumWidth")
        self.animation_max.setDuration(SideTabConfig.DURATION)
        self.animation_max.setEasingCurve(QEasingCurve.Type.InOutQuart )
        self.animation_min = QPropertyAnimation(self, b"minimumWidth")
        self.animation_min.setDuration(SideTabConfig.DURATION)

        self.animation_min.setEasingCurve(QEasingCurve.Type.InOutQuart )
        self.animation_group = QParallelAnimationGroup()
        self.animation_group.addAnimation(self.animation_max)
        self.animation_group.addAnimation(self.animation_min)
        
        def on_finished():
            # print('done')
            self.fold=not self.fold
            self.foldStateChanged.emit(self.fold)
            # print(self.fold)
        self.animation_group.finished.connect(on_finished)

    def toggle(self):
        tfold=not self.fold
        start=self.width()
        end=self.stConfig.EXPAND_WIDTH if not tfold else self.stConfig.FOLD_WIDTH
        self.animation_max.setStartValue(start)
        self.animation_max.setEndValue(end)
        self.animation_min.setStartValue(start)
        self.animation_min.setEndValue(end)
        self.animation_group.start()

    def paintEvent(self, event):
        painter = QStylePainter(self)
        option = QStyleOptionTab()
        for index in range(self.count()):
            self.initStyleOption(option, index)
            painter.drawControl(QStyle.ControlElement.CE_TabBarTabShape, option)

            tabRect = self.tabRect(index)
            draw_tab(self.stConfig, self.tabIcon(index), self.tabText(index), painter, tabRect)

    def tabSizeHint(self, index):
        size = QTabBar.tabSizeHint(self, index)
        if size.width() < size.height():
            size.transpose()
        size.setWidth(self.minimumWidth())
        # print(size)
        size.setHeight(size.height() + 2*SideTabConfig.PADDING)
        return size

class MenuButton(QPushButton):
    def __init__(self, parent=None, stConfig:SideTabConfig=...):
        QPushButton.__init__(self, parent)
        self.setFlat(True)
        self.stConfig=stConfig
        self.setIcon(stConfig.MENU_ICON)
        self.setIconSize(QSize(stConfig.ICON_SIZE,stConfig.ICON_SIZE))
        self.setText(stConfig.MENU_TEXT)

    def updatePos(self,parent: QTabWidget):
        tabbar=parent.tabBar()
        if tabbar.count() > 0:
            menuBtnWidth=tabbar.width()
            menuBtnHeight=tabbar.height()/tabbar.count()
        else:
            # print(tabbar.height(),tabbar.width())
            menuBtnWidth=tabbar.width()
            menuBtnHeight=tabbar.height()
        menuBtnBottom=parent.height()
        self.setGeometry(0,menuBtnBottom-menuBtnHeight,menuBtnWidth,menuBtnHeight)

    def paintEvent(self, event: QPaintEvent) -> None:
        painter = QStylePainter(self)
        option = QStyleOptionButton()
        
        self.initStyleOption(option)
        draw_tab(self.stConfig, self.icon(), self.text(), painter, self.rect())
        
        option.icon = QIcon() # clear the icon and text, drawControl should only draw the button shape, else it will draw the icon and text again
        option.text = ""
        painter.drawControl(QStyle.ControlElement.CE_PushButton, option)

class SideTabWidget(QTabWidget):
    '''A TabWidget with horizontal and foldable tabs. Animated.'''
    foldStateChanged=Signal(bool) # pass the fold state from the tabbar to the parent widget

    def __init__(self, parent=None, stConfig:SideTabConfig=SideTabConfig()):
        QTabWidget.__init__(self, parent)
        self.stConfig=stConfig

        self.tabbar=SideTabBar(self,stConfig)
        self.setTabBar(self.tabbar)
        self.tabbar.foldStateChanged.connect(self.exposeFoldState)

        self.menuBtn =MenuButton(self,stConfig)
        self.menuBtn.clicked.connect(self.tabbar.toggle)

    def paintEvent(self, event: QPaintEvent) -> None:
        self.menuBtn.updatePos(self)
        self.tabBar().setMaximumHeight(self.height()-self.menuBtn.height())
        return super().paintEvent(event)
    
    def is_folded(self)->bool:
        return self.tabbar.fold
    
    def set_foldState(self, fold:bool)->None:
        if fold!= self.is_folded():
            self.tabbar.toggle()

    @Slot(bool)
    def exposeFoldState(self, fold:bool):
        self.foldStateChanged.emit(fold)