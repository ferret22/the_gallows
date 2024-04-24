class Word:

    def __init__(self, word: str):
        self.word = word
        self.length = len(word)
        self.tries = int(len(word) / 2.3)
        self.chars = []
        self.letters = '*' * self.length

    def guess_letter(self, letter: str):
        self.chars.append(letter)
        self.letters = ''

        for char in self.word:
            if char in self.chars:
                self.letters += char
            else:
                self.letters += '*'
        self.count_tries(letter)

        return self.check_lose(), self.check_win()

    def count_tries(self, letter: str):
        letter_count = self.word.count(letter)
        if letter_count == 0:
            self.tries -= 1

        letter_count = self.letters.count(letter)
        if letter_count > 0:
            self.tries -= 1

    def check_lose(self):
        if self.tries < 0:
            return False
        return True

    def check_win(self):
        if '*' in self.letters:
            return True
        return False
