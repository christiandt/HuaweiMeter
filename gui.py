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
        self.default_text = str("Version: 0.0.1rc\nAuthor: Christian")


class StatusBarApp(rumps.App):

    def __init__(self):
        super(StatusBarApp, self).__init__("-- GB")
        self.preferences = Preferences()
        self.gig_reader = GigReader(self.preferences.ip)

    @rumps.clicked("Preferences")
    def prefs(self, _):
        response = PreferencePane().run()
        if response.clicked == 1:
            try:
                self.preferences.configuration = json.loads(str(response.text))
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
