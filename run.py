"""
file: run.py
description:
This program finds a path between pixels provided in path file.

language: python3
"""

# imports
from collections import defaultdict
from load import *


def start():
    landPixels, data = loadPixels("terrain.png")
    pathFindingAlgorithm, path = "dfs", None
    target = []
    with open("path", "r") as path:
        for line in path.readlines():
            target.append((line.split()))
    if len(target) > 1:
        for i in range(len(target) - 1):
            xSource, ySource = int(target[i][0]), int(target[i][1])
            xDestination, yDestination = int(target[i + 1][0]), int(target[i + 1][1])
            if pathFindingAlgorithm == "dfs":
                path = dfs(landPixels[(xSource, ySource)], landPixels[(xDestination, yDestination)], data)
            if pathFindingAlgorithm == "bfs":
                path = bfs(landPixels[(xSource, ySource)], landPixels[(xDestination, yDestination)], data)
            if path:
                [print(x) for x in path]


def ucs(start, end, data):
    pass


def bfs(start, end, data):
    """
    Iterative method to find a bfs path, if one exists from current to end vertex
    :param start:       source vertex in image
    :param end:         destination vertex in image
    :param data:        numpy data for image display
    :return:            shortest path else None
    """
    queue = [start]
    predecessors = defaultdict(lambda: None)
    predecessors[start] = -1

    while queue:
        current = queue.pop(0)
        if current == end:
            break
        for neighbor in current.getNeighbors(): # Traverse nodes
            if predecessors[neighbor] is None:
                showImage(data, neighbor.y, neighbor.x)
                predecessors[neighbor] = current
                queue.append(neighbor)

    if predecessors[end] is not None:   # Backtrack to find start node
        path = []
        current = end
        while current != start:
            path.insert(0, current)
            current = predecessors[current]
        path.insert(0, start)
        return path
    else:
        return None


def dfs(start, end, data):
    """
    Iterative method to find a dfs path, if one exists from current to end vertex
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
        showImage(data, vertex.y, vertex.x)
        path.append(vertex)
        for neighbor in vertex.getNeighbors():
            stack.append(neighbor)
    return None


if __name__ == '__main__':
    start()
