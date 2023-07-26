# 내 풀이
def solution(arr, divisor):
    result = []
    for x in arr:
        if x % divisor == 0:
            result.append(x)
    result.sort()

    return result if len(result) >= 1 else [-1]

# 다른 사람 풀이
def solution(arr, divisor): return sorted([n for n in arr if n%divisor == 0]) or [-1]