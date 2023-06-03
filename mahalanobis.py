import scipy as stats
from scipy.stats import chi2
import math
import numpy as np

liste_1 = [2, 4, 5, 6, 24, 15]
liste_2 = [3, 7, 3, 5, 24, 10]

def std( item:list ) -> float:
    distance = 0
    avg = sum(item) / len(item)
    for i in item:
        distance += math.sqrt(abs(np.square(i) - np.square(avg)))
    return distance / len(item)

def mahalanobis( item1:list, item2:list ) -> float:
    total = 0
    avg1 = sum(item1) / len(item1) # average of item1
    avg2 = sum(item2) / len(item2) # average of item2
    for i in range(len(item1)): # calculation of total mahal distance for each values in the lists
        total += pow(item1[i]-avg1, 2) / np.square(std(item1)) + pow(item2[i]-avg2, 2) / np.square(std(item2))
    return math.sqrt(total)

mahalanobis( liste_1, liste_2 )