# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_SettingsWindow(object):
    def setupUi(self, SettingsWindow):
        if not SettingsWindow.objectName():
            SettingsWindow.setObjectName(u"SettingsWindow")
        SettingsWindow.resize(679, 344)
        font = QFont()
        font.setFamily(u"Bahnschrift Condensed")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        SettingsWindow.setFont(font)
        self.widget = QWidget(SettingsWindow)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 137, 50))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.comboLanguage = QComboBox(self.widget)
        self.comboLanguage.addItem("")
        self.comboLanguage.addItem("")
        self.comboLanguage.setObjectName(u"comboLanguage")

        self.horizontalLayout.addWidget(self.comboLanguage)

        self.widget1 = QWidget(SettingsWindow)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(30, 260, 621, 81))
        self.horizontalLayout_2 = QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.defaultButton = QPushButton(self.widget1)
        self.defaultButton.setObjectName(u"defaultButton")

        self.horizontalLayout_2.addWidget(self.defaultButton)

        self.cancelButton = QPushButton(self.widget1)
        self.cancelButton.setObjectName(u"cancelButton")

        self.horizontalLayout_2.addWidget(self.cancelButton)

        self.saveButton = QPushButton(self.widget1)
        self.saveButton.setObjectName(u"saveButton")

        self.horizontalLayout_2.addWidget(self.saveButton)


        self.retranslateUi(SettingsWindow)

        QMetaObject.connectSlotsByName(SettingsWindow)
    # setupUi

    def retranslateUi(self, SettingsWindow):
        SettingsWindow.setWindowTitle(QCoreApplication.translate("SettingsWindow", u"The Gallows", None))
        self.label.setText(QCoreApplication.translate("SettingsWindow", u"\u042f\u0437\u044b\u043a", None))
        self.comboLanguage.setItemText(0, QCoreApplication.translate("SettingsWindow", u"RUS", None))
        self.comboLanguage.setItemText(1, QCoreApplication.translate("SettingsWindow", u"ENG", None))

        self.defaultButton.setText(QCoreApplication.translate("SettingsWindow", u"\u041f\u043e \u0443\u043c\u043e\u043b\u0447\u0430\u043d\u0438\u044e", None))
        self.cancelButton.setText(QCoreApplication.translate("SettingsWindow", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.saveButton.setText(QCoreApplication.translate("SettingsWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
    # retranslateUi

