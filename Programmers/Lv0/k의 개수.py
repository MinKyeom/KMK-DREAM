"""
출처: 프로그래머스 코딩 테스트 연습,
https://school.programmers.co.kr/learn/courses/30/lessons/120887
"""
# 풀이 1
def solution(i, j, k):
    answer = 0
    num = []
    for x in range(i, j + 1):
        num.append(str(x))

    a = "".join(num)

    return a.count(str(k))

# 풀이 2

def solution(i, j, k):
    answer = sum([ str(i).count(str(k)) for i in range(i,j+1)])
    return answer