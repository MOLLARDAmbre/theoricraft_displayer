import gi
from row_popup import RowPopup
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class RowButton(Gtk.Button):
    def __init__(self, lbl, parent, orientation, index):
        super().__init__()
        super().set_label(lbl)
        self.connect("clicked", self.display_popup)
        self.parent = parent
        self.orientation = orientation
        self.index = index


    def display_popup(self, widget):
        win = RowPopup(self)
        win.show_all()

    def get_text(self):
        return super().get_label()

    def update(self, lbl):
        super().set_label(lbl)

    def delete(self):
        self.parent.delete_row(self.orientation, self.index)

    def desincr_index(self):
        self.index = self.index - 1

### TODO : link with the popup
