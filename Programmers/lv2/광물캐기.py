# 내 풀이 1
def solution(picks, minerals):
    from collections import deque

    answer = 0
    tired = [[1, 1, 1], [5, 1, 1], [25, 5, 1]]
    connection = {"diamond": 0,
                  "iron": 1,
                  "stone": 2
                  }

    info = []
    minerals = minerals[:5 * sum(picks)]  # 곡쾡이 개수까지 슬라이싱
    q = deque(minerals)  # deque의 형태로 변형!

    while q:  # 리스트 내부가 존재하는한!
        dig = 0
        di_, ir_, st_ = 0, 0, 0
        while dig < 5:
            dig += 1
            minerals = q.popleft()
            di_ += tired[0][connection[minerals]]
            ir_ += tired[1][connection[minerals]]
            st_ += tired[2][connection[minerals]]
            if not q:
                break

        info.append([di_, ir_, st_])

    info.sort(key=lambda x: [x[2], x[1], x[0]])
    # 돌,철,다이아 순으로 피로도가 클수록 다이아 곡쾡이로 캤을때 이득이 많이 발생한다!

    for idx, p in enumerate(picks):  # enumerate의 경우 순서를 알려줌!
        for _ in range(p):
            if info:  # info 리스트가 존재하는 한
                answer += info.pop()[idx]
            else:
                return answer

    return answer

# 내 풀이 2
def solution(picks, minerals):
    from collections import deque
    minerals = minerals[:5 * sum(picks)]
    count = 0  # 광물카운트
    c_d = 0
    c_i = 0
    c_s = 0
    check = []  # 각 종류별 곡쾡이 피로도

    for x in range(len(minerals)):
        if minerals[x] == "diamond":
            count += 1
            c_d += 1
            c_i += 5
            c_s += 25
        elif minerals[x] == "iron":
            count += 1
            c_d += 1
            c_i += 1
            c_s += 5
        elif minerals[x] == "stone":
            count += 1
            c_d += 1
            c_i += 1
            c_s += 1
        if count == 5 or x == len(minerals) - 1:
            check.append([c_d, c_i, c_s])
            count = 0
            c_d = 0
            c_i = 0
            c_s = 0
    check.sort(key=lambda x: (-x[2], -x[1], -x[0]))

    result = 0

    check = deque(check)

    for y in range(len(picks)):
        count_p = 0
        while count_p < picks[y] and check:
            result += check[0][y]
            check.popleft()
            count_p += 1

    return result

# 다른 사람 풀이
def solution(picks, minerals):
    def solve(picks, minerals, fatigue):
        if sum(picks) == 0 or len(minerals) == 0:
            return fatigue
        result = [float('inf')]
        for i, fatigues in enumerate(({"diamond": 1, "iron": 1, "stone": 1},
                                      {"diamond": 5, "iron": 1, "stone": 1},
                                      {"diamond": 25, "iron": 5, "stone": 1},)):
            if picks[i] > 0:
                temp_picks = picks.copy()
                temp_picks[i] -= 1
                result.append(
                    solve(temp_picks, minerals[5:], fatigue + sum(fatigues[mineral] for mineral in minerals[:5])))
        return min(result)

    return solve(picks, minerals, 0)


