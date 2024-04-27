from PySide2.QtWidgets import *
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

        self.settings = self.load_settings()

        self.ui.startButton.clicked.connect(self.start_game)
        self.ui.exitButton.clicked.connect(self.exit_game)
        self.ui.settingsButton.clicked.connect(self.open_settings)

    def start_game(self):
        self.game_win = GameWindow(self.settings)
        self.game_win.show()

    def exit_game(self):
        self.close()

    def open_settings(self):
        self.settings_win = SettingsWindow()
        self.settings_win.show()


if __name__ == "__main__":
    game = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(game.exec_())
