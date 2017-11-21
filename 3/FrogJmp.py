# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from math import ceil

def solution(X, Y, D):
    # write your code in Python 3.6
    return int(ceil((Y - X) / D))