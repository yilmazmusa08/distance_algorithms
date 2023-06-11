def jaccard_similarity(set1, set2):
    """Calculate the Jaccard similarity between two sets."""
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    similarity = intersection / union
    return similarity

# Example usage
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

jaccard_sim = jaccard_similarity(set1, set2)
print(f"Jaccard similarity: {jaccard_sim}")
