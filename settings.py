from PySide2.QtWidgets import *
from ui.settings_ui import Ui_SettingsWindow


class SettingsWindow(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_SettingsWindow()
        self.ui.setupUi(self)

