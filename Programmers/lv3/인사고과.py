# 내 풀이
def solution(scores):
    n = scores[0]
    num = n[0] + n[1]

    s = sorted(scores, key=lambda x: (-x[0], x[1]))

    check = []

    for i in range(len(s)):
        if s[i][0] + s[i][1] > num:
            if s[i][0] > n[0] and s[i][1] > n[1]:
                return -1

            elif len(check) == 0:  # 첫번째의 경우 인센티브 못받을 경우x
                check.append([s[i][0], s[i][1]])
                v = s[i][1]
                w = s[i][0]

            else:
                if s[i][0] != w:  # 더 작아지는 순간
                    if v > s[i][1]:  # 이전 첫번째 성과가 무조건 높기에 두번째는 그 이전보다 높아야 인센티브 가능!
                        continue
                    else:
                        check.append([s[i][0], s[i][1]])
                        v = s[i][1]
                        w = s[i][0]
                else:
                    check.append([s[i][0], s[i][1]])
                    v = s[i][1]  # 첫번쨰가 같다면 두번쩨는 뒤로 갈수록 점수가 최소 높거나 같기때문에 갱신

    return len(check) + 1
# 내 풀이(개선 중5)
# 2중 for문 한 번에 구별가능한지 확인!
# 완호의 점수
# 임의의 다른 사원보다 두 점수 모두 낮은 경우 인센티브x +석차에서 제외

from collections import deque
def solution(scores):
    # 완호의 점수
    s = deque(scores)
    n = s.popleft()
    num = n[0] + n[1]
    # 완호보다 위의 사람
    check = deque([])
    while s:
        i, j = s.popleft()
        if i + j > num:
            if len(check) == 0:
                check.append([i, j])
            else:
                k = len(check)
                count = 0
                flag = False

                while count < k:
                    v, w = check.popleft()
                    if v > i and w > j:
                        flag = True
                        break
                    elif v < i and w < j:
                        continue
                    else:
                        check.append([v, w])
                    count += 1
                if flag == False:
                    check.append([i, j])

    return len(check) + 1


# 내 풀이(개선 중4)
# 2중 for문 한 번에 구별가능한지 확인!
# 완호의 점수
# 임의의 다른 사원보다 두 점수 모두 낮은 경우 인센티브x +석차에서 제외

from collections import deque


def solution(scores):
    scores = deque(scores)
    result = 0

    # 완호의 점수
    s = scores
    num = s[0][0] + s[0][1]
    rank = 1

    # 완호보다 상위 등수 확인
    check = []

    for k in range(len(s)):
        if s[k][0] + s[k][1] > num:
            check.append([s[k][0], s[k][1]])
        elif s[0][0] < s[k][0] and s[0][1] < s[k][1]:
            return -1

    # 상위 등수 중 제외 받을 사원 확인
    final = []
    for i in range(len(check)):
        for j in range(len(check)):
            if check[i][0] < check[j][0] and check[i][1] < check[j][1]:
                break
        else:
            final.append([check[i][0], check[i][1]])

    return len(final) + 1


# 내 풀이(개선 중3)
# 2중 for문을 활용하여 효율성 한 번에 개선 가능한지 체크


# 내 풀이(개선 중2)
# 완호의 점수
# 임의의 다른 사원보다 두 점수 모두 낮은 경우 인센티브x +석차에서 제외

from collections import deque


def solution(scores):
    scores = deque(scores)

    # 완호의 점수
    n = scores.popleft()
    num = n[0] + n[1]

    s = list(scores)

    check = []

    one = 0
    two = 0

    for l in range(len(s)):
        one = max(one, s[l][0])
        two = max(two, s[l][1])

    for i in range(len(s)):
        if s[i][0] + s[i][1] > num:
            new = []
            if s[i][0] < one or s[i][1] < two:
                for j in range(len(check)):
                    if check[j][0] > s[i][0] and check[j][1] > s[i][1]:
                        break
                    elif check[j][0] < s[i][0] and check[j][1] < s[i][1]:
                        new.append([check[j][0], check[j][1]])
                else:
                    check.append([s[i][0], s[i][1]])

            else:
                check.append([s[i][0], s[i][1]])

            for j in new:
                k = check.index(j)
                del check[k]

        if s[i][0] > n[0] and s[i][1] > n[1]:
            return -1

    #     # 공동으로 있는 경우도 있기 때문에 rank를 바꿀 수 없다
    #     check=deque(check)
    #     k=len(check)
    #     count=0

    #     # 제외 명단
    #     # 상위 명단에 있음에도 인센티브를 못받는 경우 발생 가능성 존재

    #     last=[]

    #     while count<k:
    #         i,j=check.popleft()
    #         new=[]
    #         for t in range(len(check)):
    #             if check[t][0]>i and check[t][1]>j:
    #                 break
    #         else:
    #             check.append([i,j])
    #             new.append([i,j])

    #         count+=1

    return len(check) + 1


# 내 풀이(개선 중)
# 완호의 점수
# 임의의 다른 사원보다 두 점수 모두 낮은 경우 인센티브x +석차에서 제외

from collections import deque


def solution(scores):
    scores = deque(scores)

    # 완호의 점수
    n = scores.popleft()
    num = n[0] + n[1]

    s = list(scores)

    check = []

    for i in range(len(s)):
        if s[i][0] + s[i][1] > num:
            check.append([s[i][0], s[i][1]])
            if s[i][0] > n[0] and s[i][1] > n[1]:
                return -1

    # 공동으로 있는 경우도 있기 때문에 rank를 바꿀 수 없다
    check = deque(check)

    k = len(check)
    count = 0

    # 제외 명단
    # 상위 명단에 있음에도 인센티브를 못받는 경우 발생 가능성 존재
    new = []

    while count < k:
        i, j = check.popleft()

        for v, w in list(check):
            if v > i and w > j:
                new.append([i, j])
                break
        else:
            check.append([i, j])

        count += 1

    return len(check) + 1

# 다른 사람 풀이
def solution(scores):
    wanho = scores[0]
    wanho_sum = sum(wanho)
    scores.sort(key=lambda s: (-s[0], s[1]))
    max_company, answer = 0, 1
    for s in scores:
        if wanho[0] < s[0] and wanho[1] < s[1]:
            return -1
        if max_company <= s[1]:
            if wanho_sum < s[0] + s[1]:
                answer += 1
            max_company = s[1]
    return answer