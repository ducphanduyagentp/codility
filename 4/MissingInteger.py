# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    check = [False for _ in range(len(A) + 1)]
    for n in A:
        if 0 < n <= len(A):
            check[n] = True
    for i in range(1, len(A) + 1):
        if not check[i]:
            return i
    return len(A) + 1