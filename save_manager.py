import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import numpy as np

def table_to_array(table): # Converts the table into an array we can easily save
    arr = np.array(table)
    for i in range(len(table)):
        for j in range(len(table[0])):
            if (i == 0 and j == 0):
                arr[i][j] = table[i][j].get_text()
            else :
                arr[i][j] = table[i][j].to_save()
    return arr


def load_parent_with_table(parent, table): # Updates parent's table properly from the new table
    for i in range(len(parent.table)):
        parent.center_grid.remove_row(0)

    new_table = [[Gtk.Label(table[0][0])]]
    parent.table = new_table
    for line in range(1, len(table)):
        parent.add_defensive_option_auto(table[line][0])
    for col in range(1, len(table[0])):
        parent.add_offensive_option_auto(table[0][col])
    for i in range(1, len(table)):
        for j in range(1, len(table[0])):
            parent.table[i][j].give_result(table[i][j], "")
    parent.grid.show_all()
    pass


def save(parent, table, default_path): # Saves the table containing everything
    dialog = Gtk.FileChooserDialog("Please choose a file", parent,
        Gtk.FileChooserAction.SAVE,
        (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
        Gtk.STOCK_OPEN, Gtk.ResponseType.OK))
    dialog.set_current_name(default_path)
    response = dialog.run()
    if response == Gtk.ResponseType.OK:
        np.save(dialog.get_filename()+".npy", table_to_array(table), allow_pickle=True)
    elif response == Gtk.ResponseType.CANCEL:
        pass
    dialog.destroy()
    return


def load(parent): # Loads the table from file
    dialog = Gtk.FileChooserDialog("Please select a file", parent,
        Gtk.FileChooserAction.OPEN,
        (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
        Gtk.STOCK_OPEN, Gtk.ResponseType.OK))
    filter = Gtk.FileFilter()
    filter.set_name("Theoricraft displayer files or other npy files")
    filter.add_pattern("*.npy")
    dialog.add_filter(filter)
    response = dialog.run()
    if (response == Gtk.ResponseType.OK) :
        table = np.load(dialog.get_filename(), allow_pickle=True)
        load_parent_with_table(parent, table)
    elif response == Gtk.ResponseType.CANCEL:
        pass
    dialog.destroy()
    return
