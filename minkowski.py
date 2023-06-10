import math

def minkowski_distance(point1, point2, p):
    """Calculate the Minkowski distance between two points."""
    distance = 0
    n = len(point1)
    
    for i in range(n):
        distance += abs(point1[i] - point2[i]) ** p
    
    distance = distance ** (1/p)
    return distance

# Example usage
point1 = [1, 2, 3]
point2 = [4, 5, 6]
p = 2

minkowski_dist = minkowski_distance(point1, point2, p)
print(f"Minkowski distance: {minkowski_dist}")
