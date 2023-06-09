def manhattan_distance(point1, point2):
    """
    Calculates the Manhattan distance between two points in a 2D grid.
    Each point should be a tuple (x, y) representing the coordinates.
    """
    x1, y1 = point1
    x2, y2 = point2
    distance = abs(x1 - x2) + abs(y1 - y2)
    return distance

# Example usage
point_a = (3, 5)
point_b = (1, 9)
distance = manhattan_distance(point_a, point_b)
print(f"The Manhattan distance between {point_a} and {point_b} is: {distance}")
