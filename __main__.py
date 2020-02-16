from MonteCarlo import MonteCarlo
from general import *

if __name__ == '__main__':
    print('Enter count points in figure')
    count_points = int(input())
    points = []
    for i in range(count_points):
        print(f'Enter (x, y) for {i} point')
        x, y = input().replace('(', '').replace(')', '').split(',')
        points.append(Point(int(x), int(y)))

    print(points[0].x, points[0].y)
    max_dice_rolls = 10000
    min_dice_rolls = 1000
    print(f'Enter the number of "dice rolls"(not less {min_dice_rolls}, but no more {max_dice_rolls})')
    dice_rolls = int(input())
    if dice_rolls < min_dice_rolls:
        print(f'The number of dice rolls entered is less than {min_dice_rolls},')
        print(f'so there will be a minimum number({min_dice_rolls})')
        dice_rolls = min_dice_rolls
    else:
        print(f'The number of dice rolls entered is more than {max_dice_rolls},')
        print(f'so there will be a maximum number({max_dice_rolls})')
        dice_rolls = max_dice_rolls

    monte_carlo = MonteCarlo(points=points, count_points=dice_rolls)
    monte_carlo.add_figure()
    monte_carlo.calc()
    monte_carlo.show()
    print(monte_carlo.square)

