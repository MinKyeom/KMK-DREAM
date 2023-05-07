# 내 풀이
def solution(n):
    num = []
    for a in range(1, n + 1):
        if a % 2 == 1:
            num.append(a)
        else:
            continue

    answer = sorted(num)
    return answer
# 다른 사람 풀이
def solution(n):
    return [i for i in range(1, n+1, 2)]
