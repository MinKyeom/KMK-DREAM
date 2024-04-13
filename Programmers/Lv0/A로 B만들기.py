"""
출처: 프로그래머스 코딩 테스트 연습,
https://school.programmers.co.kr/learn/courses/30/lessons/120886
"""
# 풀이1
def solution(before, after):
    result = 0
    if len(before) == len(after):
        for a in range(len(before)):
            if before.count(before[a]) == after.count(before[a]):
                result += 1
                continue
            else:
                return 0

    return 1


# 풀이2

def solution(before, after):
    before=sorted(before)
    after=sorted(after)
    if before==after:
        return 1
    else:
        return 0



