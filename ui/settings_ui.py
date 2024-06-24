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

import ui.icons.icons

class Ui_SettingsWindow(object):
    def setupUi(self, SettingsWindow):
        if not SettingsWindow.objectName():
            SettingsWindow.setObjectName(u"SettingsWindow")
        SettingsWindow.resize(679, 344)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SettingsWindow.sizePolicy().hasHeightForWidth())
        SettingsWindow.setSizePolicy(sizePolicy)
        SettingsWindow.setMinimumSize(QSize(679, 344))
        SettingsWindow.setMaximumSize(QSize(800, 600))
        font = QFont()
        font.setFamily(u"Bahnschrift Condensed")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        SettingsWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/icon/settings.png", QSize(), QIcon.Normal, QIcon.Off)
        SettingsWindow.setWindowIcon(icon)
        self.gridLayout_2 = QGridLayout(SettingsWindow)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(SettingsWindow)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.comboLanguage = QComboBox(SettingsWindow)
        icon1 = QIcon()
        icon1.addFile(u":/win/russia.png", QSize(), QIcon.Normal, QIcon.Off)
        self.comboLanguage.addItem(icon1, "")
        icon2 = QIcon()
        icon2.addFile(u":/win/united-kingdom.png", QSize(), QIcon.Normal, QIcon.Off)
        self.comboLanguage.addItem(icon2, "")
        self.comboLanguage.setObjectName(u"comboLanguage")
        self.comboLanguage.setIconSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.comboLanguage)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.defaultDictionary = QPushButton(SettingsWindow)
        self.defaultDictionary.setObjectName(u"defaultDictionary")

        self.verticalLayout_2.addWidget(self.defaultDictionary)


        self.horizontalLayout_5.addLayout(self.verticalLayout_2)

        self.groupBox = QGroupBox(SettingsWindow)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.labelRus = QLabel(self.groupBox)
        self.labelRus.setObjectName(u"labelRus")

        self.horizontalLayout_3.addWidget(self.labelRus)

        self.rusButton = QPushButton(self.groupBox)
        self.rusButton.setObjectName(u"rusButton")
        self.rusButton.setIcon(icon1)
        self.rusButton.setIconSize(QSize(32, 32))

        self.horizontalLayout_3.addWidget(self.rusButton)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.labelEng = QLabel(self.groupBox)
        self.labelEng.setObjectName(u"labelEng")

        self.horizontalLayout_4.addWidget(self.labelEng)

        self.engButton = QPushButton(self.groupBox)
        self.engButton.setObjectName(u"engButton")
        self.engButton.setIcon(icon2)
        self.engButton.setIconSize(QSize(32, 32))

        self.horizontalLayout_4.addWidget(self.engButton)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.horizontalLayout_5.addWidget(self.groupBox)


        self.gridLayout_2.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 83, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 1, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.defaultButton = QPushButton(SettingsWindow)
        self.defaultButton.setObjectName(u"defaultButton")
        icon3 = QIcon()
        icon3.addFile(u":/win/default.png", QSize(), QIcon.Normal, QIcon.Off)
        self.defaultButton.setIcon(icon3)
        self.defaultButton.setIconSize(QSize(30, 30))

        self.horizontalLayout_2.addWidget(self.defaultButton)

        self.cancelButton = QPushButton(SettingsWindow)
        self.cancelButton.setObjectName(u"cancelButton")
        icon4 = QIcon()
        icon4.addFile(u":/win/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cancelButton.setIcon(icon4)
        self.cancelButton.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.cancelButton)

        self.saveButton = QPushButton(SettingsWindow)
        self.saveButton.setObjectName(u"saveButton")
        icon5 = QIcon()
        icon5.addFile(u":/win/diskette.png", QSize(), QIcon.Normal, QIcon.Off)
        self.saveButton.setIcon(icon5)
        self.saveButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.saveButton)


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)


        self.retranslateUi(SettingsWindow)

        QMetaObject.connectSlotsByName(SettingsWindow)
    # setupUi

    def retranslateUi(self, SettingsWindow):
        SettingsWindow.setWindowTitle(QCoreApplication.translate("SettingsWindow", u"The Gallows", None))
        self.label.setText(QCoreApplication.translate("SettingsWindow", u"\u042f\u0437\u044b\u043a", None))
        self.comboLanguage.setItemText(0, QCoreApplication.translate("SettingsWindow", u"RUS", None))
        self.comboLanguage.setItemText(1, QCoreApplication.translate("SettingsWindow", u"ENG", None))

        self.defaultDictionary.setText(QCoreApplication.translate("SettingsWindow", u"\u0421\u043b\u043e\u0432\u0430\u0440\u0438 \u043f\u043e \u0443\u043c\u043e\u043b\u0447\u0430\u043d\u0438\u044e", None))
        self.groupBox.setTitle(QCoreApplication.translate("SettingsWindow", u"\u0421\u0442\u0430\u0442\u0443\u0441 \u0441\u043b\u043e\u0432\u0430\u0440\u0435\u0439", None))
        self.labelRus.setText(QCoreApplication.translate("SettingsWindow", u"RUS - ... \u0441\u043b\u043e\u0432", None))
        self.rusButton.setText(QCoreApplication.translate("SettingsWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c", None))
        self.labelEng.setText(QCoreApplication.translate("SettingsWindow", u"ENG - ... \u0441\u043b\u043e\u0432", None))
        self.engButton.setText(QCoreApplication.translate("SettingsWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c", None))
        self.defaultButton.setText(QCoreApplication.translate("SettingsWindow", u"\u041f\u043e \u0443\u043c\u043e\u043b\u0447\u0430\u043d\u0438\u044e", None))
        self.cancelButton.setText(QCoreApplication.translate("SettingsWindow", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.saveButton.setText(QCoreApplication.translate("SettingsWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
    # retranslateUi

