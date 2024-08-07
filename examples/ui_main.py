# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QTabWidget, QVBoxLayout, QWidget)

from QoreWidgets import SideTabWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.sidetab = SideTabWidget(self.centralwidget)
        self.sidetab.setObjectName(u"sidetab")
        self.sidetab.setTabPosition(QTabWidget.West)
        self.sidetab.setUsesScrollButtons(True)
        self.sidetab.setDocumentMode(False)
        self.sidetab.setTabBarAutoHide(False)
        self.tab_home = QWidget()
        self.tab_home.setObjectName(u"tab_home")
        self.verticalLayout_2 = QVBoxLayout(self.tab_home)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.label_foldState = QLabel(self.tab_home)
        self.label_foldState.setObjectName(u"label_foldState")
        self.label_foldState.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_foldState)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label_toggle_prompt = QLabel(self.tab_home)
        self.label_toggle_prompt.setObjectName(u"label_toggle_prompt")

        self.horizontalLayout.addWidget(self.label_toggle_prompt)

        self.btn_fold = QPushButton(self.tab_home)
        self.btn_fold.setObjectName(u"btn_fold")

        self.horizontalLayout.addWidget(self.btn_fold)

        self.btn_expand = QPushButton(self.tab_home)
        self.btn_expand.setObjectName(u"btn_expand")

        self.horizontalLayout.addWidget(self.btn_expand)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.label_click_toggle_prompt = QLabel(self.tab_home)
        self.label_click_toggle_prompt.setObjectName(u"label_click_toggle_prompt")

        self.verticalLayout_2.addWidget(self.label_click_toggle_prompt)

        icon = QIcon(QIcon.fromTheme(u":/icons/home"))
        self.sidetab.addTab(self.tab_home, icon, "")
        self.tab_settings = QWidget()
        self.tab_settings.setObjectName(u"tab_settings")
        icon1 = QIcon(QIcon.fromTheme(u":/icons/settings"))
        self.sidetab.addTab(self.tab_settings, icon1, "")
        self.tab_about = QWidget()
        self.tab_about.setObjectName(u"tab_about")
        icon2 = QIcon(QIcon.fromTheme(u":/icons/info"))
        self.sidetab.addTab(self.tab_about, icon2, "")

        self.verticalLayout.addWidget(self.sidetab)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.sidetab.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_foldState.setText("")
        self.label_toggle_prompt.setText(QCoreApplication.translate("MainWindow", u"Programmatic Toggle:", None))
        self.btn_fold.setText(QCoreApplication.translate("MainWindow", u"Fold", None))
        self.btn_expand.setText(QCoreApplication.translate("MainWindow", u"Expand", None))
        self.label_click_toggle_prompt.setText(QCoreApplication.translate("MainWindow", u"\u2190 click the menu button to toggle sidebar", None))
        self.sidetab.setTabText(self.sidetab.indexOf(self.tab_home), QCoreApplication.translate("MainWindow", u"Home", None))
        self.sidetab.setTabText(self.sidetab.indexOf(self.tab_settings), QCoreApplication.translate("MainWindow", u"Settings", None))
        self.sidetab.setTabText(self.sidetab.indexOf(self.tab_about), QCoreApplication.translate("MainWindow", u"About", None))
    # retranslateUi

