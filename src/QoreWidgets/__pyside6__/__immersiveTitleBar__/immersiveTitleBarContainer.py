from PySide6.QtWidgets import QWidget,QPushButton
from PySide6.QtGui import QIcon, QPaintEvent,QMouseEvent,QWindowStateChangeEvent
from PySide6.QtCore import QSize,Qt,QRect,Property

class ImmersiveTitleBarButton(QPushButton):
	def __init__(self, parent:"ImmersiveTitleBarContainer",index:int):
		'''index: 0 for close, 1 for maximize, 2 for minimize'''
		super().__init__(parent)

		self.setIconSize(QSize(parent.buttonIconSize, parent.buttonIconSize))
		self.setFixedSize(parent.buttonSize, parent.buttonSize)
		self.setFlat(parent.flatButton)
		self.index=index

	def update_pos(self):
		parent:ImmersiveTitleBarContainer=self.parent()
		x,y=parent.get_button_offset(self.index)
		self.move(parent.width()-x,y)

class ImmersiveTitleBarContainer(QWidget):
	'''Immersive Title Bar Container with only close, maximize, minimize buttons. The rest area is an empty layout for developer to add custom widgets.'''
	def __init__(self, parent=None):
		super().__init__(parent)
		self.init_properties()		
		self.dragging=False
		self.setFixedHeight(self.titleBarHeight)
		self.init_btns()

	def maximize_icon_toggle(self, event: QWindowStateChangeEvent) -> None:
		if event.type() == QWindowStateChangeEvent.Type.WindowStateChange:
			win=self.window()
			if win.isMaximized():
				self.maximizeButton.setIcon(self.restoreIcon)
			else:
				self.maximizeButton.setIcon(self.maximizeIcon)
		
	def on_maximize_clicked(self):
		win=self.window()
		if win.isMaximized():
			win.showNormal()
		else:
			win.showMaximized()

	def init_btns(self):
		# create buttons
		self.closeButton = ImmersiveTitleBarButton(self,  0)
		self.closeButton.setIcon(self.closeIcon)

		self.maximizeButton = ImmersiveTitleBarButton(self,  1)
		self.maximizeButton.setIcon(self.maximizeIcon)

		self.minimizeButton = ImmersiveTitleBarButton(self,  2)		
		self.minimizeButton.setIcon(self.minimizeIcon)
		self.btns=[self.closeButton,self.maximizeButton,self.minimizeButton]

		# bind button to window events
		self.closeButton.clicked.connect(self.window().close)
		
		self.maximizeButton.clicked.connect(self.on_maximize_clicked)
		self.minimizeButton.clicked.connect(self.window().showMinimized)
		
		old_hook=self.window().changeEvent
		def window_state_changed_wrapper(event: QWindowStateChangeEvent) -> None:
			old_hook(event)
			self.maximize_icon_toggle(event)
		self.window().changeEvent=window_state_changed_wrapper
	#[end init_btns]
 
	def paintEvent(self, event: QPaintEvent) -> None:
		[btn.update_pos() for btn in self.btns]

		# layout auto adjust to reserve space for buttons
		if self.layout():
			# Adjust the layout to fit within the available space minus the reserved area
			available_width = self.width() - self.buttonsReservedWidth
			# Resize the layout's geometry to the available width
			self.layout().setGeometry(QRect(0, 0, available_width, self.height())) 
		return super().paintEvent(event)
	
	# double click to maximize window
	def mouseDoubleClickEvent(self, event: QMouseEvent) -> None:
		if event.button() == Qt.MouseButton.LeftButton:
			self.on_maximize_clicked()
		return super().mouseDoubleClickEvent(event)

	# handle window drag
	def mousePressEvent(self, event: QMouseEvent) -> None:
		# check event target
		if event.buttons() == Qt.MouseButton.LeftButton:
			self.dragPos = event.globalPos()
			self.dragging=True
		return super().mousePressEvent(event)
	
	def mouseReleaseEvent(self, event: QMouseEvent) -> None:
		self.dragging=False
		return super().mouseReleaseEvent(event)

	def mouseMoveEvent(self, event: QMouseEvent) -> None:
		if event.buttons() == Qt.MouseButton.LeftButton and self.dragging:
			win=self.window()
			if win.isMaximized(): # handle drag window off from maximized state
				leftDistance=event.globalX()
				screenWidth=win.screen().geometry().width()
				winNormalWidth=win.normalGeometry().width()
				rightDistance=screenWidth-leftDistance

				win.showNormal() # ** must be place after get normal width and before move **

				if leftDistance<rightDistance:
					win.move(max(0,event.globalX()-leftDistance),win.y())
				else:
					win.move(screenWidth-winNormalWidth,win.y())
				
			win.move(win.pos() + event.globalPos() - self.dragPos)
			self.dragPos = event.globalPos()
		return super().mouseMoveEvent(event)

	#properties
	def init_properties(self):
		self._titleBarHeight: int = 32
		self._flatButton: bool = False
		self._buttonSize: int = 24
		self._buttonIconSize: int = 20
		self._buttonSpacing: int = 4
		self._buttonMargin: int = 4
		self._closeIcon:	QIcon = QIcon(":/icons/close")
		self._maximizeIcon: QIcon = QIcon(":/icons/maximize")
		self._restoreIcon: QIcon = QIcon(":/icons/restore")
		self._minimizeIcon: QIcon = QIcon(":/icons/minimize")

	def setTitleBarHeight(self, height: int) -> None:
		self._titleBarHeight = height
		self.setFixedHeight(height)
	def getTitleBarHeight(self) -> int:
		return self._titleBarHeight
	def setFlatButton(self, flat: bool) -> None:
		self._flatButton = flat
		[btn.setFlat(flat) for btn in self.btns]
	def getFlatButton(self) -> bool:
		return self._flatButton
	def setButtonSize(self, size: int) -> None:
		self._buttonSize = size
		[btn.setFixedSize(size, size) for btn in self.btns]
	def getButtonSize(self) -> int:
		return self._buttonSize
	def setButtonIconSize(self, size: int) -> None:
		self._buttonIconSize = size
		[btn.setIconSize(QSize(size, size)) for btn in self.btns]
	def getButtonIconSize(self) -> int:
		return self._buttonIconSize
	def setButtonSpacing(self, spacing: int) -> None:
		self._buttonSpacing = spacing
	def getButtonSpacing(self) -> int:
		return self._buttonSpacing
	def setButtonMargin(self, margin: int) -> None:
		self._buttonMargin = margin
	def getButtonMargin(self) -> int:
		return self._buttonMargin
	def setCloseIcon(self, icon: QIcon) -> None:
		self._closeIcon = icon
		self.closeButton.setIcon(icon)
	def getCloseIcon(self) -> QIcon:
		return self._closeIcon
	def setMaximizeIcon(self, icon: QIcon) -> None:
		self._maximizeIcon = icon
		if not self.window().isMaximized():
			self.maximizeButton.setIcon(icon)
	def getMaximizeIcon(self) -> QIcon:
		return self._maximizeIcon
	def setRestoreIcon(self, icon: QIcon) -> None:
		self._restoreIcon = icon
		if self.window().isMaximized():
			self.maximizeButton.setIcon(icon)
	def getRestoreIcon(self) -> QIcon:
		return self._restoreIcon
	def setMinimizeIcon(self, icon: QIcon) -> None:
		self._minimizeIcon = icon
		self.minimizeButton.setIcon(icon)
	def getMinimizeIcon(self) -> QIcon:
		return self._minimizeIcon

	titleBarHeight=Property(int, getTitleBarHeight, setTitleBarHeight, doc="The height of the title bar.")
	flatButton=Property(bool, getFlatButton, setFlatButton, doc="Whether the buttons are flat or not.")
	buttonSize=Property(int, getButtonSize, setButtonSize, doc="The size of the buttons.")
	buttonIconSize=Property(int, getButtonIconSize, setButtonIconSize, doc="The size of the buttons' icons.")
	buttonSpacing=Property(int, getButtonSpacing, setButtonSpacing, doc="The spacing between the buttons.")
	buttonMargin=Property(int, getButtonMargin, setButtonMargin, doc="The margin between the edge of the title bar and the buttons.")
	closeIcon=Property(QIcon, getCloseIcon, setCloseIcon, doc="The icon for the close button.")
	maximizeIcon=Property(QIcon, getMaximizeIcon, setMaximizeIcon, doc="The icon for the maximize button.")
	restoreIcon=Property(QIcon, getRestoreIcon, setRestoreIcon, doc="The icon for the restore button.")
	minimizeIcon=Property(QIcon, getMinimizeIcon, setMinimizeIcon, doc="The icon for the minimize button.")

	def get_button_offset(self, index: int) -> tuple[int, int]:
		x =  (self.buttonSize + self.buttonSpacing) * (index+1) + self.buttonMargin
		y = (self.height() - self.buttonSize) // 2
		return (x, y)

	@property
	def buttonsReservedWidth(self):
		return (self.buttonSize + self.buttonSpacing) * 3 + self.buttonMargin*2