# 내 풀이
def solution(id_list, report, k):
    result = [0 for i in range(len(id_list))]
    answer = [0 for j in range(len(id_list))]
    report = list(set(report))
    check = []
    for x in report:
        o = x.split(" ")
        l = o[1]
        n = o[0]
        m = id_list.index(l)
        result[m] = result[m] + 1  # 신고를 받은 유저 및 횟수

    print(result)

    for y in range(len(result)):
        if result[y] >= k:
            check.append(id_list[y])

    for z in report:
        a = z.split(" ")
        if a[1] in check:
            f = id_list.index(a[0])
            answer[f] = answer[f] + 1

    return answer

# 다른 사람 풀이
def solution(id_list, report, k):
    answer = [0] * len(id_list)
    reports = {x : 0 for x in id_list}

    for r in set(report):
        reports[r.split()[1]] += 1

    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1

    return answer