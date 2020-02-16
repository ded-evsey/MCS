from random import randrange


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class Figure:
    def __init__(self, points=None):
        if points is None:
            points = [Point()]
        if len(points) < 5:
            raise ValueError('Too few points. Need more than 5 points.')
        self.points = points
        self.faces = points.uppend()

    def get(self, index):
        return self.points[index]

    def last(self):
        return self.points[-1]

    def first(self):
        return self.points[0]

    def random_point(self):
        list_x = [point.x for point in self.points]
        list_y = [point.y for point in self.points]

        return Point(randrange(min(list_x), max(list_x)), randrange(min(list_y), max(list_y)))

    def draw(self):
        pass

    def calc(self):
        pass


class MonteCarlo(Figure):
    def calc(self):
        return
