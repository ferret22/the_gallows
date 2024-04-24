# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_GameWindow(object):
    def setupUi(self, GameWindow):
        if not GameWindow.objectName():
            GameWindow.setObjectName(u"GameWindow")
        GameWindow.resize(800, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(GameWindow.sizePolicy().hasHeightForWidth())
        GameWindow.setSizePolicy(sizePolicy)
        GameWindow.setMinimumSize(QSize(800, 600))
        GameWindow.setMaximumSize(QSize(800, 600))
        self.centralwidget = QWidget(GameWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        GameWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(GameWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        GameWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(GameWindow)
        self.statusbar.setObjectName(u"statusbar")
        GameWindow.setStatusBar(self.statusbar)

        self.retranslateUi(GameWindow)

        QMetaObject.connectSlotsByName(GameWindow)
    # setupUi

    def retranslateUi(self, GameWindow):
        GameWindow.setWindowTitle(QCoreApplication.translate("GameWindow", u"The Gallows", None))
    # retranslateUi

