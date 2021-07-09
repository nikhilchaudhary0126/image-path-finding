"""
file: run.py
description:
This program finds a path between pixels provided in path file.

language: python3
"""

# imports
from collections import defaultdict
from queue import PriorityQueue
from math import sqrt, pow
from classes.PixelPriority import PixelPriority
from scripts.load import *
from classes.Pixel import *


def st(imagleFile: str, algorithm: str) -> None:
    landPixels, data = loadPixels(imagleFile)
    target = []
    with open("path", "r") as path:
        for line in path.readlines():
            target.append((line.split()))
    if len(target) > 1:
        for i in range(len(target) - 1):
            xSource, ySource = int(target[i][0]), int(target[i][1])
            xDestination, yDestination = int(target[i + 1][0]), int(target[i + 1][1])
            if algorithm == "dfs":
                path = dfs(landPixels[(xSource, ySource)], landPixels[(xDestination, yDestination)], data)
            elif algorithm == "bfs":
                path = bfs(landPixels[(xSource, ySource)], landPixels[(xDestination, yDestination)], data)
            elif algorithm == "ucs":
                path = ucs(landPixels[(xSource, ySource)], landPixels[(xDestination, yDestination)], data)
            elif algorithm == "astar":
                path = astar(landPixels[(xSource, ySource)], landPixels[(xDestination, yDestination)], data)
            if path:
                [print(x) for x in path]


def bfs(st: Pixel, end: Pixel, data: np.ndarray):
    """
    Iterative method to find a bfs path, if one exists from current to end vertex
    :param st:       source vertex in image
    :param end:         destination vertex in image
    :param data:        numpy data for image display
    :return:            shortest path else None
    """
    queue = [st]
    predecessors = defaultdict(lambda: None)
    predecessors[st] = -1

    while queue:
        current = queue.pop(0)
        if current == end:
            break
        for neighbor in current.getNeighbors():  # Traverse nodes
            if predecessors[neighbor] is None:
                showImage(data, neighbor.y, neighbor.x)
                predecessors[neighbor] = current
                queue.append(neighbor)

    if predecessors[end] is not None:  # Backtrack to find st node
        path = []
        current = end
        while current != st:
            path.insert(0, current)
            current = predecessors[current]
        path.insert(0, st)
        return path
    else:
        return None


def dfs(st: Pixel, end: Pixel, data: np.ndarray):
    """
    Iterative method to find a dfs path, if one exists from current to end vertex
    :param st:       source vertex in image
    :param end:         destination vertex in image
    :param data:        numpy data for image display
    :return:            list of visited vertices else None
    """

    stack, path = [st], []

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


def ucs(st: Pixel, end: Pixel, data: np.ndarray):
    """
    Iterative method to find a Dijkstra path, if one exists from current to end vertex
    :param startKey:        start pixel point key
    :param endKey:          end pixel point key
    :return:                path
    """
    q = PriorityQueue()
    startPriorityPixel = PixelPriority(st, 0, 0)  # start priority pixel with 0 priority
    q.put((0, startPriorityPixel))

    lowest = startPriorityPixel
    visited = dict()
    while lowest.pxl != end:
        if q.empty():  # No way to get to end
            return [], -1
        thisDistace = lowest.distance
        for u in lowest.pxl.getNeighbors():
            if u is not None and (u.x, u.y) not in visited:
                showImage(data, u.y, u.x)
                visited[(u.x, u.y)] = 1
                # distance travelled from start pixel to current pixel
                dist = sqrt(pow(u.x - lowest.pxl.x, 2) + pow(u.y - lowest.pxl.y, 2) + \
                            pow(u.elevation - lowest.pxl.elevation, 2))
                newDistance = thisDistace + dist
                priority = newDistance
                priorityPixel = PixelPriority(u, newDistance, priority)
                priorityPixel.predecessor = lowest
                q.put((priority, priorityPixel))

        lowest = q.get()[1]
    path = []
    if lowest.distance != 0:  # We found the end, but it never got connected.
        lst = lowest
        while lst is not None:
            path.insert(0, lst.pxl)
            lst = lst.predecessor
    return path


def astar(st: Pixel, end: Pixel, data: np.ndarray):
    """
    Compute the path through the graph from st to end vertex whose sum of edge weights is minimized
    :param startKey:        start pixel point key
    :param endKey:          end pixel point key
    :return:                path
    """
    q = PriorityQueue()
    startPriorityPixel = PixelPriority(st, 0, 0)  # start priority pixel with 0 priority
    q.put((0, startPriorityPixel))

    lowest = startPriorityPixel
    visited = dict()
    while lowest.pxl != end:
        if q.empty():  # No way to get to end
            return [], -1
        thisDistace = lowest.distance
        for u in lowest.pxl.getNeighbors():
            if u is not None and (u.x, u.y) not in visited:
                showImage(data, u.y, u.x)
                visited[(u.x, u.y)] = 1
                # heuristic function computed by calculating min. distance from end
                heuristic = sqrt(pow(u.x - end.x, 2) + pow(u.y - end.y, 2) + pow(u.elevation - end.elevation, 2))
                # distance travelled from start pixel to current pixel
                dist = sqrt(pow(u.x - lowest.pxl.x, 2) + pow(u.y - lowest.pxl.y, 2) + \
                            pow(u.elevation - lowest.pxl.elevation, 2))
                newDistance = thisDistace + dist
                priority = lowest.pxl.getCost(u) + heuristic
                priorityPixel = PixelPriority(u, newDistance, priority)
                priorityPixel.predecessor = lowest
                q.put((priority, priorityPixel))

        lowest = q.get()[1]
    path = []
    if lowest.distance != 0:  # found the end, but it never got connected
        lst = lowest
        while lst is not None:
            path.insert(0, lst.pxl)
            lst = lst.predecessor
    return path


if __name__ == '__main__':
    st("terrain.png", "dfs")
