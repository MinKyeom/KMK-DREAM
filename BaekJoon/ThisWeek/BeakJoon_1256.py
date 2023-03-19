import sys
input = sys.stdin.readline

if __name__ == '__main__':
    N, M, K = map(int, input().split())

    # Set counts
    counts = [[1]*(M+1) for _ in range(N+1)]

    for i in range(1, N+1):
        for j in range(1, M+1):
            counts[i][j] = counts[i-1][j] + counts[i][j-1]
    # Print
    if counts[N][M] < K:
        print(-1)
    else:
        to_print = ""

        while True:
            if N == 0 or M == 0:
                to_print += "a"*N + "z"*M
                break

            cnt = counts[N-1][M]
            if cnt >= K:
                to_print += "a"
                N -= 1
            else:
                to_print += "z"
                M -= 1
                K -= cnt

        print(to_print)


print(solution(0, 0))