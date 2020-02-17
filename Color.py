import gi
import Color
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import Gdk

# Color for the worst result
worst_r = 1
worst_g = 128/255
worst_b = 128/255

#Color for the best result
best_r = 128/255
best_g = 1
best_b = 170/255

def get_color(value):
    val = value + 2 # the min goes from -2 to 0
    r = (val * best_r + (5-val) * worst_r)/5
    g = (val * best_g + (5-val) * worst_g)/5
    b = (val * best_b + (5-val) * worst_b)/5
    return Gdk.RGBA(r, g, b, 0.8)

def get_color_array(value):
    val = value + 2 # the min goes from -2 to 0
    r = (val * best_r + (5-val) * worst_r)/5
    g = (val * best_g + (5-val) * worst_g)/5
    b = (val * best_b + (5-val) * worst_b)/5
    return [255*r, 255*g, 255*b]
