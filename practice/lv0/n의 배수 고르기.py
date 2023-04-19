# 내 풀이

def solution(n, numlist):
    answer = []
    for x in numlist:
        if x % n == 0:
            answer.append(x)

    return answer


# 다른 사람들 풀이

def solution(n, numlist):
    return list(filter(lambda v: v%n==0, numlist))