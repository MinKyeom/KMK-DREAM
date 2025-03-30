"""
출처:프로그래머스,
https://school.programmers.co.kr/learn/courses/30/lessons/138475
"""

# 풀이 과정
# point:약수의 개수를 효율적으로 구하는 방식에 대하여 고민해서 풀기

# 약수의 개수로 구할 수 있다
# 리스트로 만들기에는 1억의 숫자를 두 번 구성하는 리스트 만들 경우 데이터 초과
# 각 수가 나오는 출현 횟수는 표를 보면 약수의 개수와 비례한다는 사실 유추 가능!!
# dp로 한 번에 나오는게 가능한가 생각 접근해보기! > 출제의도!(디클레어 증명등등 사용x)
# 약수의 개수를 구하는 과정을 간소화 시킬 전략 생각해보고 접근하기!

def solution(e, starts):
    dp = [0] * (e + 1)

    for i in range(1, e + 1):
        for j in range(1, min((e // i + 1), i)):
            dp[i * j] += 1

    check = [0] * (e + 1)

    num = 0  # 약수의 번호
    count = 0  # 약수의 개수

    for k in range(e, -1, -1):
        if dp[k] >= count:
            count = dp[k]
            num = k
            check[k] = num
        else:
            check[k] = num

    result = []
    for t in starts:
        result.append(check[t])

    return result

# 약수의 개수로 구할 수 있다
# 리스트로 만들기에는 1억의 숫자를 두 번 구성하는 리스트 만들 경우 데이터 초과
# 각 수가 나오는 출현 횟수는 표를 보면 약수의 개수와 비례한다는 사실 유추 가능!!
# dp로 한 번에 나오는게 가능한가 생각 접근해보기!
# 약수의 개수를 구하는 과정을 간소화 시킬 전략 생각해보고 접근하기!
from collections import deque


def solution(e, starts):
    # 1~e까지의 약수의 개수: 등장 횟수와 동일하다
    # 숫자별 약수 개수 모음 :check
    check = [0] * min(starts)
    count = min(starts)
    check_num = [0] * (e + 1)  # 최대 공약수에 따른 약수 개수

    while count <= e:
        num = 0
        n = int(count ** 0.5)
        g = False  # 최대공약수
        for i in range(1, int(n) + 1):
            # if i!=1 and check_num[count//i]!=0 and :
            #     check.append(check_num[count//i])
            #     break
            if count % i == 0 and count // i != i:
                num += 2
            elif count % i == 0 and count // i == i:
                num += 1
            if i != 1 and g == False:
                g = count // i
                if check_num[g] != 0:
                    check.append(check_num[g])
                    break
                else:
                    continue
        else:
            check.append(num)
            check_num[g] = num

        count += 1

    print(check_num)

    result = []

    # e>1까지의 최소 숫자 리스트
    c_e = [0] * (e + 1)

    count = 0
    num = 0

    for j in range(e, min(starts) - 1, -1):
        if check[j] >= count:
            count = check[j]
            c_e[j] = j
            num = j
        else:
            c_e[j] = num

    result = []

    for a in starts:
        result.append(c_e[a])

    return result
# 내 풀이(개선 중)
# 약수의 개수로 구할 수 있다
# 리스트로 만들기에는 1억의 숫자를 두 번 구성하는 리스트 만들 경우 데이터 초과
# 각 수가 나오는 출현 횟수는 표를 보면 약수의 개수와 비례한다는 사실 유추 가능!!
# dp로 한 번에 나오는게 가능한가 생각 접근해보기!

from collections import deque


def solution(e, starts):
    # 1~e까지의 약수의 개수: 등장 횟수와 동일하다
    # 숫자별 약수 개수 모음 :check
    check = [0] * min(starts)
    count = min(starts)
    check_num = [0] * (e + 1)  # 최대 공약수에 따른 약수 개수

    while count <= e:
        num = 0
        n = int(count ** 0.5)
        g = False  # 최대공약수
        for i in range(1, int(n) + 1):
            # if i!=1 and check_num[count//i]!=0 and :
            #     check.append(check_num[count//i])
            #     break
            if count % i == 0 and count // i != i:
                num += 2
            elif count % i == 0 and count // i == i:
                num += 1
            if i != 1 and g == False:
                g = count // i
                if check_num[g] != 0:
                    check.append(check_num[g])
                    break
                else:
                    continue
        else:
            check.append(num)
            check_num[g] = num

        count += 1

    print(check_num)

    result = []

    # e>1까지의 최소 숫자 리스트
    c_e = [0] * (e + 1)

    count = 0
    num = 0

    for j in range(e, min(starts) - 1, -1):
        if check[j] >= count:
            count = check[j]
            c_e[j] = j
            num = j
        else:
            c_e[j] = num

    result = []

    for a in starts:
        result.append(c_e[a])

    return result

# 내 풀이(개선 중): 시간 초과 발생 및 정답률 80퍼
# 약수의 개수로 구할 수 있다
# 리스트로 만들기에는 1억의 숫자를 두 번 구성하는 리스트 만들 경우 데이터 초과
# 각 수가 나오는 출현 횟수는 표를 보면 약수의 개수와 비례한다는 사실 유추 가능!!
# dp로 한 번에 나오는게 가능한가 생각 접근해보기!

from collections import deque


def solution(e, starts):
    # 1~e까지의 약수의 개수: 등장 횟수와 동일하다
    # 숫자별 약수 개수 모음 :check
    check = [0] * min(starts)
    count = min(starts)
    check_num = [0] * (e + 1)  # 최대 공약수에 따른 약수 개수

    while count <= e:
        num = 0
        n = int(count ** 0.5)

        for i in range(1, int(n) + 1):

            if count % i == 0 and count // i != i:
                num += 2
            elif count % i == 0 and count // i == i:
                num += 1
            if i != 1 and g == False:
                g = count // i

        check.append(num)
        count += 1

    result = []

    # e>1까지의 최소 숫자 리스트
    c_e = [0] * (e + 1)

    count = 0
    num = 0

    for j in range(e, min(starts) - 1, -1):
        if check[j] >= count:
            count = check[j]
            c_e[j] = j
            num = j
        else:
            c_e[j] = num

    result = []

    for a in starts:
        result.append(c_e[a])

    return result

# 다른 사람 풀이
def solution(e, starts):
    answer = []
    data = [1] * (e + 1)

    for i in range(2, e + 1):
        for j in range(i, e + 1, i):
            data[j] += 1

    arr = [0 for _ in range(e + 1)]
    max_val = data[-1]
    idx = len(data) - 1

    for i in range(len(data) - 1, 0, -1):
        if data[i] >= max_val:
            idx = i
            max_val = data[i]
        arr[i] = idx

    for start in starts:
        answer.append(arr[start])

    return answer