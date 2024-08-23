from PySide6.QtWidgets import QTabWidget, QTabBar, QPushButton,QWidget,QStylePainter,QStyleOptionTab,QStyle
from PySide6.QtCore import QRect,QPropertyAnimation,QEasingCurve,QParallelAnimationGroup,QSize,Qt,Signal,Slot,QEvent,Property
from PySide6.QtGui import QIcon ,QPaintEvent,QFont

def draw_tab(iconSize:QSize, padding:int, icon:QIcon, text:str,painter:QStylePainter, tabRect:QRect):
    '''
    if icon is null, will draw the first character of the text as icon
    '''
    #draw the icon
    if not icon.isNull():
        iconSize = icon.actualSize(iconSize)
    iconRect = QRect(
        tabRect.left() + padding,
        tabRect.top() + (tabRect.height() - iconSize.height()) // 2, 
        iconSize.width(),
        iconSize.height()
    )
    if not icon.isNull():
        icon.paint(painter, iconRect, Qt.AlignmentFlag.AlignVCenter| Qt.AlignmentFlag.AlignLeft)
    else:
        old_font=painter.font()
        font=QFont()
        font.setPixelSize(iconSize.height()*0.8)
        painter.setFont(font)
        painter.drawText(iconRect, Qt.AlignmentFlag.AlignVCenter| Qt.AlignmentFlag.AlignCenter, text[0].upper())
        painter.setFont(old_font)
    #draw the text
    textRect = QRect(
        iconRect.right() + padding*2,
        tabRect.top(),  # Adjust the top position as needed
        tabRect.width()- iconRect.width() - 3*padding,
        tabRect.height()
    )
    painter.drawText(
        textRect,
        Qt.AlignmentFlag.AlignVCenter| Qt.AlignmentFlag.AlignLeft | Qt.TextFlag.TextDontClip,
        text
    )
    
class SideTabBar(QTabBar):

    foldStateChanged=Signal(bool)

    def __init__(self, parent: "SideTabWidget") -> None:
        super().__init__(parent)
        self.fold=True
        self.targetFold=True
        self.par:SideTabWidget=parent
        self.init_animation()
        self.update_target_width()

    def update_target_width(self):
        targetWidth=self.par.expandWidth if not self.fold else self.par.foldWidth
        
        self.setMinimumWidth(targetWidth)
        self.setMaximumWidth(targetWidth)
        # print(targetWidth)

    def init_animation(self):
        self.animationMax = QPropertyAnimation(self, b"maximumWidth")
        self.animationMax.setDuration(self.par.animateDuration)
        self.animationMax.setEasingCurve(QEasingCurve.Type.InOutQuart )
        self.animationMin = QPropertyAnimation(self, b"minimumWidth")
        self.animationMin.setDuration(self.par.animateDuration)

        self.animationMin.setEasingCurve(QEasingCurve.Type.InOutQuart )
        self.animationGroup = QParallelAnimationGroup()
        self.animationGroup.addAnimation(self.animationMax)
        self.animationGroup.addAnimation(self.animationMin)
        
        def on_finished():
            # print('done')
            self.fold=self.targetFold
            self.foldStateChanged.emit(self.fold)
            # print(self.fold)
        self.animationGroup.finished.connect(on_finished)

    def setFold(self, newFold:bool)->None:
        if newFold == self.targetFold:
            return
        self.targetFold=newFold
        if self.targetFold != self.fold:# animation is running
            self.animationGroup.stop()
        start=self.width()
        end=self.par.expandWidth if not self.targetFold else self.par.foldWidth
        self.animationMax.setStartValue(start)
        self.animationMax.setEndValue(end)
        self.animationMin.setStartValue(start)
        self.animationMin.setEndValue(end)
        self.animationGroup.start()

    def toggle(self):
       self.setFold(not self.fold)

    def paintEvent(self, event):
        painter = QStylePainter(self)
        option = QStyleOptionTab()
        for index in range(self.count()):
            self.initStyleOption(option, index)
            painter.drawControl(QStyle.ControlElement.CE_TabBarTabShape, option)

            tabRect = self.tabRect(index)
            draw_tab(self.iconSize(), self.par.padding, self.tabIcon(index), self.tabText(index), painter, tabRect)

    def tabSizeHint(self, index):
        size = QTabBar.tabSizeHint(self, index)
        if size.width() < size.height():
            size.transpose()
        size.setWidth(self.minimumWidth())
        # print(size)
        size.setHeight(size.height() + 2*self.par.padding)
        return size
    
    def enterEvent(self, event: QEvent) -> None:
        # print('enter')
        if self.par.autoExpand and self.targetFold:
            self.setFold(False)
        return super().enterEvent(event)
    
    def leaveEvent(self, event: QEvent) -> None:
        # print('leave')
        if self.par.autoExpand and not self.targetFold:
            self.setFold(True)
        return super().leaveEvent(event)

