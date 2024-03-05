# 내 풀이(개선 중)
# 이진트리 표현가능:1  불가능:0
# 이진수를 보고 트리 모양 결정 후 더미 위치가 문제가 안되는지 체크 후
# 기본 트리 모양을 찾은 후 비교할 트리와 비교
# 높이를 기준으로 나머지를 통해 더미 여부 확인
# 더미가 아니어야 될 위치에 더미가 된다면 0 그렇지 않다면 1
from collections import deque


def solution(numbers):
    n = numbers

    result = []

    for i in n:
        k = bin(i)[2:]
        t = len(k)
        before = t
        count = 0
        check = 0

        while t > 0:
            check += 2 ** count
            t = t - 2 ** count
            count += 1

        h = count  # 트리 높이
        num = "1" * check
        middle = (len(num) + 1) // 2

        if len(num) != before:
            k = "0" * abs(len(num) - before) + k

        m = [False for _ in range(len(k))]

        # k: 체크할 모양
        q = deque([middle])

        flag = False  # 그래프 성립 여부 체크

        while q:
            v = q.popleft()
            m[v] = True
            a = v // 2
            if v == 1:
                a = 1

            if int(k[v]) == 0:
                if 0 <= v + a < len(k):
                    if int(k[v + a]) == 1:
                        flag = True
                        break
                if 0 <= v - a < len(k):
                    if int(k[v - a]) == 1:
                        flag = True
                        break
                if 0 <= v + a < len(k) and m[v + a] == False:
                    q.append(v + a)
                if len(k) > v - a >= 0 and m[v - a] == False:
                    q.append(v - a)

            else:
                if v + a < len(k) and m[v + a] == False:
                    q.append(v + a)
                if v - a >= 0 and m[v - a] == False:
                    q.append(v - a)

        if flag == False:
            result.append(1)
        else:
            result.append(0)

    return result

# 내 풀이(개선 중)
# 이진트리 표현가능:1  불가능:0
# 이진수를 보고 트리 모양 결정 후 더미 위치가 문제가 안되는지 체크 후
# 기본 트리 모양을 찾은 후 비교할 트리와 비교
# 높이를 기준으로 나머지를 통해 더미 여부 확인
# 더미가 아니어야 될 위치에 더미가 된다면 0 그렇지 않다면 1
def solution(numbers):
    n = numbers
    result = []
    for i in n:
        k = bin(i)[2:]
        t = len(k)
        count = 0
        check = 0

        while t > 0:
            check += 2 ** count
            t = t - 2 ** count
            count += 1
        h = count + 1  # 트리 높이
        print(check)
        break

    answer = []
    return answer