# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'game.ui'
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
        GameWindow.resize(768, 251)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(GameWindow.sizePolicy().hasHeightForWidth())
        GameWindow.setSizePolicy(sizePolicy)
        GameWindow.setMinimumSize(QSize(0, 0))
        GameWindow.setMaximumSize(QSize(768, 400))
        font = QFont()
        font.setFamily(u"Bahnschrift Condensed")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        GameWindow.setFont(font)
        self.gridLayout = QGridLayout(GameWindow)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Label = QLabel(GameWindow)
        self.Label.setObjectName(u"Label")
        self.Label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.Label)

        self.wordLabel = QLabel(GameWindow)
        self.wordLabel.setObjectName(u"wordLabel")
        self.wordLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.wordLabel)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.signEdit = QLineEdit(GameWindow)
        self.signEdit.setObjectName(u"signEdit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(100)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.signEdit.sizePolicy().hasHeightForWidth())
        self.signEdit.setSizePolicy(sizePolicy1)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.signEdit)

        self.checkWord = QPushButton(GameWindow)
        self.checkWord.setObjectName(u"checkWord")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.checkWord.sizePolicy().hasHeightForWidth())
        self.checkWord.setSizePolicy(sizePolicy2)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.checkWord)


        self.gridLayout.addLayout(self.formLayout, 1, 0, 1, 1)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label = QLabel(GameWindow)
        self.label.setObjectName(u"label")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label)

        self.tryNum = QLCDNumber(GameWindow)
        self.tryNum.setObjectName(u"tryNum")
        self.tryNum.setFrameShape(QFrame.StyledPanel)
        self.tryNum.setFrameShadow(QFrame.Sunken)
        self.tryNum.setMidLineWidth(4)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.tryNum)


        self.gridLayout.addLayout(self.formLayout_2, 2, 0, 1, 1)


        self.retranslateUi(GameWindow)

        QMetaObject.connectSlotsByName(GameWindow)
    # setupUi

    def retranslateUi(self, GameWindow):
        GameWindow.setWindowTitle(QCoreApplication.translate("GameWindow", u"The Gallows", None))
        self.Label.setText(QCoreApplication.translate("GameWindow", u"\u0421\u043b\u043e\u0432\u043e", None))
        self.wordLabel.setText(QCoreApplication.translate("GameWindow", u"TextLabel", None))
        self.signEdit.setPlaceholderText(QCoreApplication.translate("GameWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0431\u0443\u043a\u0432\u0443", None))
        self.checkWord.setText(QCoreApplication.translate("GameWindow", u"\u041f\u0440\u043e\u0432\u0435\u0440\u0438\u0442\u044c \u0431\u0443\u043a\u0432\u0443", None))
        self.label.setText(QCoreApplication.translate("GameWindow", u"\u041f\u043e\u043f\u044b\u0442\u043a\u0438:", None))
    # retranslateUi

