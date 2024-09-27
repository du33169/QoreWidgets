from PySide6.QtWidgets import QWidget,QStylePainter
from PySide6.QtGui import QIcon,QTransform
from PySide6.QtCore import QRect,QThread,Signal,Property, QPropertyAnimation,Qt

from typing import Callable,Any

class LoadingOverlay(QWidget):
	finished=Signal(Any)
	def __init__(self, parent:QWidget,icon:QIcon=QIcon(":/icons/loading"),iconSize:int=48,rps:float=1.5,alpha:int=150):
		super().__init__(parent)
		# mask entire parent widget
		self.par:QWidget=parent
		# add self to parent widget
		self.loadingIcon=icon
		self.iconSize=iconSize
		self.rps=rps
		self.alpha=alpha
		self._angle=0
		self.workerThread=None
		self.init_animation()
		self.hide()

	@Property(int)
	def angle(self):
		return self._angle
	@angle.setter
	def angle(self, value):
		self._angle=value
		self.update()

	def init_animation(self):
		# setup animation
		self.animation = QPropertyAnimation(self, b'angle')
		self.animation.setStartValue(0)
		self.animation.setEndValue(360)
		self.animation.setDuration(1/self.rps*1000)  # 2 seconds for a full rotation
		self.animation.setLoopCount(-1)   # Loop indefinitely
		# self.animation.start()

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
		transform.rotate(self._angle)
		painter.setTransform(transform)
		self.loadingIcon.paint(painter, QRect(-self.iconSize // 2, -self.iconSize // 2, self.iconSize, self.iconSize))

		# sync with parent position and rect

	def start(self):
		self.animation.start()
		self.show()
		self.raise_()

	def stop(self,ret:Any=None):
		self.animation.stop()
		self.hide()
		if self.workerThread is not None:
			self.workerThread.quit()
		self.finished.emit(ret)

	def run_thread(self, func:Callable, *args, **kwargs)->QThread:
		self.start()
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