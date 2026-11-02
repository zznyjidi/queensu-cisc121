def solution(X, A):
    # Create a set of all leaves need to fall
    leaf = set(range(1, X + 1))
    # Remove each felt leaf from set until all required leaves are felt or no more leaves
    for time, fall in enumerate(A):
        if fall > X:
            continue
        if fall in leaf:
            leaf.remove(fall)
            if len(leaf) < 1:
                return time
    return -1
