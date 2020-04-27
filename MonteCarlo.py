from general import Axes, Point
from random import uniform


class MonteCarlo(Axes):
    def __init__(self, points, count_points):
        """
        Класс метод
        :param points: точки фигуры
        :param count_points: количество бросков кубика
        """
        super().__init__(points)
        self.points_figure = []
        self.points_all = [self.random_point for _ in range(count_points)]
        self.point_size = self.get_point_size

    @property
    def get_point_size(self):
        """
         вычисление Размера точки(нужен для отображения)
        :return: размер точки
        """
        return self.square_plate / len(self.points_all) * 100

    @property
    def random_point(self):
        """
        Метод получения случайно точки принадлежащей поверхности
        :return: Случайная точка
        """
        min_point, max_point = self.plate
        return Point(
            uniform(min_point.x, max_point.x),
            uniform(min_point.y, max_point.y)
        )

    def calc(self):
        """
        Метод посчета точек попавших в фигуру
        :return:
        """
        for point in self.points_all:
            if self.in_figure(point):
                self.add_point(point, color='green', size=self.point_size * 2)
                self.points_figure.append(point)
            else:
                self.add_point(point, color='red', size=self.point_size)
        return self

    @property
    def square(self):
        """
        вычисление площади
        :return: плащадь
        """
        return self.square_plate * len(self.points_figure) / len(self.points_all)
