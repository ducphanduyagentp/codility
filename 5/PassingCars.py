# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    countOne = A.count(1)
    ans = 0
    one = 0
    for n in A:
        if n == 0:
            ans += (countOne - one)
            if ans > int(1e9):
                return -1
        else:
            one += 1
    return ans