from words_getter import select_random_word
from word import Word


if __name__ == "__main__":
    random_word = Word(select_random_word())
    while random_word.check_win():
        print(f'Попытки: {random_word.tries}')
        sign = input('Введите букву: ')
        if len(sign) == 1:
            if not random_word.guess_letter(sign):
                break
        else:
            print('Неверный ввод!')
