from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import option_button
import numpy as np


class ImageGenerator():
    def __init__(self, table):
        self.x = len(table[0])
        self.y = len(table)
        self.hor_size = 0
        self.vert_size = 0
        self.table = table
        self.font = ImageFont.truetype('damase.ttf', 12)

    def calculate_sizes(self):
        max_x_size = 0
        max_y_size = 0
        for i in range(len(self.table)):
            for j in range(len(self.table[0])):
                x_size, y_size = self.font.getsize(self.table[i][j].get_text())
                if (x_size > max_x_size):
                    max_x_size = x_size
                if (y_size > max_y_size):
                    max_y_size = y_size
        max_x_size += 20 # Left and right margins
        max_y_size += 20 # same

        self.hor_size = max_x_size
        self.vert_size = max_y_size

    def generate_base(self): # generates the image with the specific size, not adding colors, grid or labels yet
        im = [[[255,255,255] for i in range(self.x*self.hor_size)] for j in range(self.y*self.vert_size)]
        return im

    def color_rect(self, im, top, left, bottom, right, color): # colors the rectangle witht he specified color
        for k in range(left, right):
            for l in range(top, bottom):
                im[l][k] = color
        return im

    def add_colors(self, im): # Adds the colors to the image
        for i in range(self.x):
            for j in range(self.y):
                try :
                    col = self.table[j][i].get_color_array()
                except :
                    col = [255,255,255] #if there is no color for the cell (eg label cells), we use white
                left = self.hor_size * i
                right = self.hor_size * (i+1)
                top = self.vert_size * j
                bot = self.vert_size * (j+1)
                self.color_rect(im, top, left, bot, right, col)
        return im

    def draw_vert_line(self, im, index):
        for k in range(len(im)):
            im[k][index] = [0,0,0]
        return im

    def draw_hor_line(self, im, index):
        for k in range(len(im[0])):
            im[index][k] = [0,0,0]
        return im

    def add_grid(self, im): # Adds the grid to the generated image
        for i in range(1, self.x):
            self.draw_vert_line(im, i*self.hor_size)
        for i in range(1, self.y):
            self.draw_hor_line(im, i*self.vert_size)
        return im

    def convert_into_PIL(self, im): # Converts the arrey into a PIL image
        return Image.fromarray(np.array(im, dtype=np.uint8))

    def add_labels(self, im): # Adds the labels
        draw = ImageDraw.Draw(im)
        for i in range(self.x):
            for j in range(self.y):
                try :
                    text = self.table[j][i].get_text()
                    if (text != "Result unknown"):
                        draw.text((i*self.hor_size + 10, j*self.vert_size + 10), self.table[j][i].get_text(), (0,0,0))
                except :
                    print((i*self.hor_size + 10, j*self.vert_size + 10))
        return im




def save(path, table):
    """
    from os import chdir, getcwd
    #chdir("~/theoricraft_displayer")
    width = len(table[0])*100
    height = len(table)*100
    im = [[0 for j in range(width)] for i in range(height)]
    for i in range(len(table[0])):
        for j in range(len(table)):
            for k in range(100):
                for l in range(100):
                    try :
                        im[100*j+k][100*i+l] = table[j][i].get_color_array()
                    except :
                        im[100*j+k][100*i+l] = [255,255,255]

    im = Image.fromarray(np.array(im, dtype=np.uint8))

    draw = ImageDraw.Draw(im)

    for i in range(len(table[0])):
        for j in range(len(table)):
            try :
                draw.text((100*j,100*i+50), table[j][i].get_text(), (0,0,0))
            except :
                pass

    """
    im = ImageGenerator(table)
    path = "test.jpg"
    im.calculate_sizes()
    image = im.generate_base()
    image = im.add_colors(image)
    image = im.add_grid(image)
    image = im.convert_into_PIL(image)
    image = im.add_labels(image)
    image.save(path)
