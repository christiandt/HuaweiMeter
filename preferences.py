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
        return self.configuration['ip']

    @ip.setter
    def ip(self, value):
        self.configuration['ip'] = value

    @property
    def interval(self):
        return self.configuration['interval']

    @interval.setter
    def interval(self, value):
        self.configuration['interval'] = value

    @property
    def config(self):
        return self.configuration

    @config.setter
    def config(self, value):
        self.configuration = value


