from words_getter import select_random_word
from word import Word
from PySide2.QtWidgets import QWidget, QMessageBox
from ui.game_ui import Ui_GameWindow
from settings import Settings


class GameWindow(QWidget, Settings):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_GameWindow()
        self.ui.setupUi(self)

        self.msg_info = QMessageBox(self)
        self.settings = self.load_settings()
        self.set_language()

        self.random_word = Word(select_random_word(self.settings))

        self.ui.tryNum.display(self.random_word.tries + 1)
        self.ui.wordLabel.setText('*' * self.random_word.length)

        self.ui.checkWord.clicked.connect(self.check_sign)

    def set_language(self) -> None:
        translate = self.open_translate()

        self.ui.Label.setText(translate[3])
        self.ui.checkWord.setText(translate[4])
        self.ui.signEdit.setPlaceholderText(translate[5])
        self.ui.label.setText(translate[6])

    def show_msg_info(self, msg: str, title: str) -> None:
        self.msg_info.setWindowTitle(title)
        self.msg_info.setText(msg)
        self.msg_info.setIcon(QMessageBox.Information)
        self.msg_info.show()

    def get_sign(self) -> str:
        translate = self.open_translate()
        sign = self.ui.signEdit.text()
        if len(sign) == 1:
            return sign
        else:
            self.show_msg_info(translate[12], 'Invalid input')

    def check_sign(self) -> None:
        translate = self.open_translate()
        sign = self.get_sign()
        if sign:
            lose_flag, win_flag = self.random_word.guess_letter(sign)

            if lose_flag:
                self.ui.wordLabel.setText(self.random_word.letters)

                if win_flag:
                    self.show_msg_info(f"{translate[13]}\n{translate[3]}: {self.random_word.word}",
                                       'The Gallows')
                    self.set_disabled()
            else:
                self.show_msg_info(f'{translate[14]}\n{translate[3]}: {self.random_word.word}', 'The Gallows')
                self.set_disabled()

        self.ui.signEdit.setText('')
        self.ui.tryNum.display(self.random_word.tries + 1)

    def set_disabled(self) -> None:
        self.ui.signEdit.setDisabled(True)
        self.ui.checkWord.setDisabled(True)
        self.ui.wordLabel.setText(self.random_word.word)
