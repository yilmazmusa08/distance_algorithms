import numpy as np

# define the cosine fundtion
cosine = lambda v1, v2: np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

# define lists
list1 = [10, 20, 10, 20, 30, 40, 50, 60, 70, 80, 30, 40, 50, 60, 80, 90]
list2 = [20, 50, 0, 75, 80, 90, 10, 90, 10, 20, 30, 50, 60, 70, 80, 90]

# print the result
print(cosine(list1, list2))