from words_getter import select_random_word
from word import Word
from PySide2.QtWidgets import *
from ui.main_ui import Ui_GameWindow
import sys


def test_con_game():
    random_word = Word(select_random_word())
    while random_word.check_win():
        print(f'Попытки: {random_word.tries}')
        sign = input('Введите букву: ')
        if len(sign) == 1:
            if not random_word.guess_letter(sign):
                break
        else:
            print('Неверный ввод!')


class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.ui = Ui_GameWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    # test_con_game()
    game = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(game.exec_())
