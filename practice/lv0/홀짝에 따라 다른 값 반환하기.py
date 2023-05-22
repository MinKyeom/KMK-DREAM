# 내 풀이
def solution(n):
    count=0
    if n%2==0:
        for a in range(n+1):
            if a%2==0:
                count+=a**2
        return count
    else:
        for a in range(n+1):
            if not a%2==0:
                count+=a
        return count

# 다른 사람 풀이
def solution(n):
    return sum(x ** (2 - x % 2) for x in range(n + 1) if n % 2 == x % 2)
