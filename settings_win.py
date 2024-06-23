from PySide2.QtWidgets import QWidget
from ui.settings_ui import Ui_SettingsWindow
import files
from settings import Settings


class SettingsWindow(QWidget, Settings):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_SettingsWindow()
        self.ui.setupUi(self)

        self.settings = self.load_settings()
        self.set_language()

        self.ui.cancelButton.clicked.connect(self.cancel_settings)
        self.ui.saveButton.clicked.connect(self.save_settings)
        self.ui.defaultButton.clicked.connect(self.set_default_settings)

    def cancel_settings(self) -> None:
        self.close()

    def save_settings(self) -> None:
        language = self.ui.comboLanguage.currentText()
        with open(files.settings_file, 'w') as language_file:
            language_file.write(language + '\n')
        language_file.close()

        self.set_language()

    def set_default_settings(self) -> None:
        self.set_default()

        with open(files.settings_file, 'r') as settings_file:
            settings = settings_file.read()
        settings_file.close()

        self.ui.comboLanguage.setCurrentText(settings[:3])

    def set_language(self):
        self.ui.comboLanguage.setCurrentText(self.settings[:3])

        translate = self.open_translate()

        self.ui.label.setText(translate[7])
        self.ui.defaultButton.setText(translate[8])
        self.ui.cancelButton.setText(translate[9])
        self.ui.saveButton.setText(translate[10])
