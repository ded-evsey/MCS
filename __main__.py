from MonteCarlo import MonteCarlo
from general import *
import numpy as np

if __name__ == '__main__':
    print('Enter count points in figure')
    count_points = int(input())
    points = []
    for i in range(count_points):
        print(f'Enter (x, y) for {i} point')
        x, y = input().replace('(', '').replace(')', '').split(',')
        points.append(Point(float(x), float(y)))
    # оперделение количества точек, а так же заведение точек фигуры
    max_dice_rolls = 10000
    min_dice_rolls = 1000
    print(f'Enter the number of "dice rolls"(not less {min_dice_rolls}, but no more {max_dice_rolls})')
    dice_rolls = int(input())
    if dice_rolls < min_dice_rolls:
        print(f'The number of dice rolls entered is less than {min_dice_rolls},')
        print(f'so there will be a minimum number({min_dice_rolls})')
        dice_rolls = min_dice_rolls
    elif max_dice_rolls < dice_rolls:
        print(f'The number of dice rolls entered is more than {max_dice_rolls},')
        print(f'so there will be a maximum number({max_dice_rolls})')
        dice_rolls = max_dice_rolls
    else:
        dice_rolls = dice_rolls
    # заведение количества попыток
    # нижний порог существует, что бы вычисления имели хоть какой то смысл
    # верхний, что бы ограничить жадность пользователя и не насиловать комп
    monte_carlo = MonteCarlo(points=points, count_points=dice_rolls)  # Инициализация класса Монте Карло
    monte_carlo = monte_carlo.add_figure()  # Добавление фигуры на поверхность
    monte_carlo = monte_carlo.calc()  # Подсчет точек, попавших в границы фигуры
    monte_carlo = monte_carlo.show()  # Отображение результата
    """
        Эстетическое отображение результатов подсчета площади,
        а так же матожидания и дисперсии
    """
    print(f'The area of the figure calculated by the Monte Carlo method = {monte_carlo.square}')
    print(f'dispersion X = {np.var([item.x for item in monte_carlo.points_all])}')
    print(f'dispersion Y = {np.var([item.y for item in monte_carlo.points_all])}')
    print(f'expectation X = {np.mean([item.x for item in monte_carlo.points_all])}')
    print(f'expectation Y = {np.mean([item.y for item in monte_carlo.points_all])}')
