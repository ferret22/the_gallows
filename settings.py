import files
from words_getter import check_language


class Settings:

    @staticmethod
    def set_default() -> None:
        with open(files.default_settings, 'r') as default_settings:
            settings = default_settings.read()
        default_settings.close()

        with open(files.settings_file, 'w') as settings_file:
            settings_file.write(settings)
        settings_file.close()

    @staticmethod
    def load_settings() -> str:
        with open(files.settings_file, 'r') as settings_file:
            settings = settings_file.read()
        settings_file.close()

        return settings

    def open_translate(self) -> list[str] | bool:
        language = check_language(self.load_settings())

        match language:
            case 1:
                return self.read_translate(files.translate_ru)
            case 2:
                return self.read_translate(files.translate_en)
            case _:
                return False

    @staticmethod
    def read_translate(file: str) -> list[str]:
        refactor_translate = []
        with open(file, 'r', encoding='UTF-8') as translate_file:
            translate = translate_file.readlines()
        translate_file.close()

        for word in translate:
            ref_word = word.split('\n')
            refactor_translate.append(''.join(ref_word))

        return refactor_translate
