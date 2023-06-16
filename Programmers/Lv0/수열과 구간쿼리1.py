# 내 풀이
def solution(arr, queries):
    for x, y in queries:
        num = [z for z in range(x, y + 1)]
        for s in num:
            arr[s] = arr[s] + 1

    answer = arr
    return answer

# 다른 사람 풀이
import numpy as np

def solution(arr, queries):
    answer = []

    arr = np.array(arr)
    for query in queries:
        arr[query[0]:query[1] + 1] += 1

    answer = arr.tolist()
    return answer
