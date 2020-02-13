import gi
import Color
from result_popup import ResultPopup
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import Gdk

class OptionButton(Gtk.Button):
    def __init__(self):
        super().__init__(self)
        super().set_label("Result unknown")
        self.value = None # We don't have a value yet
        self.connect("clicked", self.open_popup)

    def give_result(self, value, label):
        super().set_label(label) # Sets the new label
        self.value = value # Sets the new value
        col = Color.get_color(value) # Gets the new color
        super().override_background_color(0, col) #Update the background

    def open_popup(self, btn):
        win = ResultPopup(self)
        win.show_all()


### TODO : make it change color based on what it needs
### TODO : link with the popup
