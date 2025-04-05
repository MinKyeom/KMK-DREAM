"""
출처:프로그래머스,
https://school.programmers.co.kr/learn/courses/30/lessons/42883
"""
# 풀이 과정
def solution(number, k):
    # 앞에서부터 제일 작은 수 k개
    from collections import deque
    t = deque(list(number))

    result = []

    while k:
        n = t.popleft()

        if len(result) == 0:
            result.append(n)

        elif len(t) == 0:
            if int(result[-1]) < int(n):
                while True:
                    result.pop()
                    k -= 1
                    if len(result) == 0 or k == 0:
                        result.append(n)
                        break
                    elif int(result[-1]) >= int(n):
                        result.append(n)
                        break
            else:
                if int(result[-1]) >= int(n):
                    result.append(n)
            if k > 0:
                return "".join(result[:len(result) - k])
        else:
            if int(result[-1]) < int(n):
                while True:
                    result.pop()
                    k -= 1
                    if len(result) == 0 or k == 0:
                        result.append(n)
                        break
                    elif int(result[-1]) >= int(n):
                        result.append(n)
                        break
            else:
                if int(result[-1]) >= int(n):
                    result.append(n)

    final = "".join(list(result) + list(t))
    return final

# 다른 사람 풀이
def solution(number, k):
    stack = [number[0]]
    for num in number[1:]:
        while len(stack) > 0 and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()
        stack.append(num)
    if k != 0:
        stack = stack[:-k]
    return ''.join(stack)
