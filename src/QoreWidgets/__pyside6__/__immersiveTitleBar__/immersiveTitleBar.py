from dataclasses import dataclass
from PySide6.QtGui import QIcon,Qt
from PySide6.QtWidgets import QLabel, QSizePolicy, QHBoxLayout

from .immersiveTitleBarContainer import ImmersiveTitleBarContainer,ImmersiveTitleBarContainerConfig

@dataclass
class ImmersiveTitleBarConfig(ImmersiveTitleBarContainerConfig):
	ICON_SIZE=24
	TITLE_TEXT_ALIGN_FLAG:Qt.AlignmentFlag=Qt.AlignmentFlag.AlignCenter|Qt.AlignmentFlag.AlignVCenter

class ImmersiveTitleBar(ImmersiveTitleBarContainer):
	'''Simple immersive title bar with icon and title.'''
	def __init__(self, parent=None,itbconfig:ImmersiveTitleBarConfig=ImmersiveTitleBarConfig()):
		super().__init__(parent,itbconfig)
		self.itbconfig=itbconfig
		layout=QHBoxLayout()
		layout.setContentsMargins(0,0,0,0)
		self.setLayout(layout)
		self.init_icon()
		self.init_title()

	def init_icon(self):
		self.winIcon=QLabel(self)
		def update_icon(icon:QIcon):
			self.winIcon.setPixmap(icon.pixmap(self.itbconfig.ICON_SIZE,self.itbconfig.ICON_SIZE))

		self.window().windowIconChanged.connect(update_icon)
		update_icon(self.window().windowIcon())
		self.layout().addWidget(self.winIcon)

	def init_title(self):
		self.winTitle=QLabel(self)
		self.winTitle.setAlignment(self.itbconfig.TITLE_TEXT_ALIGN_FLAG)
		# set expanding
		self.winTitle.setSizePolicy(QSizePolicy.Policy.Expanding,QSizePolicy.Policy.Expanding)
		
		def update_title(title:str):
			self.winTitle.setText(title)

		self.window().windowTitleChanged.connect(update_title)
		update_title(self.window().windowTitle())
		self.layout().addWidget(self.winTitle)
		self.align_title()

	def align_title(self):
		if self.winTitle.alignment() & Qt.AlignmentFlag.AlignCenter == Qt.AlignmentFlag.AlignCenter: # cannot use "!=0"
			rightDistance=self.itbconfig.BUTTONS_RESERVED_WIDTH
			leftDisatnce=self.winIcon.geometry().right()
			distance=max(rightDistance,leftDisatnce)
			left_margin=distance-leftDisatnce
			right_margin=distance-rightDistance
			self.winTitle.setContentsMargins(left_margin,0,right_margin,0)
	
	def resizeEvent(self,event):
		super().resizeEvent(event)
		self.align_title()