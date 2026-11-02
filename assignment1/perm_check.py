def solution(A):
    # Return 0 if there is a integer not connected with last one in the sorted list else 1
    sortedA = sorted(A)
    last = 0
    for n in sortedA:
        if n != last + 1:
            return 0
        last = n
    return 1
