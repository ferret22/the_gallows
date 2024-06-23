from PySide2.QtWidgets import QWidget
from ui.settings_ui import Ui_SettingsWindow
import files
from settings import Settings
from words_getter import open_word_file


class SettingsWindow(QWidget, Settings):

    def __init__(self, parent=None, parent_win=None):
        super().__init__(parent)
        self.ui = Ui_SettingsWindow()
        self.ui.setupUi(self)

        self.parent_win = parent_win
        self.settings = self.load_settings()
        self.set_language()

        self.ui.cancelButton.clicked.connect(self.cancel_settings)
        self.ui.saveButton.clicked.connect(self.save_settings)
        self.ui.defaultButton.clicked.connect(self.set_default_settings)

    def cancel_settings(self) -> None:
        self.parent_win.set_language()
        self.close()

    def closeEvent(self, event):
        self.cancel_settings()

    def save_settings(self) -> None:
        language = self.ui.comboLanguage.currentText()
        with open(files.settings_file, 'w') as language_file:
            language_file.write(language + '\n')
        language_file.close()

        self.ui.comboLanguage.setCurrentText(language)
        self.set_language()

    def set_default_settings(self) -> None:
        self.set_default()
        self.settings = self.load_settings()
        self.ui.comboLanguage.setCurrentText(self.settings[:3])
        self.set_language()

    def set_language(self) -> None:
        self.settings = self.load_settings()
        self.ui.comboLanguage.setCurrentText(self.settings[:3])

        rus_len = len(open_word_file(files.words_ru))
        eng_len = len(open_word_file(files.words_en))
        translate = self.open_translate()

        self.ui.label.setText(translate[7])
        self.ui.defaultButton.setText(translate[8])
        self.ui.cancelButton.setText(translate[9])
        self.ui.saveButton.setText(translate[10])
        self.ui.groupBox.setTitle(translate[15])
        self.ui.labelRus.setText(f'RUS - {rus_len} {translate[16]}')
        self.ui.labelEng.setText(f'ENG - {eng_len} {translate[16]}')
        self.ui.rusButton.setText(translate[17])
        self.ui.engButton.setText(translate[17])
