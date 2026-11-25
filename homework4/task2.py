def find_max_subarray(array):
    n = len(array)
    best = float('-inf')
    
    for a in range(n):
        array_sum = 0
        for b in range(a, n):
            array_sum += array[b]
            best = max(best, array_sum)
    return best
