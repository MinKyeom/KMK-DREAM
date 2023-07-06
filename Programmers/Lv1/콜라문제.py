# 내 풀이
def solution(a, b, n):
    result = 0
    while True:
        x = int(n / a) * b
        result += x
        n = (n % a) + x
        if n < a:
            return result

# 다른 사람 풀이
solution = lambda a, b, n: max(n - b, 0) // (a - b) * b