"""
출처:프로그래머스,
https://school.programmers.co.kr/learn/courses/30/lessons/181188
"""
# 풀이 과정
def solution(targets):
    targets.sort(key=lambda x: x[1])
    target = 0
    count = 0
    for x, y in targets:
        if target <= x:
            count += 1
            target = y

    return count

# 다른 사람 풀이
def solution(targets):
    answer = 0
    targets.sort(key=lambda x: x[1])
    temp = 0
    for i in targets:
        if i[0]<temp:
            continue
        else:
            answer+=1
            temp = i[1]

    return answer