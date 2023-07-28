# 내 풀이
def solution(picks, minerals):
    from collections import deque

    answer = 0
    tired = [[1, 1, 1], [5, 1, 1], [25, 1, 1]]
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

