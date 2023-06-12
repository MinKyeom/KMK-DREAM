# 내 풀이
def solution(n):
    result=[n]
    while True:
        if n%2==0:
            n/=2
            result.append(n)
            if n==1:
                return result
        else:
            n=3*n+1
            result.append(n)
            if n==1:
                return result

# 다른 사람 풀이
def solution(n):
    answer = [n]
    while n > 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        answer.append(n)
    return answer