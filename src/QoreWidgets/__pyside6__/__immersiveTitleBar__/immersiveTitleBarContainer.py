from PySide6.QtWidgets import QWidget,QPushButton
from PySide6.QtGui import QIcon, QPaintEvent,QMouseEvent,QWindowStateChangeEvent
from PySide6.QtCore import QSize,Qt,QRect
from dataclasses import dataclass

@dataclass
class ImmersiveTitleBarContainerConfig:
	#title bar config
	HEIGHT: int = 32
	FLAT_BUTTON: bool = False
	#button config
	BUTTON_SIZE: int = 24
	BUTTON_ICON_SIZE: int = 20
	BUTTON_SPACING: int = 4
	BUTTONS_MARGIN: int = 4
	CLOSE_BUTTON_ICON:	QIcon = QIcon(":/icons/close")
	MAXIMIZE_BUTTON_ICON: QIcon = QIcon(":/icons/maximize")
	RESTORE_BUTTON_ICON: QIcon = QIcon(":/icons/restore")
	MINIMIZE_BUTTON_ICON: QIcon = QIcon(":/icons/minimize")

	def get_button_offset(self, index: int) -> tuple[int, int]:
		x =  (self.BUTTON_SIZE + self.BUTTON_SPACING) * (index+1) + self.BUTTONS_MARGIN
		y = (self.HEIGHT - self.BUTTON_SIZE) // 2
		return (x, y)

	@property
	def BUTTONS_RESERVED_WIDTH(self):
		return (self.BUTTON_SIZE + self.BUTTON_SPACING) * 3 + self.BUTTONS_MARGIN*2

class ImmersiveTitleBarButton(QPushButton):
	def __init__(self, parent:QWidget,itbconfig:ImmersiveTitleBarContainerConfig,index:int):
		'''index: 0 for close, 1 for maximize, 2 for minimize'''
		super().__init__(parent)
		self.setIconSize(QSize(itbconfig.BUTTON_ICON_SIZE, itbconfig.BUTTON_ICON_SIZE))
		self.setFixedSize(itbconfig.BUTTON_SIZE, itbconfig.BUTTON_SIZE)
		self.setFlat(itbconfig.FLAT_BUTTON)
		self.index=index
		self.itbconfig=itbconfig
	def update_pos(self):
		parent:QWidget=self.parent()
		x,y=self.itbconfig.get_button_offset(self.index)
		self.move(parent.width()-x,y)

class ImmersiveTitleBarContainer(QWidget):
	'''Immersive Title Bar Container with only close, maximize, minimize buttons. The rest area is an empty layout for developer to add custom widgets.'''
	def __init__(self, parent=None,itbconfig:ImmersiveTitleBarContainerConfig=ImmersiveTitleBarContainerConfig()):
		super().__init__(parent)
		self.setFixedHeight(itbconfig.HEIGHT)
		self.itbconfig=itbconfig
		self.dragging=False
		self.init_btns()

	def maximize_icon_toggle(self, event: QWindowStateChangeEvent) -> None:
		if event.type() == QWindowStateChangeEvent.Type.WindowStateChange:
			win=self.window()
			if win.isMaximized():
				self.maximizeButton.setIcon(self.itbconfig.RESTORE_BUTTON_ICON)
			else:
				self.maximizeButton.setIcon(self.itbconfig.MAXIMIZE_BUTTON_ICON)
		
	def on_maximize_clicked(self):
		win=self.window()
		if win.isMaximized():
			win.showNormal()
		else:
			win.showMaximized()

	def init_btns(self):
		# create buttons
		self.closeButton = ImmersiveTitleBarButton(self, self.itbconfig, 0)
		self.closeButton.setIcon(self.itbconfig.CLOSE_BUTTON_ICON)

		self.maximizeButton = ImmersiveTitleBarButton(self, self.itbconfig, 1)
		self.maximizeButton.setIcon(self.itbconfig.MAXIMIZE_BUTTON_ICON)

		self.minimizeButton = ImmersiveTitleBarButton(self, self.itbconfig, 2)		
		self.minimizeButton.setIcon(self.itbconfig.MINIMIZE_BUTTON_ICON)
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
			available_width = self.width() - self.itbconfig.BUTTONS_RESERVED_WIDTH
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


