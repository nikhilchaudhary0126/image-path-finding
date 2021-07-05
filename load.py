from PIL import Image
from pixel import Pixel
import numpy as np

TERRAIN = {
    "Water": (0, 0, 255),
    "Out of bounds": (205, 0, 101)
}


def loadPixels(filename):
    """
    Create a dictionary of Pixel nodes and returns

    :param filename: Terrain file resolution 395x500
    :return: Dictionary of connected land pixels
    """
    im = Image.open(filename)
    rgb_im = im.convert('RGB')
    im.close()
    landPixels = {}
    data = np.zeros((500, 395, 3), dtype=np.uint8)
    for i in range(395):
        for j in range(500):
            rgb = rgb_im.getpixel((i, j))
            data[j, i] = rgb
            # Assuming we cannot pass through water and out of bounds area
            if TERRAIN["Out of bounds"] != rgb and TERRAIN["Water"] != rgb:
                landPixels[(i, j)] = Pixel(i, j, rgb)

    # Connect all land Pixels in 8 coordinate system with each other
    for key in landPixels:
        x, y = key
        if (x - 1, y - 1) in landPixels:
            landPixels[x, y].addNeighbor(landPixels[x - 1, y - 1], 1)
        if (x - 1, y) in landPixels:
            landPixels[x, y].addNeighbor(landPixels[x - 1, y], 1)
        if (x - 1, y + 1) in landPixels:
            landPixels[x, y].addNeighbor(landPixels[x - 1, y + 1], 1)
        if (x, y - 1) in landPixels:
            landPixels[x, y].addNeighbor(landPixels[x, y - 1], 1)
        if (x, y + 1) in landPixels:
            landPixels[x, y].addNeighbor(landPixels[x, y + 1], 1)
        if (x + 1, y - 1) in landPixels:
            landPixels[x, y].addNeighbor(landPixels[x + 1, y - 1], 1)
        if (x + 1, y) in landPixels:
            landPixels[x, y].addNeighbor(landPixels[x + 1, y], 1)
        if (x + 1, y + 1) in landPixels:
            landPixels[x, y].addNeighbor(landPixels[x + 1, y + 1], 1)
    return landPixels, data
