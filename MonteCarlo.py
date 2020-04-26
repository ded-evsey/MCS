from general import Axes, Point
from random import uniform


class MonteCarlo(Axes):
    def __init__(self, points, count_points):
        super().__init__(points)
        self.points_figure = []
        self.points_all = [self.random_point for _ in range(count_points)]
        self.point_size = self.get_point_size

    @property
    def get_point_size(self):
        return self.square_plate / len(self.points_all) * 100

    @property
    def random_point(self):
        min_point, max_point = self.plate
        return Point(
            uniform(min_point.x - 1, max_point.x + 1),
            uniform(min_point.y - 1, max_point.y + 1)
        )

    def calc(self):
        for point in self.points_all:
            if self.in_figure(point):
                self.add_point(point, color='green', size=self.point_size * 2)
                self.points_figure.append(point)
            else:
                self.add_point(point, color='red', size=self.point_size)
        return self

    @property
    def square(self):
        return self.square_plate * len(self.points_figure) / len(self.points_all)
