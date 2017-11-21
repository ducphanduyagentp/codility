# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, A):
    # write your code in Python 3.6
    maxCounter = 0
    currentMaxCounter = 0
    counter = [-1 for _ in range(N)]
    for n in A:
        if n == N + 1:
            currentMaxCounter = maxCounter
        else:
            n -= 1
            counter[n] = counter[n] + 1 if counter[n] > currentMaxCounter else currentMaxCounter + 1
            maxCounter = max(maxCounter, counter[n])
    return [n if n > currentMaxCounter else currentMaxCounter for n in counter]