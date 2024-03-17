import random


def check_language():
    with open('settings/language.txt', 'r') as language_file:
        language = language_file.read()
    language_file.close()

    if language == 'ru\n':
        return 1

    if language == 'en\n':
        return 2

    return False


def refactor_words(words: list[str]):
    answer = []

    for word in words:
        idx = word.find('\n')
        answer.append(word[:idx])

    return answer


def open_words():
    language = check_language()

    if language == 1:
        with open('settings/words_ru.txt', 'r') as path_file:
            words = path_file.readlines()
            words = refactor_words(words)
            return words

    if language == 2:
        with open('settings/words_en.txt', 'r') as path_file:
            words = path_file.readlines()
            words = refactor_words(words)
            return words

    return False


def select_random_word():
    words = open_words()

    if words:
        random_word = random.choice(words)
        return random_word

    return False


if __name__ == "__main__":
    print(select_random_word())
