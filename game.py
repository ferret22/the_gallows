from words_getter import select_random_word
from word import Word
from PySide2.QtWidgets import *
from ui.game_ui import Ui_GameWindow


class GameWindow(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_GameWindow()
        self.ui.setupUi(self)

        self.error = QErrorMessage(self)
        self.msg_info = QMessageBox(self)

        self.random_word = Word(select_random_word())

        self.ui.tryNum.display(self.random_word.tries)
        self.ui.wordLabel.setText('*' * self.random_word.length)

        self.ui.checkWord.clicked.connect(self.check_sign)

    def show_msg_info(self, msg: str, title: str):
        self.msg_info.setWindowTitle(title)
        self.msg_info.setText(msg)
        self.msg_info.setIcon(QMessageBox.Information)
        self.msg_info.show()

    def ms_error(self, title: str, message: str, type_error: str):
        self.error.setWindowTitle(title)
        self.error.showMessage(message, type_error)

    def get_sign(self):
        sign = self.ui.signEdit.text()
        if len(sign) == 1:
            return sign

    def check_sign(self):
        sign = self.get_sign()
        if sign:
            lose_flag, win_flag = self.random_word.guess_letter(sign)

            if lose_flag:
                self.ui.signEdit.setText(self.random_word.letters)
                self.ui.tryNum.display(self.random_word.tries)

                if win_flag:
                    self.show_msg_info(f"You won!\nWord: {self.random_word.word}", 'The Gallows')
                    self.set_disabled()
            else:
                self.show_msg_info(f'You lose!\nWord: {self.random_word.word}', 'The Gallows')
                self.set_disabled()

    def set_disabled(self):
        self.ui.signEdit.setDisabled(True)
        self.ui.checkWord.setDisabled(True)
        self.ui.wordLabel.setText(self.random_word.word)
