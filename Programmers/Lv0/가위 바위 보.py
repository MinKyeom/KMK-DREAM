"""
출처: 프로그래머스 코딩 테스트 연습,
https://school.programmers.co.kr/learn/courses/30/lessons/120839
"""
# 내 풀이

def solution(rsp):
    a = list(rsp)
    result = []
    for x in a:
        if x == "2":
            result.append("0")
        elif x == "0":
            result.append("5")
        elif x == "5":
            result.append("2")
    answer = "".join(result)

    return answer


# 다른 사람 풀이

def solution(rsp):
    d = {'0':'5','2':'0','5':'2'}
    return ''.join(d[i] for i in rsp)

def solution(rsp):
    rsp =rsp.replace('2','s')
    rsp =rsp.replace('5','p')
    rsp =rsp.replace('0','r')
    rsp =rsp.replace('r','5')
    rsp =rsp.replace('s','0')
    rsp =rsp.replace('p','2')
    return rsp
