from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import option_button
import numpy as np


def save(path, table):
    from os import chdir
    chdir("theoricraft_displayer")
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


    im.save(path)
