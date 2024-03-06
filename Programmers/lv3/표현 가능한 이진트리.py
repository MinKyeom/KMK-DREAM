# 내 풀이
# 왼쪽 자식 노드가 1일때 오른쪽 노드는 반드시 1이고,부모노드 또한 1이어야한다 이걸 바탕으로 확인해야한다
from collections import deque


def solution(numbers):
    result = []
    n = numbers

    for i in n:
        k = bin(i)[2:]

        l = len(k)

        # 포화이진 트리 찾기
        h = 0  # 깊이
        count = 0

        while count < l:
            count += 2 ** h
            h += 1

        # 포화 이진트리로 모형으로 변환
        k = "0" * (count - l) + k

        # 맨 처음 노드 번호
        start = (len(k) + 1) // 2 - 1  # -1인이유: 인덱스 번호
        d = (start + 1) // 2
        # print(start,i, "start")
        q = deque([start])

        m = [False for _ in range(len(k))]
        flag = False

        son = []  # 자식노드 모음
        while True:
            arrive = q.popleft()
            a = arrive
            # 방문 확인
            m[a] = True
            # 부모 노드 0일때
            if k[a] == "0":
                if 0 <= a + d < len(k) and k[a + d] == "1" and m[a + d] == False:
                    # print(1,i,"d:",d,"a :",a,"a+d:",a+d)
                    flag = True
                    break
                elif 0 <= a + d < len(k) and k[a + d] == "0" and m[a + d] == False:
                    # print(2,i)
                    son.append(a + d)

                if 0 <= a - d < len(k) and k[a - d] == "1" and m[a - d] == False:
                    # print(3,i)
                    flag = True
                    break
                elif 0 <= a - d < len(k) and k[a - d] == "0" and m[a - d] == False:
                    # print(4,i)
                    son.append(a - d)
            else:

                if 0 <= a + d < len(k) and m[a + d] == False:
                    son.append(a + d)
                if 0 <= a - d < len(k) and m[a - d] == False:
                    son.append(a - d)

            if len(q) == 0:
                if len(son) == 0:
                    break
                else:
                    q += son
                    d //= 2
                    son = []
            # print(q)

        if flag == True:
            result.append(0)
            # print("--------",i,"result")
        else:
            result.append(1)
            # print("--------",i,"result")
    return result

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


# 다른 사람 풀이
def dnc(num, left, right):
    if left == right:
        return [True, int(num[left])]

    mid = (left + right) // 2
    root = int(num[mid])

    left_subtree = dnc(num, left, mid - 1)
    right_subtree = dnc(num, mid + 1, right)

    flag = left_subtree[1] or right_subtree[1]

    if flag == 1 and root == 0:
        return [0, 0]

    return [left_subtree[0] and right_subtree[0], root]

def get_answer(num):
    tmp = ''
    while num > 0:
        tmp = tmp + str(num % 2)
        num //= 2
    size = 1
    while len(tmp) > pow(2, size) - 1:
        size += 1
    while len(tmp) < pow(2, size) - 1:
        tmp += '0'

    return int(dnc(tmp, 0, len(tmp) - 1)[0])


def solution(numbers):
    answer = [get_answer(num) for num in numbers]
    return answer