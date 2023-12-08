# 내 풀이
def solution(n, a, b):
    from collections import deque
    k = deque([a for a in range(1, n + 1)])

    answer = 1  # 라운드

    if a > b:
        b, a = a, b

    next_ = []
    count = 0
    while True:
        blue = k.popleft()
        red = k.popleft()

        if blue == a and red == b:
            return answer

        else:
            if blue == a or blue == b:
                k.append(blue)
            else:
                k.append(red)

        if blue == a or blue == b or red == a or red == b:
            count += 1
            if count == 2:
                answer += 1
                count = 0

    return answer

# 다른 사람 풀이
def solution(n,a,b):
    return ((a-1)^(b-1)).bit_length()