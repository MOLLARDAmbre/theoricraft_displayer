import gi
from row_button import RowButton
from option_button import OptionButton
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

def save():
    saver = Gtk.FileChooser()
    saver.set_action(GTK_FILE_CHOOSER_ACTION_SAVE)
