import configparser
import os


class Configuration:
    __objects = []
    __basedir = 'conf'

    def __init__(self, filename, markdown=None):
        if markdown:
            self.markdown = str(markdown)
        else:
            head, tail = os.path.split(filename)
            if not tail.find('.') == -1:
                tail = tail.split('.')[0]
            self.markdown = tail

        self.filename = filename
        self.path = '{0}/{1}'.format(Configuration.__basedir, filename)
        self.check_exists()

    def make(self, force=False):
        if not os.path.exists(Configuration.__basedir):
            os.makedirs(Configuration.__basedir)

        if not os.path.exists(self.path) or force:
            config = configparser.ConfigParser()

            payload = {}
            if self.markdown == 'main':
                payload = {
                    'GENERIC': [['version'], {'project_name': 'GetChatBot'}],
                    'ABOUT': [['author_fullname', 'author_telegram']],
                    'TELEGRAM': [['token']],
                }

            Configuration.initialize(config, payload)

            with open(self.path, 'w') as configfile:
                config.write(configfile)

        if self not in Configuration.__objects:
            Configuration.__objects.append(self)

    @staticmethod
    def objects():
        return Configuration.__objects

    @staticmethod
    def get_basedir():
        return Configuration.__basedir

    @staticmethod
    def set_basedir(path):
        Configuration.__basedir = str(path)

    @staticmethod
    def initialize(conf, payload):
        convert = Configuration.convert
        for key, value in payload.items():
            conf[key] = convert(*value)

    @staticmethod
    def convert(*args):
        result = {}
        for arg in args:
            if isinstance(arg, list) or isinstance(arg, tuple):
                for option in arg:
                    result[option] = str(Configuration.get_from_env('{}_{}'.format(arg, option), ''))
            elif isinstance(arg, dict):
                result.update(arg)
        return result

    @staticmethod
    def get_from_env(variable, default=None):
        return os.environ.get(variable.upper()) or default

    def check_exists(self):
        if not os.path.exists(self.path):
            self.make()
        elif self not in Configuration.__objects:
                Configuration.__objects.append(self)

    class __Value:
        def __init__(self, data):
            self.__data = str(data)

        def __str__(self):
            return self.__data

        def as_int(self):
            return int(self.__data)

        def as_float(self):
            return float(self.__data)

        def as_bool(self):
            return bool(int(self.__data))

        def as_str(self):
            return self.__data

        def as_csv(self):
            return self.__data.split(',')

    def get(self, section, key, type=None, update=False):
        if type:
            type = str(type).casefold()

        value = None
        if update:
            value = str(Configuration.get_from_env('{}_{}'.format(section, key)))

        if value:
            self.set(section, key, value)
        else:
            self.check_exists()
            config = configparser.ConfigParser()
            config.read(self.path)
            try:
                value = config[section][key]

            except (configparser.NoSectionError, configparser.NoOptionError) as e:
                print(e)

        if value:
            if type == 'bool':
                return self.__Value(value).as_bool()
            elif type == 'int':
                return self.__Value(value).as_int()
            elif type == 'float':
                return self.__Value(value).as_float()
            elif type == 'csv':
                return self.__Value(value).as_csv()
            elif type == 'raw':
                return self.__Value(value)
            else:
                return self.__Value(value).as_str()
        else:
            return None

    def set(self, section, key, data):
        self.check_exists()
        config = configparser.ConfigParser()
        config.read(self.path)
        try:
            config[section][key] = data
        except (configparser.NoSectionError, configparser.NoOptionError) as e:
            print(e)

        with open(self.path, 'w') as configfile:
            config.write(configfile)
