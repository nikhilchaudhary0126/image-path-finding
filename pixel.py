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


class PixelPriority:
    """
    Class used for defining pixel priority while covering paths
    """
    __slots__ = "pxl", "predecessor", "distance", "priority"

    def __init__(self, pixel, distance, priority):
        """
        Initialize a priority pixel with below properties

        :param pixel:       Pixel Object
        :param distance:    distance travelled to reach this object from start Pixel
        :param priority:    Priority of the pixel object
        """
        self.pxl = pixel
        self.predecessor = None
        self.distance = distance
        self.priority = priority

    def __lt__(self, other):
        """
        Comparator for comparison of priority objects
        :param other:   Other PixelPriority object
        :return:        PixelPriority object with less priority
        """
        return self.priority < other.priority
