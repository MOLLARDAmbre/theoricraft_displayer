import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class RowPopup(Gtk.Window):
    def __init__(self, btn):
        super().__init__()

        # Base elements
        self.btn = btn
        self.lbl = Gtk.Label("Option's name")
        self.edit = Gtk.Entry()
        self.grid = Gtk.Grid()
        self.edit.set_text(self.btn.get_text())


        # Buttons with behaviours
        self.delete_btn = Gtk.Button(label="Delete")
        self.save_btn = Gtk.Button(label="Save")
        self.cancel_btn = Gtk.Button(label="Cancel")
        self.save_btn.connect("clicked", self.save)
        self.cancel_btn.connect("clicked", self.cancel)
        self.delete_btn.connect("clicked", self.delete)

        # Grid setup
        self.grid.set_column_homogeneous(True)
        self.grid.set_column_spacing(10)
        self.grid.set_row_homogeneous(True)
        self.grid.set_row_spacing(15)

        # Adds the elements
        self.add(self.grid)
        self.grid.attach(self.lbl, 0, 1, 1, 1)
        self.grid.attach(self.edit, 1, 1, 1, 1)
        self.grid.attach(self.save_btn, 2, 2, 1, 1)
        self.grid.attach(self.cancel_btn, 0, 2, 1, 1)
        self.grid.attach(self.delete_btn, 2, 1, 1, 1)


    def save(self, widget):
        self.btn.update(self.edit.get_text())
        self.close()

    def cancel(self, widget):
        self.close()

    def delete(self, widget):
        self.btn.delete()
        self.close()

### TODO : make it able to delete a row/column or edit the name
