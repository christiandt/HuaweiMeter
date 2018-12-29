import json


class Preferences:

    def __init__(self):
        self.configuration = dict()
        self.filename = "configuration.json"
        self.read_config()

    def write_config(self):
        with open(self.filename, 'wb') as f:
            f.write(json.dumps(self.configuration))

    def read_config(self):
        with open(self.filename, 'r') as f:
            self.configuration = json.loads(f.read())

    @property
    def ip(self):
        return str(self.configuration['ip'])

    @ip.setter
    def ip(self, value):
        self.configuration['ip'] = str(value)

    @property
    def interval(self):
        return int(self.configuration['interval'])

    @interval.setter
    def interval(self, value):
        self.configuration['interval'] = int(value)

    @property
    def show_limit(self):
        if 'show_limit' in self.configuration:
            return bool(self.configuration['show_limit'])
        return False

    @show_limit.setter
    def show_limit(self, value):
        self.configuration['show_limit'] = bool(value)

    @property
    def config(self):
        return self.configuration

    @config.setter
    def config(self, value):
        self.configuration = value


