# 내 풀이
def solution(want, number, discount):
    from collections import deque
    discount = deque(discount)

    result = 0

    check = {}

    for k in range(len(want)):
        check[want[k]] = number[k]

    result_check = check.copy()

    check_2 = deque([])

    while discount:
        t = discount.pop()
        check_2.append(t)

        if len(check_2) >= 10:
            flag = False
            for l in check_2:
                if l in result_check:
                    if result_check[l] > 0:
                        result_check[l] -= 1
                        if result_check[l] == 0:
                            del result_check[l]
                            if len(result_check) == 0:
                                result += 1
                                check_2.popleft()
                                result_check = check.copy()
                                flag = True
                                break
            if flag == False:
                check_2.popleft()
                result_check = check.copy()

    return result

# 다른 사람 풀이
from collections import Counter
def solution(want, number, discount):
    answer = 0
    dic = {}
    for i in range(len(want)):
        dic[want[i]] = number[i]

    for i in range(len(discount)-9):
        if dic == Counter(discount[i:i+10]):
            answer += 1

    return answer
