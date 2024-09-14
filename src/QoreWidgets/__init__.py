from enum import Enum

from . import rc #noqa:F401
class QtBackend(Enum):
	Undefined = 0
	PySide6 = 1
	PyQt5 = 2

qt_backend = QtBackend.Undefined

try:
	import PySide6
	qt_backend = QtBackend.PySide6
except ImportError:
	try:
		import PyQt5
		qt_backend = QtBackend.PyQt5
	except ImportError:
		pass
#[end try import]

if qt_backend == QtBackend.PySide6:
	from .__pyside6__.__sideTabWidget__.sideTabWidget import SideTabWidget
	from .__pyside6__.__immersiveTitleBar__.immersiveTitleBarContainer import ImmersiveTitleBarContainer
	from .__pyside6__.__immersiveTitleBar__.immersiveTitleBar import ImmersiveTitleBar
	from .__pyside6__.__framelessWindow__.framelessWindow import FramelessWindow
	from .__pyside6__.__loadingOverlay__.loadingOverlay import LoadingOverlay
elif qt_backend == QtBackend.PyQt5:
	#TODO
	raise NotImplementedError("PyQt5 backend is not implemented yet.")
else:
	raise ImportError("No Qt backend found. Please install either PySide6 or PyQt5.")