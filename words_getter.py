import random
import files


def check_language(settings: str) -> int | bool:
    language = settings[:5]

    match language:
        case 'RUS\n':
            return 1
        case 'ENG\n':
            return 2
        case _:
            return False


def refactor_words(words: list[str]) -> list[str]:
    answer = []

    for word in words:
        idx = word.find('\n')
        answer.append(word[:idx])

    return answer


def open_words(settings: str) -> list[str] | bool:
    language = check_language(settings)

    match language:
        case 1:
            return open_word_file(files.words_ru)
        case 2:
            return open_word_file(files.words_en)
        case _:
            return False


def write_words(file: str, words: list[str]) -> None:
    with open(file, 'w', encoding='UTF-8') as word_file:
        word_file.writelines(words)
    word_file.close()


def read_words(file: str) -> list[str]:
    with open(file, 'r', encoding='UTF-8') as word_file:
        words = word_file.readlines()
        return words


def open_word_file(file: str) -> list[str]:
    words = read_words(file)
    words = refactor_words(words)
    return words


def select_random_word(settings: str) -> str | bool:
    words = open_words(settings)

    if words:
        random_word = random.choice(words)
        return random_word

    return False
