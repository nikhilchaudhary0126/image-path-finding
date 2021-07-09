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