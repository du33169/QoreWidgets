# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QTabWidget, QVBoxLayout, QWidget)

from QoreWidgets import (ImmersiveTitleBar, SideTabWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_titlebar = ImmersiveTitleBar(self.centralwidget)
        self.widget_titlebar.setObjectName(u"widget_titlebar")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_titlebar)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.label_appIcon = QLabel(self.widget_titlebar)
        self.label_appIcon.setObjectName(u"label_appIcon")

        self.horizontalLayout_2.addWidget(self.label_appIcon)

        self.label_title = QLabel(self.widget_titlebar)
        self.label_title.setObjectName(u"label_title")

        self.horizontalLayout_2.addWidget(self.label_title)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.comboBox = QComboBox(self.widget_titlebar)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.comboBox)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.label = QLabel(self.widget_titlebar)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.line = QFrame(self.widget_titlebar)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_2.addWidget(self.line)


        self.verticalLayout.addWidget(self.widget_titlebar)

        self.sidetab = SideTabWidget(self.centralwidget)
        self.sidetab.setObjectName(u"sidetab")
        self.sidetab.setTabPosition(QTabWidget.TabPosition.West)
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
        self.label_foldState.setAlignment(Qt.AlignmentFlag.AlignCenter)

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

        self.retranslateUi(MainWindow)

        self.sidetab.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_appIcon.setText(QCoreApplication.translate("MainWindow", u"[Icon]", None))
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"This is ImmersiveTitleBar. Drag to move window.", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Put", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"any widget", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"you like", None))

        self.label.setText(QCoreApplication.translate("MainWindow", u"auto margin reserving\u2192", None))
        self.label_foldState.setText("")
        self.label_toggle_prompt.setText(QCoreApplication.translate("MainWindow", u"Programmatic Toggle:", None))
        self.btn_fold.setText(QCoreApplication.translate("MainWindow", u"Fold", None))
        self.btn_expand.setText(QCoreApplication.translate("MainWindow", u"Expand", None))
        self.label_click_toggle_prompt.setText(QCoreApplication.translate("MainWindow", u"\u2190 click the menu button to toggle sidebar", None))
        self.sidetab.setTabText(self.sidetab.indexOf(self.tab_home), QCoreApplication.translate("MainWindow", u"Home", None))
        self.sidetab.setTabText(self.sidetab.indexOf(self.tab_settings), QCoreApplication.translate("MainWindow", u"Settings", None))
        self.sidetab.setTabText(self.sidetab.indexOf(self.tab_about), QCoreApplication.translate("MainWindow", u"About", None))
    # retranslateUi

