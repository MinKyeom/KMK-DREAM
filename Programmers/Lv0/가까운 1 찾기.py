"""
출처: 프로그래머스 코딩 테스트 연습,
https://school.programmers.co.kr/learn/courses/30/lessons/181898
"""
# 내 풀이
def solution(arr, idx):
    for x in range(idx,len(arr)):
        if arr[x]==1:
            return x
    return -1

# 다른 사람 풀이
def solution(arr, idx):
    answer = 0
    try:
        answer = arr.index(1, idx)
    except:
        answer = -1

    return answer