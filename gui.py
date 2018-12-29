from gigreader import GigReader
from preferences import Preferences
import rumps, json, requests


class PreferencePane(rumps.Window):

    def __init__(self):
        super(PreferencePane, self).__init__(title="Preferences")
        self.message = "You can modify the below configuration using JSON. \
            A restart of the application is required for most properties."
        self.default_text = str(json.dumps(Preferences().config,
                                           sort_keys=True,
                                           indent=4,
                                           separators=(',', ': ')
                                           ))
        self.add_button("Cancel")


class About(rumps.Window):

    def __init__(self):
        super(About, self).__init__(title="About")
        self.default_text = str("Version: 1.0.3\nAuthor: Christian D. Tuen")


class StatusBarApp(rumps.App):

    def __init__(self):
        super(StatusBarApp, self).__init__("-- GB")
        try:
            self.preferences = Preferences()
            self.gig_reader = GigReader(self.preferences.ip)
        except requests.exceptions.ReadTimeout:
            rumps.alert("Not able to connect to default IP address, please check the application preferences.")
        except Exception, e:
            rumps.alert(str(e.message))

    @rumps.clicked("Preferences")
    def prefs(self, _):
        response = PreferencePane().run()
        requirements = ['ip', 'interval']
        if response.clicked == 1:
            try:
                user_configuration = json.loads(str(response.text))
                if not all(requirement in user_configuration for requirement in requirements):
                    raise ValueError('You are missing required properties in the JSON configuration.')
                self.preferences.configuration = user_configuration
                self.preferences.write_config()
            except Exception, e:
                rumps.alert(str(e.message))

    @rumps.clicked("About")
    def about(self, _):
        About().run()

    @rumps.timer(Preferences().interval)
    def gig_updater(self, _):
        self.gig_reader.get_cookie()
        self.gig_reader.update_usage()
        usage = self.gig_reader.get_usage()
        if usage == -1:
            usage = "--"
        new_title = str(usage)
        if self.preferences.show_limit:
            new_title += "/%s GB" % str(self.gig_reader.get_stored_limit())
        else:
            new_title += " GB"
        self.title = new_title


if __name__ == "__main__":
    StatusBarApp().run()
