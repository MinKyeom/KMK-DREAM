# 내 풀이
def solution(N, stages):
    result = []
    for x in range(1, N + 1):
        arrive = 0
        succes = 0
        for y in stages:
            if y >= x:
                arrive += 1
            if y > x:
                succes += 1
        k = arrive - succes
        if arrive == 0:
            result.append([x, 0])
        else:
            result.append([x, k / arrive])

    result.sort(key=lambda x: (-x[1]))

    answer = [m for m, n in result]

    return answer

# 다른 사람 풀이
def solution(N, stages):
    result = {}
    denominator = len(stages)
    for stage in range(1, N+1):
        if denominator != 0:
            count = stages.count(stage)
            result[stage] = count / denominator
            denominator -= count
        else:
            result[stage] = 0
    return sorted(result, key=lambda x : result[x], reverse=True)