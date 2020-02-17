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
        self.value = 0
        self.connect("clicked", self.open_popup)
        self.clicked = False

    def give_result(self, value, label):
        super().set_label(label) # Sets the new label
        self.value = value # Sets the new value
        col = Color.get_color(value) # Gets the new color
        super().override_background_color(0, col) #Update the background

    def open_popup(self, btn):
        if (self.clicked):
            win = ResultPopup(self, self.value, self.get_label())
        else :
            self.clicked = True
            win = ResultPopup(self, self.value, "")
        win.show_all()

    def get_color_array(self):
        return Color.get_color_array(self.value)

    def get_text(self):
        return self.get_label()
