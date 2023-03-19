import sys
from collections import deque

T = int(sys.stdin.readline())

for _ in range(T):
    N, K = map(int, sys.stdin.readline().split())
    time = [0] + list(map(int, sys.stdin.readline().split()))
    seq = [[] for _ in range(N + 1)]
    inDegree = [0 for _ in range(N + 1)]
    DP = [0 for _ in range(N + 1)]

    for _ in range(K):
        a, b = map(int, sys.stdin.readline().split())
        seq[a].append(b)
        inDegree[b] += 1

    q = deque()
    for i in range(1, N + 1):
        if inDegree[i] == 0:
            q.append(i)
            DP[i] = time[i]

    while q:
        a = q.popleft()
        for i in seq[a]:
            inDegree[i] -= 1
            DP[i] = max(DP[a] + time[i], DP[i])
            if inDegree[i] == 0:
                q.append(i)

    ans = int(sys.stdin.readline())
    print(DP[ans])