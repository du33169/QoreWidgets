from PySide6.QtWidgets import QWidget,QStylePainter,QAbstractItemView,QLabel
from PySide6.QtGui import QIcon
from PySide6.QtCore import QRect,Signal,Qt

from typing import Any

class EmptyOverlay(QWidget):
	finished=Signal(Any)
	def __init__(self, parent:QWidget,icon:QIcon=QIcon(":/icons/empty"),iconSize:int=48,text:str|QLabel="Empty"):
		super().__init__(parent)
		# mask entire parent widget
		self.par:QWidget=parent
		# add self to parent widget
		self.emptyIcon=icon
		self.iconSize=iconSize
		self.bind_parent(parent)
		self.textLabel=QLabel(text,self) if isinstance(text,str) else text
		self.textLabel.setParent(self)
		self.textLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
		if isinstance(text,str):
			# set font color to #5f6368
			self.textLabel.setStyleSheet("color:#5f6368;")
	def paintEvent(self, event):
		super().paintEvent(event)
		self.move(0,0)
		self.resize(self.par.size())
		painter = QStylePainter(self)
		centralPos = self.rect().center()
		self.emptyIcon.paint(painter, QRect(centralPos.x() - self.iconSize // 2, centralPos.y() - self.iconSize // 2, self.iconSize, self.iconSize))
		self.textLabel.move(centralPos.x() - self.textLabel.width() // 2, centralPos.y() + self.iconSize // 2 + self.textLabel.height() // 2)
	def bind_parent(self,parent:QWidget):
		assert isinstance(parent,QAbstractItemView),f"parent must be a QAbstractItemView, current parent is {type(parent)}"
		assert parent.model() is not None,"please bind empty overlay after model is set"
		def update_empty_overlay_state():
			if parent.model() is None or parent.model().rowCount() == 0:
				self.show()
			else:
				self.hide()
		update_empty_overlay_state()
		parent.model().rowsInserted.connect(update_empty_overlay_state)
		parent.model().rowsRemoved.connect(update_empty_overlay_state)
		parent.model().modelReset.connect(update_empty_overlay_state)
		