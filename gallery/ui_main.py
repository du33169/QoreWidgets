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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QTabWidget, QTextBrowser,
    QVBoxLayout, QWidget)

from QoreWidgets import (ImmersiveTitleBar, ImmersiveTitleBarContainer, SideTabWidget)

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

        self.verticalLayout.addWidget(self.widget_titlebar)

        self.widget_titlebar_container = ImmersiveTitleBarContainer(self.centralwidget)
        self.widget_titlebar_container.setObjectName(u"widget_titlebar_container")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_titlebar_container)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.label_appIcon = QLabel(self.widget_titlebar_container)
        self.label_appIcon.setObjectName(u"label_appIcon")

        self.horizontalLayout_2.addWidget(self.label_appIcon)

        self.label_title = QLabel(self.widget_titlebar_container)
        self.label_title.setObjectName(u"label_title")

        self.horizontalLayout_2.addWidget(self.label_title)

        self.lineEdit = QLineEdit(self.widget_titlebar_container)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setFrame(True)
        self.lineEdit.setClearButtonEnabled(True)

        self.horizontalLayout_2.addWidget(self.lineEdit)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.btn_scrshot = QPushButton(self.widget_titlebar_container)
        self.btn_scrshot.setObjectName(u"btn_scrshot")
        icon = QIcon(QIcon.fromTheme(u":/icons/camera"))
        self.btn_scrshot.setIcon(icon)
        self.btn_scrshot.setFlat(True)

        self.horizontalLayout_2.addWidget(self.btn_scrshot)

        self.btn_settings = QPushButton(self.widget_titlebar_container)
        self.btn_settings.setObjectName(u"btn_settings")
        icon1 = QIcon(QIcon.fromTheme(u":/icons/settings"))
        self.btn_settings.setIcon(icon1)
        self.btn_settings.setFlat(True)

        self.horizontalLayout_2.addWidget(self.btn_settings)


        self.verticalLayout.addWidget(self.widget_titlebar_container)

        self.sidetab = SideTabWidget(self.centralwidget)
        self.sidetab.setObjectName(u"sidetab")
        self.sidetab.setTabPosition(QTabWidget.TabPosition.West)
        self.sidetab.setIconSize(QSize(30, 30))
        self.sidetab.setUsesScrollButtons(True)
        self.sidetab.setDocumentMode(False)
        self.sidetab.setTabBarAutoHide(False)
        self.tab_home = QWidget()
        self.tab_home.setObjectName(u"tab_home")
        self.horizontalLayout_5 = QHBoxLayout(self.tab_home)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.textBrowser_home = QTextBrowser(self.tab_home)
        self.textBrowser_home.setObjectName(u"textBrowser_home")
        self.textBrowser_home.setFrameShape(QFrame.Shape.NoFrame)
        self.textBrowser_home.setOpenExternalLinks(True)

        self.horizontalLayout_5.addWidget(self.textBrowser_home)

        icon2 = QIcon(QIcon.fromTheme(u":/icons/home"))
        self.sidetab.addTab(self.tab_home, icon2, "")
        self.tab_sidetab = QWidget()
        self.tab_sidetab.setObjectName(u"tab_sidetab")
        self.verticalLayout_2 = QVBoxLayout(self.tab_sidetab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.tab_sidetab)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.label_toggle_prompt = QLabel(self.tab_sidetab)
        self.label_toggle_prompt.setObjectName(u"label_toggle_prompt")

        self.verticalLayout_2.addWidget(self.label_toggle_prompt)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label_foldState = QLabel(self.tab_sidetab)
        self.label_foldState.setObjectName(u"label_foldState")
        self.label_foldState.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label_foldState)

        self.btn_fold = QPushButton(self.tab_sidetab)
        self.btn_fold.setObjectName(u"btn_fold")

        self.horizontalLayout.addWidget(self.btn_fold)

        self.btn_expand = QPushButton(self.tab_sidetab)
        self.btn_expand.setObjectName(u"btn_expand")

        self.horizontalLayout.addWidget(self.btn_expand)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.tab_sidetab)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.check_tabIcon = QCheckBox(self.tab_sidetab)
        self.check_tabIcon.setObjectName(u"check_tabIcon")
        self.check_tabIcon.setChecked(True)

        self.verticalLayout_2.addWidget(self.check_tabIcon)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.label_click_toggle_prompt = QLabel(self.tab_sidetab)
        self.label_click_toggle_prompt.setObjectName(u"label_click_toggle_prompt")

        self.verticalLayout_2.addWidget(self.label_click_toggle_prompt)

        icon3 = QIcon(QIcon.fromTheme(u":/icons/sidebar"))
        self.sidetab.addTab(self.tab_sidetab, icon3, "")
        self.tab_titlebar = QWidget()
        self.tab_titlebar.setObjectName(u"tab_titlebar")
        self.label_selectTitleBarPrompt = QLabel(self.tab_titlebar)
        self.label_selectTitleBarPrompt.setObjectName(u"label_selectTitleBarPrompt")
        self.label_selectTitleBarPrompt.setGeometry(QRect(120, 90, 291, 16))
        self.tabWidget_selectTitleBar = QTabWidget(self.tab_titlebar)
        self.tabWidget_selectTitleBar.setObjectName(u"tabWidget_selectTitleBar")
        self.tabWidget_selectTitleBar.setGeometry(QRect(130, 130, 471, 291))
        self.tab_simple = QWidget()
        self.tab_simple.setObjectName(u"tab_simple")
        self.lineEdit_setTitle = QLineEdit(self.tab_simple)
        self.lineEdit_setTitle.setObjectName(u"lineEdit_setTitle")
        self.lineEdit_setTitle.setGeometry(QRect(120, 200, 113, 21))
        self.btn_setTitle = QPushButton(self.tab_simple)
        self.btn_setTitle.setObjectName(u"btn_setTitle")
        self.btn_setTitle.setGeometry(QRect(250, 200, 101, 23))
        self.textBrowser = QTextBrowser(self.tab_simple)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(30, 30, 411, 151))
        self.textBrowser.setFrameShape(QFrame.Shape.NoFrame)
        self.tabWidget_selectTitleBar.addTab(self.tab_simple, "")
        self.tab_immersive = QWidget()
        self.tab_immersive.setObjectName(u"tab_immersive")
        self.textBrowser_2 = QTextBrowser(self.tab_immersive)
        self.textBrowser_2.setObjectName(u"textBrowser_2")
        self.textBrowser_2.setGeometry(QRect(20, 20, 421, 171))
        self.textBrowser_2.setFrameShape(QFrame.Shape.NoFrame)
        self.tabWidget_selectTitleBar.addTab(self.tab_immersive, "")
        icon4 = QIcon(QIcon.fromTheme(u":/icons/titlebar"))
        self.sidetab.addTab(self.tab_titlebar, icon4, "")
        self.tab_overlay = QWidget()
        self.tab_overlay.setObjectName(u"tab_overlay")
        self.horizontalLayout_4 = QHBoxLayout(self.tab_overlay)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.tab_overlay)
        self.label.setObjectName(u"label")

        self.verticalLayout_3.addWidget(self.label)

        self.btn_loadingOverlay = QPushButton(self.tab_overlay)
        self.btn_loadingOverlay.setObjectName(u"btn_loadingOverlay")

        self.verticalLayout_3.addWidget(self.btn_loadingOverlay)

        self.label_4 = QLabel(self.tab_overlay)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_3.addWidget(self.label_4)

        self.btn_startOverlay = QPushButton(self.tab_overlay)
        self.btn_startOverlay.setObjectName(u"btn_startOverlay")

        self.verticalLayout_3.addWidget(self.btn_startOverlay)

        self.btn_stopOverlay = QPushButton(self.tab_overlay)
        self.btn_stopOverlay.setObjectName(u"btn_stopOverlay")

        self.verticalLayout_3.addWidget(self.btn_stopOverlay)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)

        self.label_5 = QLabel(self.tab_overlay)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_3.addWidget(self.label_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_5)

        self.widget_overlayContainer = QWidget(self.tab_overlay)
        self.widget_overlayContainer.setObjectName(u"widget_overlayContainer")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_overlayContainer.sizePolicy().hasHeightForWidth())
        self.widget_overlayContainer.setSizePolicy(sizePolicy)
        self.horizontalLayout_7 = QHBoxLayout(self.widget_overlayContainer)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.text_overlayContent = QTextBrowser(self.widget_overlayContainer)
        self.text_overlayContent.setObjectName(u"text_overlayContent")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.text_overlayContent.sizePolicy().hasHeightForWidth())
        self.text_overlayContent.setSizePolicy(sizePolicy1)

        self.horizontalLayout_7.addWidget(self.text_overlayContent)


        self.horizontalLayout_6.addWidget(self.widget_overlayContainer)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_5)


        self.horizontalLayout_4.addLayout(self.verticalLayout_3)

        icon5 = QIcon(QIcon.fromTheme(u":/icons/loading"))
        self.sidetab.addTab(self.tab_overlay, icon5, "")

        self.verticalLayout.addWidget(self.sidetab)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.sidetab.setCurrentIndex(0)
        self.tabWidget_selectTitleBar.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_appIcon.setText(QCoreApplication.translate("MainWindow", u"[Icon]", None))
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"The QoreWidgets Gallery ", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"This is a fake search bar...", None))
        self.btn_scrshot.setText("")
        self.btn_settings.setText("")
        self.sidetab.setTabText(self.sidetab.indexOf(self.tab_home), QCoreApplication.translate("MainWindow", u"Home", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u2190Auto expand on hover", None))
        self.label_toggle_prompt.setText(QCoreApplication.translate("MainWindow", u"The SideTab can also be programmatically toggled:", None))
        self.label_foldState.setText("")
        self.btn_fold.setText(QCoreApplication.translate("MainWindow", u"Fold", None))
        self.btn_expand.setText(QCoreApplication.translate("MainWindow", u"Expand", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"If no tab icon is set, SideTabWidget will draw the first character as icon. ", None))
        self.check_tabIcon.setText(QCoreApplication.translate("MainWindow", u"Use customized icons", None))
        self.label_click_toggle_prompt.setText(QCoreApplication.translate("MainWindow", u"\u2190 click the menu button to toggle sidebar", None))
        self.sidetab.setTabText(self.sidetab.indexOf(self.tab_sidetab), QCoreApplication.translate("MainWindow", u"SideTab", None))
        self.label_selectTitleBarPrompt.setText(QCoreApplication.translate("MainWindow", u"Select title bar style:", None))
        self.btn_setTitle.setText(QCoreApplication.translate("MainWindow", u"Set Title Text", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">A simple title bar inherits ImmersiveTitleBarContainer, with a window icon and window title.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The icon and title will follow the changes of windowIcon and windowTitle of current window.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-r"
                        "ight:0px; -qt-block-indent:0; text-indent:0px;\">Select this if you only want a title bar that can fit your theme.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">For better customization, try the base class ImmersiveTitleBarContainer.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.tabWidget_selectTitleBar.setTabText(self.tabWidget_selectTitleBar.indexOf(self.tab_simple), QCoreApplication.translate("MainWindow", u"ImmersiveTitleBar", None))
        self.textBrowser_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">A immersive title bar container with only minimize, maximize and close button. The rest area are left  as a empty layout for developer to put any widget they want.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0p"
                        "x; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The following actions are supported:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- drag to move window</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- automatically adjusting margin to reserve space for buttons</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- double click to maximize/restore</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">- restore to normal when dragging at maximized state</p></body></html>", None))
        self.tabWidget_selectTitleBar.setTabText(self.tabWidget_selectTitleBar.indexOf(self.tab_immersive), QCoreApplication.translate("MainWindow", u"ImmersiveTitleBarContainer", None))
        self.sidetab.setTabText(self.sidetab.indexOf(self.tab_titlebar), QCoreApplication.translate("MainWindow", u"TitleBar", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Wait for a function:", None))
        self.btn_loadingOverlay.setText(QCoreApplication.translate("MainWindow", u"Play", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Or manually:", None))
        self.btn_startOverlay.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.btn_stopOverlay.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"The overlay will show on the following widget:", None))
        self.sidetab.setTabText(self.sidetab.indexOf(self.tab_overlay), QCoreApplication.translate("MainWindow", u"Overlay", None))
    # retranslateUi

