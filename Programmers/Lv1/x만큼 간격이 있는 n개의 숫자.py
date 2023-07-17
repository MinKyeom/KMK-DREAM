# 내 풀이
def solution(x, n):
    if x == 0:
        return [x for i in range(n)]

    return [x for x in range(x, x * n + 1, x)] if x > 0 else [x for x in range(x, x * n - 1, x)]
# 다른 사람 풀이
def number_generator(x, n):
    # 함수를 완성하세요
    return [i * x + x for i in range(n)]
print(number_generator(2, 5))
