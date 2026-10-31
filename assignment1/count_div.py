def solution(A, B, K):
    # Start at A if A is divisible by K else the first number after A that is divisible by K
    start = A + K - remainder if (remainder := A % K) != 0 else A
    # Find how many K are in the range
    return (B - start) // K + 1
