from gigreader import GigReader
from preferences import Preferences
import rumps, json


class PreferencePane(rumps.Window):

    def __init__(self):
        super(PreferencePane, self).__init__(title="Preferences")
        self.message = "You can modify the below configuration using JSON"
        self.default_text = str(json.dumps(Preferences().config))
        self.add_button("Cancel")


class About(rumps.Window):

    def __init__(self):
        super(About, self).__init__(title="About")
        self.default_text = str("Version: 1.0.1\nAuthor: Christian D. Tuen")


class StatusBarApp(rumps.App):

    def __init__(self):
        super(StatusBarApp, self).__init__("-- GB")
        self.preferences = Preferences()
        self.gig_reader = GigReader(self.preferences.ip)

    @rumps.clicked("Preferences")
    def prefs(self, _):
        response = PreferencePane().run()
        requirements = ['ip', 'interval']
        if response.clicked == 1:
            try:
                user_configuration = json.loads(str(response.text))
                if not all(config in requirements for config in user_configuration):
                    raise ValueError('Required configuration not part of JSON.')
                self.preferences.configuration = user_configuration
                self.preferences.write_config()
            except Exception, e:
                rumps.alert(e.message)

    @rumps.clicked("About")
    def about(self, _):
        About().run()

    @rumps.timer(Preferences().interval)
    def gig_updater(self, _):
        self.gig_reader.get_cookie()
        self.gig_reader.update_usage()
        self.title = str(self.gig_reader.get_usage()) + " GB"


if __name__ == "__main__":
    StatusBarApp().run()