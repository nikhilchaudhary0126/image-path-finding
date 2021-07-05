"""
file: run.py
description:
This program finds a path between pixels provided in path file.

language: python3
"""

# imports
from load import loadPixels
import cv2


def start():
    landPixels, data = loadPixels("terrain.png")
    target = []
    with open("path", "r") as path:
        for line in path.readlines():
            target.append((line.split()))
    if len(target) > 1:
        for i in range(len(target) - 1):
            xSource, ySource = int(target[i][0]), int(target[i][1])
            xDestination, yDestination = int(target[i + 1][0]), int(target[i + 1][1])
            dfs(landPixels[(xSource, ySource)], landPixels[(xDestination, yDestination)], data)


def dfs(start, end, data):
    """
    Iterative method to find a path, if one exists from current to end vertex
    :param start:       source vertex in image
    :param end:         destination vertex in image
    :param data:        numpy data for image display
    :return:            list of visited vertices else None
    """

    stack, path = [start], []

    while stack:
        vertex = stack.pop()
        if vertex in path:
            continue
        if vertex == end:
            return path
        data[vertex.y, vertex.x] = [191, 255, 0]
        RGB_img = cv2.cvtColor(data, cv2.COLOR_BGR2RGB)
        cv2.imshow('image', RGB_img)
        cv2.waitKey(1)
        path.append(vertex)
        for neighbor in vertex.getNeighbors():
            stack.append(neighbor)
    return None


if __name__ == '__main__':
    start()
