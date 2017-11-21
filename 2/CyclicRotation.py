# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    # write your code in Python 3.6
    return A if len(A) == 0 else A[len(A) - K % len(A):] + A[:len(A) - K % len(A)]