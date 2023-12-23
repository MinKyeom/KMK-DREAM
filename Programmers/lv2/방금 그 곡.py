# 내 풀이(개선 중)
def solution(m, musicinfos):
    from collections import deque

    mu = musicinfos

    result = []

    for k in mu:
        t = k.split(",")

        time_start = t[0].split(":")
        time_start = int(time_start[0]) * 60 + int(time_start[1])

        time_finish = t[1].split(":")
        time_finish = int(time_finish[0]) * 60 + int(time_finish[1])

        run_time = time_finish - time_start  # 시작 할 때 첫 소절 나옴

        if len(t[3]) > run_time:
            pass

        else:
            count = 0
            num = len(t[3])
            while len(t[3]) <= run_time:
                if count == 0:
                    t[3] += t[3][0]
                else:
                    k = count % num
                    t[3] += t[3][k]
                count += 1

        # print(t[3])
        t += [run_time]

        # print(t[3],run_time)

        if m in t[3]:
            if m[-1] != "#":
                if (m + "#") in t[3]:
                    continue
                else:
                    result.append(t)
            else:
                result.append(t)

        # elif t[3] in m:
        #     if t[3][-1]!="#":
        #         if t[3]+"#" in m:
        #             continue
        #         else:
        #             result.append(t)
        #     else:
        else:
            continue
    # print(t[3][-1],"t[3]")
    if len(result) == 0:
        return "(None)"

    result.sort(key=lambda x: (-int(x[-1])))

    return result[0][2]

# 다른 사람 풀이