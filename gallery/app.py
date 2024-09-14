

from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
# import qdarktheme

import rc_assets# noqa:F401
try:
    import QoreWidgets
except ImportError:
    print("QoreWidgets not installed, trying to import from local src")
    import sys
    import os
    # switch to current path
    curdir=os.path.dirname(os.path.abspath(__file__))
    # get parent dir
    sys.path.append(
        os.path.join(os.path.dirname(curdir) , 'src')
    )
    import QoreWidgets

from ui_main import Ui_MainWindow

class MainWindow(QoreWidgets.FramelessWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.sidebar_example()
        self.titlebar_example()
        self.overlay_example()

    def sidebar_example(self):
        def update_foldState(fold: bool):
            self.ui.label_foldState.setText(f"The Sidebar is {'folded >_<' if fold else 'unfolded OvO'}")

        self.ui.sidetab.foldStateChanged.connect(update_foldState)
        update_foldState(self.ui.sidetab.isFolded())

        self.ui.btn_expand.clicked.connect(lambda: self.ui.sidetab.setFolded(False))
        self.ui.btn_fold.clicked.connect(lambda: self.ui.sidetab.setFolded(True))

        self.icons=[]
        for i in range(self.ui.sidetab.count()):
            self.icons.append(self.ui.sidetab.tabIcon(i))
        def toggle_icon():
            if self.ui.check_tabIcon.isChecked():
                for i in range(self.ui.sidetab.count()):
                    self.ui.sidetab.setTabIcon(i, self.icons[i])
            else:
                # save all tab icons and set all to null               
                for i in range(self.ui.sidetab.count()):
                    self.ui.sidetab.setTabIcon(i, QIcon())
        self.ui.check_tabIcon.stateChanged.connect(toggle_icon)
        toggle_icon()

    def titlebar_example(self):
        self.ui.label_appIcon.setPixmap(QIcon(":/icons/account").pixmap(20))
        self.setWindowIcon(QIcon(":/icons/account").pixmap(20))
        def toggle_titlebar():
            if self.ui.tabWidget_selectTitleBar.currentWidget()==self.ui.tab_simple:
                self.ui.widget_titlebar.show()
                self.ui.widget_titlebar_container.hide()
            elif self.ui.tabWidget_selectTitleBar.currentWidget()==self.ui.tab_immersive:
                self.ui.widget_titlebar.hide()
                self.ui.widget_titlebar_container.show()
        self.ui.tabWidget_selectTitleBar.currentChanged.connect(toggle_titlebar)

        def set_window_title():
            self.setWindowTitle(self.ui.lineEdit_setTitle.text())
        self.ui.btn_setTitle.clicked.connect(set_window_title)

        toggle_titlebar()

    def overlay_example(self):
        lo=QoreWidgets.LoadingOverlay(self.ui.tab_overlay,rps=1.5,alpha=150)
        def test_overlay():
            import time
            def action():
                # print("overlay action")
                time.sleep(3)
                # print("overlay action done")
            
            lo.run(action)

        self.ui.btn_loadingOverlay.clicked.connect(test_overlay)
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    # qdarktheme.setup_theme('dark')
    window = MainWindow()
    window.show()

    sys.exit(app.exec())