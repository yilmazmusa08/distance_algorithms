def levenshtein_distance(str1, str2):
    m = len(str1)
    n = len(str2)

    # Create a distance matrix
    distance = [[0] * (n + 1) for _ in range(m + 1)]

    # Initialize the first row and column of the matrix
    for i in range(m + 1):
        distance[i][0] = i
    for j in range(n + 1):
        distance[0][j] = j

    # Calculate the distance
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                cost = 0
            else:
                cost = 1

            distance[i][j] = min(
                distance[i - 1][j] + 1,     # deletion
                distance[i][j - 1] + 1,     # insertion
                distance[i - 1][j - 1] + cost  # substitution
            )

    return distance[m][n]

# Example usage
string1 = "kitten"
string2 = "sitting"

distance = levenshtein_distance(string1, string2)
print("Levenshtein distance:", distance)
