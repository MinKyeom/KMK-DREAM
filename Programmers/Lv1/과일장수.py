# 내 풀이
def solution(k, m, score):
    score.sort()
    if len(score) % m == 0:
        result = score[::m]
        count = len(score) / m
        result = [(x * m) for x in result]
        return sum(result)
    else:
        k = len(score) % m
        count = int(len(score) / m)
        result = score[k::m]
        result = [(x * m) for x in result]
        return sum(result)


# 다른 사람 풀이
def solution(k, m, score):
    return sum(sorted(score)[len(score)%m::m])*m
