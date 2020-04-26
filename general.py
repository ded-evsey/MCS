from matplotlib import pylab
from matplotlib.patches import Polygon
from errors import check_points_count


class Point:
    def __init__(self, x=0, y=0, size=None):
        """
        Класс Точки
        :param x: координата Х
        :param y: координата У
        :param size: размер точки(нужен для отображения и вычисления площади, считается отдельно)
        """
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
        """
        Класс Фигуры
        :param points: точки образующие фигуру
        """
        super().__init__()
        self.points = check_points_count(points)

    def in_figure(self, point):
        """
        Метод определяющий принадлежит ли точка фигуре
        :param point: определяемая точка
        :return: да/нет
        """
        flag = False  #
        for i, cur_point in enumerate(self.points):  #
            prev_point = self.points[i-1]  #
            # далее происходит магия математики об определении принадлежности точки к фигуре
            # лучше почитай вот тут
            # https://habr.com/ru/post/128438/ Принадлежность точки полигону
            if (
                (
                    (
                        cur_point.y > point.y
                    ) != (
                        prev_point.y > point.y
                    )
                ) and (
                    point.x < (
                        prev_point.x - cur_point.x
                    ) * (
                        point.y - cur_point.y
                    ) / (
                        prev_point.y - cur_point.y
                    ) + cur_point.x
                )
            ):
                flag = not flag
        return flag

    @property
    def plate(self):
        """
        Разметка поверхности, а так же поиск масимальной и минимальной точки фигуры
        :return: максимальная и минимальная точка относительно фигуры
        """
        list_x = [point.x for point in self.points]
        list_y = [point.y for point in self.points]
        return Point(min(list_x), min(list_y)), Point(max(list_x), max(list_y))

    @property
    def square_plate(self):
        """
        Площадь выделенной площадки
        :return: Площадь
        """
        point_min, point_max = self.plate
        return (point_max.x - point_min.x) * (point_max.y - point_min.y)

    @property
    def clear_points(self):
        return [(item.x, item.y) for item in self.points]


class Axes(Figure):
    def __init__(self, points):
        """
        Поверхность на которой размещаются точки
        :param points:
        """
        super().__init__(points)
        self.axes = self.set_axes

    @property
    def set_axes(self):
        """
        Уставновка отображаемой поверхности
        :return: поверхность для отображения
        """
        min_point, max_point = self.plate
        pylab.xlim(min_point.x - 1, max_point.x + 1)
        pylab.ylim(min_point.y - 1, max_point.y + 1)
        pylab.grid()
        return pylab.gca()

    def add_figure(self):
        """
        Добавление фигуры на поверхность
        :return:
        """
        self.axes.add_patch(
            Polygon(
                self.clear_points,
                edgecolor='black',
                facecolor='none'
            )
        )
        return self

    def add_point(self, point, size=100, color='blue'):
        """
        добавление точки на поверхность
        :param point: добавляемая точка
        :param size: размер точки
        :param color: цвет
        :return: объект класса
        """
        self.axes.scatter(point.x, point.y, c=color, s=size)
        return self

    def show(self):
        """
        переопределение отображения
        :return:
        """
        pylab.show()
        return self
