# 내 풀이(개선 중)
# dfs start
def another(i, d_time, d, count, visit, K, new):
    flag = False

    for a in d[i]:
        if not [a, i] in visit:
            if 1 in d[a]:
                count += d_time[a, i]
                count += d_time[a, 1]
                new.append(count)
            else:
                count += d_time[a, i]
                visit.append([a, i])
                if count > K:
                    flag = True
                    break

                else:
                    count, flag = another(a, d_time, d, count, visit, K, new)

        else:
            continue

    # print(new,"new")
    c = min(new)
    return flag, c


def solution(N, road, K):
    # 1번 마을에서 배달 가능한 마을의 개수
    # dfs
    # 도달 가능한지 여부

    result = 0  # 마을의 개수
    d = {}  # 연결된 마을
    d_time = {}
    del_list = [k for k in range(2, N + 1)]  # 배달 받을 마을
    visit = []

    for a, b, c in road:
        if not a in d:
            d[a] = [b]
            d_time[a, b] = c
        else:
            d[a].append(b)
            d_time[a, b] = c
        if not b in d:
            d[b] = [a]
            d_time[b, a] = c
        else:
            d[b].append(a)
            d_time[b, a] = c

    for i in del_list:
        count = 0  # 거리
        visit = []
        if i in d[1]:
            count += d_time[i, 1]
            if count <= K:
                result += 1
            else:
                continue

        else:
            new = []
            flag, c = another(i, d_time, d, count, visit, K, new)
            # print(flag,"flag",count,visit)
            if c <= K and flag == False:
                print("check")
                result += 1

    return result

# 다른 사람 풀이
