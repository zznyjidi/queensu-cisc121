def solution(A):
    # Add all integers above 0 to a sorted list
    buffer = set()
    for n in A:
        if n > 0:
            buffer.add(n)
    buffer = sorted(buffer)

    # Find the first integer not connected with last one
    last = 0
    for n in buffer:
        if n == last + 1:
            last = n
        else:
            break
    return last + 1
