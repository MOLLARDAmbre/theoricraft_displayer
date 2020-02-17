import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import Gdk


class ResultPopup(Gtk.Window):
    def __init__(self, btn, val, lbl):
        super().__init__()

        # Grid setup
        self.grid = Gtk.Grid()
        self.grid.set_column_homogeneous(True)
        self.grid.set_column_spacing(10)
        self.grid.set_row_homogeneous(True)
        self.grid.set_row_spacing(15)

        # Base elements
        self.btn = btn
        self.edit = Gtk.Entry()
        self.edit.set_text(lbl)
        self.greeting = Gtk.Label("How good is the result for the offensive player ?")
        self.range_label = Gtk.Label("Please enter a number from -5 to 5")
        self.scale = Gtk.Scale.new_with_range(Gtk.Orientation.HORIZONTAL, -2, 2, 1)
        self.scale.set_value(val)
        self.ask_comment = Gtk.Label("Do you have anything to add ?")

        # Buttons with behaviour
        self.save_button = Gtk.Button(label="Save")
        self.save_button.connect("clicked", self.save)
        self.cancel_button = Gtk.Button(label="Cancel")
        self.cancel_button.connect("clicked", self.cancel)

        # Sets focus on the scale and adds behaviour to scale and edit
        self.scale.grab_focus()
        self.scale.connect("key-press-event", self.on_key_pressed)
        self.edit.connect("key-press-event", self.on_key_pressed)

        # Adds the elements to the grid
        self.add(self.grid)
        self.grid.attach(self.edit, 1, 3, 1, 1)
        self.grid.attach(self.greeting, 1, 0, 1, 1)
        self.grid.attach(self.range_label, 1, 1, 1, 1)
        self.grid.attach(self.scale, 1, 2, 1, 1)
        self.grid.attach(self.ask_comment, 0, 3, 1, 1)
        self.grid.attach(self.cancel_button, 0, 4, 1, 1)
        self.grid.attach(self.save_button, 2, 4, 1, 1)

    def cancel(self, widget): # Closes the popup
        self.close()

    def save(self, widget): # Save the input to the button
        self.btn.give_result(self.scale.get_value(), self.edit.get_text())
        self.close()

    def on_key_pressed(self, widget, ev):
        if ev.keyval == Gdk.KEY_Return: # When enter is pressed
            self.save(None) # No need to add the widget argument
            return
        if ev.keyval == Gdk.KEY_Escape: # When esc is pressed
            self.cancel(None) # No need to add the widget argument
            return

if (__name__ == "__main__"):
    win = ResultPopup()
    win.show_all()
    win.connect("destroy", Gtk.main_quit)
    Gtk.main()
