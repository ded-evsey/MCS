from general import Axes, Point
from random import randrange


class MonteCarlo(Axes):
    def __init__(self, points, count_points):
        super().__init__(points)
        self.points_figure = []
        self.points_all = [self.random_point for item in range(count_points)]
        self.point_size = self.get_point_size

    @property
    def get_point_size(self):
        return self.square_plate / len(self.points_all)

    @property
    def random_point(self):
        max_point, min_point = self.plate
        return Point(randrange(min_point.x, max_point.x), randrange(min_point.y, max_point.x))

    def calc(self):
        for point in self.points_all:
            if point in self.points:
                self.add_point(point, color='green', size=self.point_size)
            else:
                self.add_point(point, color='red', size=self.point_size)
