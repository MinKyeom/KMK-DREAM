# 내 풀이
def solution(arr, intervals):
    result = []
    for x, y in intervals:
        result = result + arr[x:y + 1]

    return result

# 다른 사람 풀이

def solution(arr, intervals):
    s1, e1 = intervals[0]
    s2, e2 = intervals[1]
    return arr[s1:e1+1] + arr[s2:e2+1]