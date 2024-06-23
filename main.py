from PySide2.QtWidgets import QMainWindow, QApplication, QErrorMessage
from ui.main_ui import Ui_MainWindow
import sys
from game import GameWindow
from settings_win import SettingsWindow
from settings import Settings


class MainWindow(QMainWindow, Settings):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.game_win = None
        self.settings_win = None
        self.error = QErrorMessage(self)
        self.settings = self.load_settings()
        self.set_language()

        self.ui.startButton.clicked.connect(self.start_game)
        self.ui.exitButton.clicked.connect(self.exit_game)
        self.ui.settingsButton.clicked.connect(self.open_settings)

    def ms_error(self, title: str, message: str, type_error: str):  # Создание окна ошибки
        self.error.setWindowTitle(title)
        self.error.showMessage(message, type_error)

    def start_game(self) -> None:
        try:
            self.game_win = GameWindow()
            self.game_win.show()
        except TypeError:
            translate = self.open_translate()
            self.ms_error('Dictionary is empty', translate[11], 'TypeError')

    def exit_game(self) -> None:
        self.close()

    def open_settings(self) -> None:
        self.settings_win = SettingsWindow(parent_win=self)
        self.settings_win.show()

    def set_language(self) -> None:
        translate = self.open_translate()

        self.ui.startButton.setText(translate[0])
        self.ui.settingsButton.setText(translate[1])
        self.ui.exitButton.setText(translate[2])


if __name__ == "__main__":
    game = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(game.exec_())
