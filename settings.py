import files


class Settings:

    @staticmethod
    def set_default():
        with open(files.default_settings, 'r') as default_settings:
            settings = default_settings.read()
        default_settings.close()

        with open(files.settings_file, 'w') as settings_file:
            settings_file.write(settings)
        settings_file.close()

    @staticmethod
    def load_settings():
        with open(files.settings_file, 'r') as settings_file:
            settings = settings_file.read()
        settings_file.close()

        return settings
