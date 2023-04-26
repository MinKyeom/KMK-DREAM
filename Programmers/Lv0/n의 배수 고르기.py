# 내 풀이

def solution(n, numlist):
    answer = []
    for x in numlist:
        if x % n == 0:
            answer.append(x)
    return answer


# 내 풀이 2

def solution(n, numlist):
    answer = []
    for x in numlist:
        if x%n==0:
            answer.append(x)
        else:continue
    return answer

# 팀원 풀이

def solution(n, numlist):
    return [num for num in numlist if num % n == 0]

# 다른 사람들 풀이

def solution(n, numlist):
    return list(filter(lambda v: v%n==0, numlist))