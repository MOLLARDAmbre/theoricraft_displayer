import gi
from row_button import RowButton
from option_button import OptionButton
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import Gdk



class MainWindow(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.connect("destroy", Gtk.main_quit)

        ### Grid setup
        self.grid = Gtk.Grid()
        self.grid.set_column_spacing(10)
        self.grid.set_row_spacing(15)
        self.add(self.grid)

        ### Title and upper options setup
        self.add_offensive_option_label = Gtk.Label("Add an offensive option")
        self.add_defensive_option_label = Gtk.Label("Add a defensive option")
        self.add_offensive_option_edit = Gtk.Entry()
        self.add_defensive_option_edit = Gtk.Entry()
        self.add_defensive_option_confirm = Gtk.Button(label="Confirm")
        self.add_offensive_option_confirm = Gtk.Button(label="Confirm")
        self.add_defensive_option_confirm.connect("clicked", self.add_defensive_option)
        self.add_offensive_option_confirm.connect("clicked", self.add_offensive_option)
        self.offensive_char_label = Gtk.Label("The offensive character")
        self.defensive_char_label = Gtk.Label("The defensive character")
        self.offensive_char = Gtk.ComboBoxText()
        self.defensive_char = Gtk.ComboBoxText()
        fill_combo_box_with_char_names(self.offensive_char)
        fill_combo_box_with_char_names(self.defensive_char)
        self.title_part_situation = Gtk.Label()
        self.title_part_characters = Gtk.Label()
        self.situation_label = Gtk.Label("The current situation")
        self.situation_edit = Gtk.Entry()
        self.situation_edit.set_text("Situation")

        ### Make the title
        self.offensive_char.connect("changed", self.updated_chars)
        self.defensive_char.connect("changed", self.updated_chars)
        self.situation_edit.connect("key-press-event", self.updated_situation)


        ### Fill the window with widgets
        self.grid.attach(self.offensive_char_label, 0, 0, 1, 1)
        self.grid.attach(self.offensive_char, 0, 1, 1, 1)
        self.grid.attach(self.add_offensive_option_label, 0, 3, 1, 1)
        self.grid.attach(self.add_offensive_option_edit, 0, 4, 1, 1)
        self.grid.attach(self.add_offensive_option_confirm, 0, 5, 1, 1)
        self.add_offensive_option_edit.connect("key-press-event", self.confirm_add_offensive_option)

        self.grid.attach(self.defensive_char_label, 2, 0, 1, 1)
        self.grid.attach(self.defensive_char, 2, 1, 1, 1)
        self.grid.attach(self.add_defensive_option_label, 2, 3, 1, 1)
        self.grid.attach(self.add_defensive_option_edit, 2, 4, 1, 1)
        self.grid.attach(self.add_defensive_option_confirm, 2, 5, 1, 1)
        self.add_defensive_option_edit.connect("key-press-event", self.confirm_add_defensive_option)


        self.grid.attach(self.situation_label, 1, 0, 1, 1)
        self.grid.attach(self.situation_edit, 1, 1, 1, 1)
        self.grid.attach(self.title_part_characters, 1, 4, 1, 1)
        self.grid.attach(self.title_part_situation, 1, 5, 1, 1)

        ### Main frame setup
        self.center_grid = Gtk.Grid()
        self.center_grid.set_column_homogeneous(True)
        self.center_grid.set_column_spacing(5)
        self.center_grid.set_row_homogeneous(True)
        self.center_grid.set_row_spacing(5)
        self.table = [[Gtk.Label(self.situation_edit.get_text())]]
        self.current_focus = [0,0]
        self.center_grid.attach(self.table[0][0], 0,0,1,1)
        self.grid.attach(self.center_grid, 1, 6, 1, 1)

    def updated_chars(self, widget):
        try :
            o = self.offensive_char.get_active_text() # offensive char text
            d = self.defensive_char.get_active_text() # defensive char text
            if (len(o) > 0 and len(d) > 0):
                self.title_part_characters.set_text(o + " vs " + d)
        except :
            pass


    def updated_situation(self, widget, ev):
        if ev.keyval == Gdk.KEY_Left:
            self.offensive_char.grab_focus()
        if ev.keyval == Gdk.KEY_Right:
            self.defensive_char.grab_focus()
        self.title_part_situation.set_text(self.situation_edit.get_text())
        self.table[0][0].set_text(self.situation_edit.get_text())

    def confirm_add_offensive_option(self, widget, ev):
        if ev.keyval == Gdk.KEY_Return:
            self.add_offensive_option(widget)

    def confirm_add_defensive_option(self, widget, ev):
        if ev.keyval == Gdk.KEY_Return:
            self.add_defensive_option(widget)


    def add_defensive_option(self, button):
        row_button = RowButton(self.add_defensive_option_edit.get_text(), self, "lig", len(self.table))
        self.table.append([row_button])
        self.center_grid.attach(row_button, 0, len(self.table)-1, 1, 1)
        for i in range(1, len(self.table[0])):
            self.table[-1].append(OptionButton())
            self.center_grid.attach(self.table[-1][i], i, len(self.table)-1, 1, 1)
        self.grid.show_all()
        return

    def add_offensive_option(self, button):
        row_button = RowButton(self.add_offensive_option_edit.get_text(), self, "col", len(self.table[0]))
        self.table[0].append(row_button)
        self.center_grid.attach(row_button, len(self.table[0])-1, 0, 1, 1)
        for i in range(1, len(self.table)):
            self.table[i].append(OptionButton())
            self.center_grid.attach(self.table[i][-1], len(self.table[0])-1, i, 1, 1)
        self.grid.show_all()
        return

    def delete_row(self, orientation, index): #deletes a row or a column based on orientation
        if (orientation == "lig"):
            self.delete_row_row(index)
        else :
            self.delete_row_col(index)

    def delete_row_row(self, index): #Deletes a row
        new_table = [[0 for i in range(len(self.table[0]))] for j in range(len(self.table)-1)]
        for i in range(index):
            for j in range(len(self.table[0])):
                new_table[i][j] = self.table[i][j]
        for i in range(index+1, len(self.table)):
            for j in range(len(self.table[0])):
                new_table[i-1][j] = self.table[i][j]
            try :
                self.table[i][0].desincr_index()
            except :
                pass
        new_table[0][0] = self.table[0][0]
        self.table = new_table
        self.center_grid.remove_row(index)


    def delete_row_col(self, index): # Deletes a column
        new_table = [[0 for i in range(len(self.table[0])-1)] for j in range(len(self.table))]
        for i in range(len(self.table)):
            for j in range(index):
                new_table[i][j] = self.table[i][j]
            for j in range(index+1, len(self.table[0])):
                new_table[i][j-1] = self.table[i][j]

        for j in range(index+1, len(self.table[0])):
            self.table[0][j].desincr_index()
        new_table[0][0] = self.table[0][0]
        self.table = new_table
        self.center_grid.remove_column(index)



def fill_combo_box_with_char_names(cb):
    cb.append_text("Mario")
    cb.append_text("Donkey Kong")
    cb.append_text("Link")
    cb.append_text("Samus")
    cb.append_text("Dark Samus")
    cb.append_text("Yoshi")
    cb.append_text("Kirby")
    cb.append_text("Fox")
    cb.append_text("Pikachu")
    cb.append_text("Luigi")
    cb.append_text("Ness")
    cb.append_text("Captain Falcon")
    cb.append_text("Jigglypuff")
    cb.append_text("Peach")
    cb.append_text("Daisy")
    cb.append_text("Bowser")
    cb.append_text("Ice Climbers")
    cb.append_text("Sheik")
    cb.append_text("Zelda")
    cb.append_text("Dr Mario")
    cb.append_text("Pichu")
    cb.append_text("Falco")
    cb.append_text("Marth")
    cb.append_text("Lucina")
    cb.append_text("Young Link")
    cb.append_text("Ganondorf")
    cb.append_text("Mewtwo")
    cb.append_text("Roy")
    cb.append_text("Chrom")
    cb.append_text("Mr Game and Watch")
    cb.append_text("Meta Kgnight")
    cb.append_text("Pit")
    cb.append_text("Dark Pit")
    cb.append_text("Zero Suit Samus")
    cb.append_text("Wario")
    cb.append_text("Snake")
    cb.append_text("Ike")
    cb.append_text("Pokemon Trainer")
    cb.append_text("Diddy Kong")
    cb.append_text("Lucas")
    cb.append_text("Sonic")
    cb.append_text("King DeDeDe")
    cb.append_text("Olimar")
    cb.append_text("Lucario")
    cb.append_text("R.O.B.")
    cb.append_text("Toon Link")
    cb.append_text("Wolf")
    cb.append_text("Villager")
    cb.append_text("Megaman")
    cb.append_text("Wii Fit Trainer")
    cb.append_text("Rosalina and Luma")
    cb.append_text("Little Mac")
    cb.append_text("Greninja")
    cb.append_text("Palutena")
    cb.append_text("Pac-Man")
    cb.append_text("Robin")
    cb.append_text("Shulk")
    cb.append_text("Bowser Jr")
    cb.append_text("Duo Duck Hunt")
    cb.append_text("Ryu")
    cb.append_text("Ken")
    cb.append_text("Cloud")
    cb.append_text("Corrin")
    cb.append_text("Bayonetta")
    cb.append_text("Inkling")
    cb.append_text("Ridley")
    cb.append_text("Simon")
    cb.append_text("Richter")
    cb.append_text("King K. Rool")
    cb.append_text("Isabelle")
    cb.append_text("Incineroar")
    cb.append_text("Piranha Plant")
    cb.append_text("Joker")
    cb.append_text("Hero")
    cb.append_text("Banjo & Kazooie")
    cb.append_text("Terry")
    cb.append_text("Byleth")
    cb.append_text("Mii Brawler")
    cb.append_text("Mii Swordfighter")
    cb.append_text("Mii Gunner")
    cb.append_text("Generic")

if (__name__ == "__main__"):
    win = MainWindow()
    win.show_all()
    Gtk.main()
