# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, A):
    # write your code in Python 3.6
    check = [False for _ in range(X)]
    countDown = X
    for i in range(len(A)):
        countDown -= 1 if not check[A[i] - 1] else 0
        check[A[i] - 1] = True
        if countDown == 0:
            return i
    return -1