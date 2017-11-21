# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    prefix = 0
    minDiff = int(1e9)
    sumA = sum(A)
        
    for p in range(1, len(A)):
        prefix += A[p - 1]
        minDiff = min(abs( 2 * prefix - sumA ), minDiff)
        
    return minDiff