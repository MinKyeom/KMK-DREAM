"""
출처: 프로그래머스 코딩 테스트 연습,
https://school.programmers.co.kr/learn/courses/30/lessons/120829
"""
# 내 풀이
def solution(angle):
    if angle<90:
        return 1
    elif angle==90:
        return 2
    elif 90<angle<180:
        return 3
    elif angle==180:
        return 4



# 다른 사람 풀이
def solution(angle):
    answer = (angle // 90) * 2 + (angle % 90 > 0) * 1
    return answer