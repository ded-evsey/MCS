import pylab
from random import randrange
from matplotlib.patches import Polygon


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class Figure(Point):
    def __init__(self):
        super().__init__()
        self.points = None

    def get_points(self, index):
        return self.points[index]

    def set_points(self, points=None):
        if not points or len(points) < 5:
            raise ValueError('Too few points. Need more than 5 points.')
        self.points = points

    @property
    def last(self):
        return self.points[-1]

    @property
    def first(self):
        return self.points[0]

    @property
    def plate(self):
        list_x = [point.x for point in self.points]
        list_y = [point.y for point in self.points]
        return Point(min(list_x), min(list_y)), Point(max(list_x), max(list_y))

    def random_point(self):
        max_point, min_point = self.plate
        return Point(randrange(min_point.x, max_point.x), randrange(min_point.y, max_point.x))


class Axes(Figure, pylab):
    def __init__(self):
        super().__init__()
        self.axes = None

    def set_axes(self):
        max_point, min_point = self.plate
        pylab.xlim(min_point.x, max_point.x)
        pylab.ylim(min_point.y, max_point.y)
        pylab.grid()
        self.axes = pylab.gca()

    def add_figure(self):
        self.axes.add_patch(Polygon(self.points))

    def add_point(self, point, color, size):
        self.axes.scatter(point.x, point.y, c=color, s=size)