class MenuButton(QPushButton):
    def __init__(self, parent:"SideTabWidget"):
        QPushButton.__init__(self, parent)
        self.setFlat(True)
        self.par:SideTabWidget=parent
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
        self.setFixedHeight(menuBtnHeight)
        self.setGeometry(tabbar.x(),menuBtnBottom-menuBtnHeight,menuBtnWidth,menuBtnHeight)
    
class SideTabWidget(QTabWidget):
    '''A TabWidget with horizontal and foldable tabs. Animated.'''

    def __init__(self, parent:QWidget=None):
        super().__init__(parent)
        # init properties
        self._autoExpand=True
        self._padding = 15
        self._maxTextWidth = 80
        self._animateDuration = 400
        self._menuIcon=QIcon(":/icons/menu")
        # init tabbar
        self.tabbar=SideTabBar(self)
        self.setTabBar(self.tabbar)
        self.tabbar.foldStateChanged.connect(self.exposeFoldState)
        self.setTabPosition(QTabWidget.TabPosition.West)
        # init menu button
        self.menuBtn =MenuButton(self)
        self.menuBtn.setIcon(self.menuIcon)

        self.menuBtn.clicked.connect(self.tabbar.toggle)

    #@override
    def setTabPosition(self, position: QTabWidget.TabPosition):
        assert position in [QTabWidget.TabPosition.West, QTabWidget.TabPosition.East], "SideTabWidget only supports horizontal tab position, current position is " + str(self.tabPosition())
        super().setTabPosition(position)
    def paintEvent(self, event: QPaintEvent) -> None:
        self.menuBtn.updatePos(self)
        self.tabBar().setMaximumHeight(self.height()-self.menuBtn.height())
        return super().paintEvent(event)
    
    def isFolded(self)->bool:
        return self.tabbar.fold
    
    def setFolded(self, fold:bool)->None:
        if fold!= self.isFolded():
            self.tabbar.toggle()

    # def leaveEvent(self, event: QEvent) -> None:
    #     # sometimes tabbar cannot trigger the leaveEvent if mouse moves too fast, so we need to check the fold state here as a safeguard
    #     super().leaveEvent(event)
    #     if self.autoExpand and not self.isFolded():
    #         self.setFolded(True)

    #@override
    def setIconSize(self, size:QSize):
        super().setIconSize(size)
        self.menuBtn.setIconSize(size)
        self.tabbar.update_target_width()
    #signal
    foldStateChanged=Signal(bool) # pass the fold state from the tabbar to the parent widget
    @Slot(bool)
    def exposeFoldState(self, fold:bool):
        self.foldStateChanged.emit(fold)

    #property
    folded=Property(bool,fget=isFolded,fset=setFolded,notify=foldStateChanged,doc="fold state of the side tab widget")

    def getAutoExpand(self)->bool:
        return self._autoExpand
    def setAutoExpand(self, value:bool)->None:
        self._autoExpand=value
    autoExpand=Property(bool,fget=getAutoExpand,fset=setAutoExpand,doc="whether to expand the tabs automatically when hovering over the tabbar")

    def getPadding(self)->int:
        return self._padding
    def setPadding(self, value:int)->None:
        self._padding=value
        self.tabbar.update_target_width()
    padding=Property(int,fget=getPadding,fset=setPadding,doc="padding between the icon and text")

    def getMaxTextWidth(self)->int:
        return self._maxTextWidth
    def setMaxTextWidth(self, value:int)->None:
        self._maxTextWidth=value
        self.tabbar.update_target_width()
    maxTextWidth=Property(int,fget=getMaxTextWidth,fset=setMaxTextWidth,doc="maximum width of the text, used to determine the expanded width of the tabbar")

    def getAnimateDuration(self)->int:
        return self._animateDuration
    def setAnimateDuration(self, value:int)->None:
        self._animateDuration=value
        self.tabbar.animationMax.setDuration(value)
        self.tabbar.animationMin.setDuration(value)
    animateDuration=Property(int,fget=getAnimateDuration,fset=setAnimateDuration,doc="duration of the animation when expanding or collapsing the tabbar")

    def getMenuIcon(self)->QIcon:
        return self._menuIcon
    def setMenuIcon(self, value:QIcon)->None:
        self._menuIcon=value
        self.menuBtn.setIcon(value)
    menuIcon=Property(QIcon,fget=getMenuIcon,fset=setMenuIcon,doc="icon of the menu button")

    @property
    def foldWidth(self)->int:
        return self.iconSize().width() + 2*self.padding
    @property
    def expandWidth(self)->int:
        return self.maxTextWidth + 2*self.padding + self.iconSize().width() + 2*self.padding

