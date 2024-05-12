"""
출처: 프로그래머스 코딩 테스트 연습,
https://school.programmers.co.kr/learn/courses/30/lessons/181853
"""
#풀이 1
def solution(score):
    result = []
    ave = []
    for a, b in score:
        x = (a + b) / 2
        ave.append(x)
    for c in ave:
        count = 1
        for d in ave:
            if c < d:
                count += 1
            else:
                continue
        result.append(count)
    return result

#풀이 2

def solution(score):
    a = sorted([sum(i) for i in score], reverse = True)
    return [a.index(sum(i))+1 for i in score]