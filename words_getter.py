import random


def check_language():
    with open('settings/language.txt', 'r') as language_file:
        language = language_file.read()
    language_file.close()

    match language:
        case 'ru\n':
            return 1
        case 'en\n':
            return 2
        case _:
            return False


def refactor_words(words: list[str]):
    answer = []

    for word in words:
        idx = word.find('\n')
        answer.append(word[:idx])

    return answer


def open_words():
    language = check_language()

    match language:
        case 1:
            return open_word_file('ru')
        case 2:
            return open_word_file('en')
        case _:
            return False


def open_word_file(lang: str):
    with open(f'settings/words_{lang}.txt', 'r') as path_file:
        words = path_file.readlines()
        words = refactor_words(words)
        return words


def select_random_word():
    words = open_words()

    if words:
        random_word = random.choice(words)
        return random_word

    return False


if __name__ == "__main__":
    print(select_random_word())
