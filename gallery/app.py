

from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize, QTimer
# import qdarktheme

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
        self.load_readme()

        self.ui.btn_scrshot.released.connect(self.grab_screenshot)
        self.ui.btn_settings.hide()

    def grab_screenshot(self):
        self.ui.btn_scrshot.hide()
        self.ui.btn_settings.show()
        import time
        curdir=os.path.dirname(os.path.abspath(__file__))
        pardir=os.path.dirname(curdir)
        screenshot_dir=os.path.join(pardir, 'screenshots')
        os.makedirs(screenshot_dir,exist_ok=True)
        
        # grab gallery
        targetSize=QSize(540, 420)
        self.resize(targetSize)
        time.sleep(0.1)
        self.grab().save(os.path.join(screenshot_dir, "gallery.png"))
        # grab sidebar

        def grab_expanded():
            self.ui.sidetab.grab().save(os.path.join(screenshot_dir, f"{self.ui.sidetab.__class__.__name__}_expanded.png"))
            print("grabbed expanded sidebar")
            self.ui.sidetab.tabbar.animationGroup.finished.disconnect(grab_expanded)

            def grab_folded():
                self.ui.sidetab.grab().save(os.path.join(screenshot_dir, f"{self.ui.sidetab.__class__.__name__}_folded.png"))
                self.ui.sidetab.tabbar.animationGroup.finished.disconnect(grab_folded)
                print("grabbed folded sidebar")

                self.lo.start()
        
                def grab_overlay():
                    self.ui.widget_overlayContainer.grab().save(os.path.join(screenshot_dir, f"{self.lo.__class__.__name__}.png"))
                    print("grabbed overlay")
                    self.lo.stop()
                QTimer.singleShot(1000,grab_overlay)
                self.ui.sidetab.setCurrentIndex(self.ui.sidetab.indexOf(self.ui.tab_overlay))

            self.ui.sidetab.tabbar.animationGroup.finished.connect(grab_folded)
            self.ui.sidetab.setFolded(True)

        self.ui.sidetab.tabbar.animationGroup.finished.connect(grab_expanded)
        self.ui.sidetab.setFolded(False)
        print("waiting for sidebar animation")


        # grab titlebar
        self.ui.widget_titlebar.show()
        self.ui.widget_titlebar.grab().save(os.path.join(screenshot_dir, f"{self.ui.widget_titlebar.__class__.__name__}.png"))
        self.ui.widget_titlebar.hide()
        self.ui.widget_titlebar_container.show()
        self.ui.widget_titlebar_container.grab().save(os.path.join(screenshot_dir, f"{self.ui.widget_titlebar_container.__class__.__name__}.png"))
        # grab overlay

        # destroy setttings button
        self.ui.btn_settings.hide()
        self.ui.btn_scrshot.show()
        # popup message
        QMessageBox.information(self, "Screenshot saved", f"Screenshots saved to {screenshot_dir} folder")

    def load_readme(self):
        # curdir=os.path.dirname(os.path.abspath(__file__))
        # readme_path=os.path.join(os.path.dirname(curdir), 'README.md')
        # self.ui.textBrowser_home.setSource('file:///'+readme_path.replace('\\','/'),type=QTextDocument.ResourceType.MarkdownResource)
        self.ui.textBrowser_home.setMarkdown('''
# The QoreWidgets Gallery

This gallery is a collection of examples of how to use the QoreWidgets library.
''')
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
        self.ui.widget_titlebar.setIconSize(24)
        self.ui.widget_titlebar.setFlatButton(True)
        self.ui.widget_titlebar_container.setFlatButton(True)
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
        self.ui.text_overlayContent.setPlainText('''Fugiat aliqua duis et fugiat irure eu magna mollit labore amet. Elit velit id amet qui sunt voluptate consectetur eiusmod officia deserunt et magna aute. Deserunt cupidatat ea incididunt aute duis id esse commodo sint.
Voluptate laborum occaecat dolor occaecat tempor eu duis quis laborum. Reprehenderit aliquip enim id dolor enim minim ad est veniam id aute labore officia eu. Ea fugiat occaecat et cupidatat culpa anim est cillum duis sunt do. Labore culpa reprehenderit aliqua laboris ut Lorem pariatur mollit non deserunt exercitation cillum.
Amet commodo consequat minim veniam incididunt. Velit Lorem et ut dolore est sit nostrud sunt enim voluptate amet pariatur ut. Ea pariatur enim irure dolor enim id cillum occaecat pariatur deserunt velit minim. In cupidatat anim duis commodo voluptate nostrud mollit enim veniam amet Lorem qui.''')
        self.lo=QoreWidgets.LoadingOverlay(self.ui.widget_overlayContainer,rps=1.5,alpha=150)

        def test_overlay():
            import time
            def action():
                # print("overlay action")
                time.sleep(3)
                # print("overlay action done")
            
            self.lo.run_thread(action)

        self.ui.btn_loadingOverlay.clicked.connect(test_overlay)
        self.ui.btn_startOverlay.clicked.connect(self.lo.start)
        self.ui.btn_stopOverlay.clicked.connect(self.lo.stop)
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    # qdarktheme.setup_theme('dark')
    window = MainWindow()
    window.show()

    sys.exit(app.exec())