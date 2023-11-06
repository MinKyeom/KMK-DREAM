# 내 풀이
def solution(info, query):
    from itertools import combinations
    from collections import defaultdict
    import bisect
    result = []

    dic = defaultdict(list)

    for a in info:
        a = a.split()
        condition = a[:-1]
        score = int(a[-1])  # 숫자만 따로 빼놓음

        # 해당 경우의 수에서 -를 포함하는 모든 경우의 수를 추가!!!
        for b in range(5):
            case = list(combinations([0, 1, 2, 3], b))

            for c in case:
                tmp = condition.copy()

                for idx in c:
                    tmp[idx] = "-"

                key = "".join(tmp)
                dic[key].append(score)

    for value in dic.values():
        # 내부 스코어 값 정렬(같은 경우의 수에 해당하는 사람의 경우 스코어를 리스트에 추가 후 지금 정렬)
        value.sort()

    for d in query:
        d = d.replace("and", "")
        d = d.split()

        target_key = "".join(d[:-1])
        target_score = int(d[-1])

        count = 0

        if target_key in dic:
            target_list = dic[target_key]
            idx = bisect.bisect_left(target_list, target_score)
            count = len(target_list) - idx

        result.append(count)

    return result
    # 개선 중 풀이 3
    for b in range(len(query)):
        t = query[b].split(" ")
        v = [t[0], t[2], t[4], t[6], t[7]]
        check.append(v)

    for a in info:
        k = a.split(" ")
        # person.append(k)

        for d in range(len(check)):
            flag = False

            if check[d][0] == "-" or check[d][0] == k[0]:
                pass
            else:
                flag = True
                continue

            if check[d][1] == "-" or check[d][1] == k[1]:
                pass
            else:
                flag = True
                continue

            if check[d][2] == "-" or check[d][2] == k[2]:
                pass
            else:
                flag = True
                continue

            if check[d][3] == "-" or check[d][3] == k[3]:
                pass
            else:
                flag = True
                continue

            if int(check[d][4]) <= int(k[4]):
                pass
            else:
                flag = True
                continue

            result[d] += 1

    """
    #정확도 100 효율성 애매 풀이
    for a in info:
        k=a.split(" ")

        for b in range(len(query)):
            t=query[b].split(" ")
            v=[t[0],t[2],t[4],t[6],t[7]]

            flag=False

            for d in range(len(v)):
                if v[d]=="-":
                    continue

                else:
                    if d<4:
                        if k[d]==v[d]:
                            continue
                        else:
                            flag=True
                            break
                    else:
                        if int(k[d])>=int(v[d]):
                            continue
                        else:
                            flag=True
                            break

            if flag==False:
                result[b]+=1
                """

    return result

# 다른 사람 풀이
from itertools import combinations
from collections import defaultdict
from bisect import bisect_left

def solution(information, queries):
    answer = []
    dic = defaultdict(list)
    for info in information:
        info = info.split()
        condition = info[:-1]
        score = int(info[-1])
        for i in range(5):
            case = list(combinations([0,1,2,3], i))
            for c in case:
                tmp = condition.copy()
                for idx in c:
                    tmp[idx] = "-"
                key = ''.join(tmp)
                dic[key].append(score)

    for value in dic.values():
        value.sort()

    for query in queries:
        query = query.replace("and ", "")
        query = query.split()
        target_key = ''.join(query[:-1])
        target_score = int(query[-1])
        count = 0
        if target_key in dic:
            target_list = dic[target_key]
            idx = bisect_left(target_list, target_score)
            count = len(target_list) - idx
        answer.append(count)
    return answer


# 다른 사람 풀이 2
# 지원자들 정보, 개발팀이 원하는 조건
def solution(info, query):
    # 나올 수 있는 모든 조건
    data = dict()
    for a in ['cpp', 'java', 'python', '-']:
        for b in ['backend', 'frontend', '-']:
            for c in ['junior', 'senior', '-']:
                for d in ['chicken', 'pizza', '-']:
                    data.setdefault((a, b, c, d), list())

    # 지원자들이 해당할 수 있는 조건에 점수 넣기
    for i in info:
        i = i.split()
        for a in [i[0], '-']:
            for b in [i[1], '-']:
                for c in [i[2], '-']:
                    for d in [i[3], '-']:
                        data[(a, b, c, d)].append(int(i[4]))

    # 지원자 점수 오름차순 정렬
    for k in data:
        data[k].sort()

    # 개발자가 원하는 조건에 맞는 인원 수
    answer = list()

    for q in query:
        q = q.split()
        # 개발자가 원하는 조건에 해당하는 사람들의 점수
        scores = data[(q[0], q[2], q[4], q[6])]
        # 개발자가 원하는 점수보다 높은 사람 수 세기 -> 이분 탐색
        wanted = int(q[7])
        l, r = 0, len(scores)
        while l < r:
            middle = (l + r) // 2
            if scores[middle] >= wanted:
                r = middle
            else:
                l = middle + 1
        answer.append(len(scores) - l)

    return answer