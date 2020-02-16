def check_points_count(points):
    if len(points) < 5:
        raise ValueError('Too few points. Need more than 5 points.')
    return points
