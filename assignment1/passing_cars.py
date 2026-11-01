def solution(A):
    # Count How many wests are in between easts
    west_counts = []
    count = 0
    for n in A:
        if n:
            count += 1
        else:
            west_counts.append(count)
            count = 0
    if count != 0:
        west_counts.append(count)
        count = 0
    
    # Group each east car with all west cars came after it
    total = 0
    for n in west_counts:
        total += n * count
        count += 1
    return total if total <= 1_000_000_000 else -1
