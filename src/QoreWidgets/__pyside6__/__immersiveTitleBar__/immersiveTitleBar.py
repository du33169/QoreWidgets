from PySide6.QtGui import QIcon,Qt
from PySide6.QtWidgets import QLabel, QSizePolicy, QHBoxLayout
from PySide6.QtCore import Property
from .immersiveTitleBarContainer import ImmersiveTitleBarContainer

class ImmersiveTitleBar(ImmersiveTitleBarContainer):
	'''Simple immersive title bar with icon and title.'''
	def __init__(self, parent=None):
		super().__init__(parent)
		layout=QHBoxLayout()
		layout.setContentsMargins(0,0,0,0)
		self.setLayout(layout)
		self.init_icon()
		self.init_title()

	def update_icon(self,icon:QIcon):
		self.winIcon.setPixmap(icon.pixmap(self.iconSize,self.iconSize))
	def init_icon(self):
		self.winIcon=QLabel(self)

		self.window().windowIconChanged.connect(self.update_icon)
		self.update_icon(self.window().windowIcon())
		self.layout().addWidget(self.winIcon)

	def init_title(self):
		self.winTitle=QLabel(self)
		self.winTitle.setAlignment(self.titleAlignmentFlag)
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
			rightDistance=self.buttonsReservedWidth
			leftDisatnce=self.winIcon.geometry().right()
			distance=max(rightDistance,leftDisatnce)
			left_margin=distance-leftDisatnce
			right_margin=distance-rightDistance
			self.winTitle.setContentsMargins(left_margin,0,right_margin,0)
	
	def resizeEvent(self,event):
		super().resizeEvent(event)
		self.align_title()

	#@override
	def init_properties(self):
		super().init_properties()
		self._iconSize=24
		self._titleAlignmentFlag:Qt.AlignmentFlag=Qt.AlignmentFlag.AlignCenter|Qt.AlignmentFlag.AlignVCenter

	def getIconSize(self):
		return self._iconSize

	def setIconSize(self,size:int):
		self._iconSize=size
		self.update_icon(self.window().windowIcon())

	def getTitleAlignmentFlag(self):
		return self._titleAlignmentFlag

	def setTitleAlignmentFlag(self,flag:Qt.AlignmentFlag):
		self._titleAlignmentFlag=flag
		self.winTitle.setAlignment(flag)
		self.align_title()

	iconSize=Property(int,getIconSize,setIconSize,doc="Icon size of the title bar.")
	titleAlignmentFlag=Property(Qt.AlignmentFlag,getTitleAlignmentFlag,setTitleAlignmentFlag,doc="Alignment flag of the title.")