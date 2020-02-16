from matplotlib import pylab
from matplotlib.patches import Polygon
from errors import check_points_count


class Point:
    def __init__(self, x=0, y=0, size=None):
        self.x = x
        self.y = y
        self.size = size

    def __lt__(self, other):
        if self.x < other.x or self.y < other.y:
            return True
        return False

    def __str__(self):
        return f'x = {self.x}, y = {self.y}'


class Figure(Point):
    def __init__(self, points):
        super().__init__()
        self.points = check_points_count(points)

    def get_points(self, index):
        return self.points[index]

    def __contains__(self, point):
        flag = 0
        check_x = point.x
        check_y = point.y
        for i in range(len(self.points)):
            cur_x = self.points[i].x
            cur_y = self.points[i].y
            prev_x = self.points[i-1].x
            prev_y = self.points[i-1].y
            if(
                (
                    (cur_y <= check_y < prev_y) or
                    (prev_y <= check_y < cur_y)
                ) and
                (
                    check_x > (prev_x - cur_x) * (check_y - cur_y) / (prev_y - cur_y) + cur_x
                )
            ):
                flag = 1 - flag
        return flag

    @property
    def plate(self):
        list_x = [point.x for point in self.points]
        list_y = [point.y for point in self.points]
        return Point(min(list_x), min(list_y)), Point(max(list_x), max(list_y))

    @property
    def square_plate(self):
        point_min, point_max = self.plate
        return (point_max.x - point_min.x) * (point_max.y - point_min.y)


class Axes(Figure):
    def __init__(self, points):
        super().__init__(points)
        self.axes = self.set_axes

    @property
    def set_axes(self):
        max_point, min_point = self.plate
        pylab.xlim(min_point.x - 1, max_point.x + 1)
        pylab.ylim(min_point.y - 1, max_point.y + 1)
        pylab.grid()
        return pylab.gca()

    def add_figure(self):
        self.axes.add_patch(Polygon(self.points))

    def add_point(self, point, size=100, color='blue'):
        self.axes.scatter(point.x, point.y, c=color, s=size)

    def show(self):
        self.set_axes.show()
