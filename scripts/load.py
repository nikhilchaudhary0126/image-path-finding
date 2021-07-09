import cv2
from PIL import Image
from classes.Pixel import Pixel
import numpy as np

TERRAIN = {
    "Water": (0, 0, 255),
    "Out of bounds": (205, 0, 101)
}


def loadPixels(filename: str) -> (dict, np.ndarray):
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


def showImage(data: np.ndarray, x: int, y: int) -> None:
    """
    Shows OpevCV image of a numpy array
    :param data: numpy array
    :param x:   xCoordinate
    :param y:   yCoordinate
    :return: None
    """
    data[x, y] = [191, 255, 0]  # Update numpy pixel
    RGB_img = cv2.cvtColor(data, cv2.COLOR_BGR2RGB)  # Covert to RGB
    cv2.imshow('image', RGB_img)
    cv2.waitKey(1)
