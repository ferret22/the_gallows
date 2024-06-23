from words_getter import select_random_word
from word import Word
from PySide2.QtWidgets import QWidget, QMessageBox
from ui.game_ui import Ui_GameWindow


class GameWindow(QWidget):

    def __init__(self, settings: str, parent=None):
        QWidget.__init__(self, parent)
        self.ui = Ui_GameWindow()
        self.ui.setupUi(self)

        self.msg_info = QMessageBox(self)
        self.settings = settings

        self.random_word = Word(select_random_word(settings))

        self.ui.tryNum.display(self.random_word.tries)
        self.ui.wordLabel.setText('*' * self.random_word.length)

        self.ui.checkWord.clicked.connect(self.check_sign)

    def show_msg_info(self, msg: str, title: str) -> None:
        self.msg_info.setWindowTitle(title)
        self.msg_info.setText(msg)
        self.msg_info.setIcon(QMessageBox.Information)
        self.msg_info.show()

    def get_sign(self) -> str:
        sign = self.ui.signEdit.text()
        if len(sign) == 1:
            return sign

    def check_sign(self) -> None:
        sign = self.get_sign()
        if sign:
            lose_flag, win_flag = self.random_word.guess_letter(sign)

            if lose_flag:
                self.ui.wordLabel.setText(self.random_word.letters)
                self.ui.tryNum.display(self.random_word.tries)

                if win_flag:
                    self.show_msg_info(f"Вы выиграли!\nСлово: {self.random_word.word}", 'The Gallows')
                    self.set_disabled()
            else:
                self.show_msg_info(f'Вы проиграли!\nСлово: {self.random_word.word}', 'The Gallows')
                self.set_disabled()

    def set_disabled(self) -> None:
        self.ui.signEdit.setDisabled(True)
        self.ui.checkWord.setDisabled(True)
        self.ui.wordLabel.setText(self.random_word.word)
