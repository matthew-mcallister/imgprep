import sys
from typing import Any

import gi

# fmt: off
gi.require_version('Adw', '1')
from gi.repository import Adw  # type: ignore
gi.require_version('Gtk', '4.0')
from gi.repository import Gtk  # type: ignore
# fmt: on


class MainWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class App(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)

    def on_activate(self, app):
        self.win = MainWindow(application=app)
        self.win.present()


def on_activate(app: Any) -> None:
    win = Gtk.ApplicationWindow(application=app)
    win.present()


def main():
    app = App(application_id='dev.imgprep.App')
    app.run(sys.argv)


if __name__ == '__main__':
    main()
