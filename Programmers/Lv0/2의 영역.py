"""
출처: 프로그래머스 코딩 테스트 연습,
https://school.programmers.co.kr/learn/courses/30/lessons/181894
"""
# 내 풀이

def solution(arr):
    result = []
    sub = []
    for x in arr:
        if x == 2 or 2 in result:
            if x == 2:
                if not len(sub) == 0:
                    result = result + sub
                    result.append(x)
                    sub = []
                else:
                    result.append(x)
            else:
                sub.append(x)

        else:
            continue

    return result if len(result) > 0 else [-1]

# 다른 사람 풀이
def solution(arr):
    if 2 not in arr:
        return [-1]
    return arr[arr.index(2) : len(arr) - arr[::-1].index(2)]
