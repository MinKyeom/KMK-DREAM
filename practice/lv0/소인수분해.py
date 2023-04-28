# 내 풀이

def solution(n):
    num = []
    count = 0
    for a in range(2, n + 1):
        if n % a == 0:
            for b in range(len(num)):
                if a % num[b] == 0:
                    count += 1
                else:
                    continue
            if count == 0:
                num.append(a)
            else:
                count = 0
                continue

    answer = num
    return answer

# 다른 사람 풀이

def solution(n):
    answer = []
    d = 2
    while d <= n:
        if n % d == 0:
            n /= d
            if d not in answer:
                answer.append(d)
        else:
            d += 1
    return answer