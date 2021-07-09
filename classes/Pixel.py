class Pixel:
    __slots__ = "x", "y", "rgb", "elevation", "connectedTo"

    def __init__(self, x: int, y: int, rgb, elevation=0):
        """
        Constructor to initialize pixel object

        :param x:           X Coordinate
        :param y:           Y Coordinate
        :param elevation:   Elevation of pixel
        :param rgb:         RGB color of pixel
        """
        self.x = x
        self.y = y
        self.rgb = rgb
        self.elevation = elevation
        self.connectedTo = dict()

    def addNeighbor(self, nbr, cost: int):
        """
        Adds a neighbor to a pixel; 8 coordinate system assumed
        :param nbr:     neighboring pixel
        :param cost:    distance from one pixel to another
        :return:        None
        """
        self.connectedTo[nbr] = cost

    def getCost(self, nbr):
        """
        Compute weight
        :param nbr:     neighboring pixel
        :return:        cost of traveling to another neighbor
        """
        return self.connectedTo[nbr]

    def getNeighbors(self):
        """
        :return:    Connected Neighbors
        """
        return self.connectedTo.keys()

    def __str__(self):
        """
        :return:    String representation of Pixel
        """
        return "Pixel:(" + str(self.x) + "," + str(self.y) + ")"
