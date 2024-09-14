from PySide6.QtWidgets import QWidget,QStylePainter
from PySide6.QtGui import QIcon,QColor,QTransform
from PySide6.QtCore import QRect,QThread,Signal,QTimer

from typing import Callable,Any
class LoadingOverlay(QWidget):
	finished=Signal(Any)
	def __init__(self, parent:QWidget,icon:QIcon=QIcon(":/icons/loading"),iconSize:int=48,fps:int=60,rps:float=1.5,alpha:int=150):
		super().__init__(parent)
		# mask entire parent widget
		self.par:QWidget=parent
		# add self to parent widget
		self.loadingIcon=icon
		self.iconSize=iconSize
		self.alpha=alpha
		# rotate timer
		self.rotateDeg=0
		self.timer=QTimer(self)
		self.timer.setInterval(1000/fps)
		def timeout():
			self.rotateDeg+=rps*360/fps
			# print(self.rotateDeg)
			self.update() # repaint
		self.timer.timeout.connect(timeout)
		self.hide()

	def paintEvent(self, event):
		super().paintEvent(event)
		self.move(0,0)
		self.resize(self.par.size())
		painter = QStylePainter(self)
		color=self.par.palette().color(self.par.backgroundRole())
		color.setAlpha(self.alpha)
		painter.fillRect(self.rect(), color)
		# paint loading icon
		centralPos = self.rect().center()
		transform = QTransform()
		transform.translate(centralPos.x(), centralPos.y())  # Translate to the center of the rect, not the widget
		transform.rotate(self.rotateDeg)
		painter.setTransform(transform)
		self.loadingIcon.paint(painter, QRect(-self.iconSize // 2, -self.iconSize // 2, self.iconSize, self.iconSize))
	
		# sync with parent position and rect
	def stop(self,ret:Any):
		self.timer.stop()
		self.hide()
		self.workerThread.quit()
		self.finished.emit(ret)

	def run(self, func:Callable, *args, **kwargs)->QThread:
		self.timer.start()
		self.show()
		self.raise_()
		# create a new thread to run the function in background
		class WorkerThread(QThread):
			finished=Signal(Any)
			def run(self):
				ret=func(*args, **kwargs)
				self.finished.emit(ret)
		self.workerThread=WorkerThread()
		self.workerThread.finished.connect(self.stop)
		self.workerThread.start()
		return self.workerThread