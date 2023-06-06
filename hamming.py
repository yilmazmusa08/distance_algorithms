def hamming_distance(list1, list2):
    if len(list1) != len(list2):
        raise ValueError("Input lists must have the same length")

    distance = 0
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            distance += 1

    return distance

# Example usage
list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 9, 4, 0]

distance = hamming_distance(list1, list2)
print("Hamming distance:", distance)
