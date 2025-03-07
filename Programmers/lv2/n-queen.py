"""
출처:프로그래머스,
https://school.programmers.co.kr/learn/courses/30/lessons/12952
"""
# 풀이 과정
def check(chess, n, queen):
    count = 0
    if n == queen:
        return 1

    for i in range(n):
        chess[queen] = i
        for j in range(queen):
            if chess[j] == chess[queen]:
                break
            if abs(chess[j] - chess[queen]) == (queen - j):
                break
        else:
            count += check(chess, n, queen + 1)
    return count


def solution(n):
    chess = [0] * n
    return check(chess, n, 0)


# 다른 사람 풀이
def solution(n):
    # 어태까지의 queen 위치 ls, 내가 두려는 위치 new
    def check(ls, new):
        for i in range(len(ls)):
            # 같은 열에 퀸을 둔 적이 있거나, 대각 위치에 둔 적이 있다면, return False
            if new == ls[i] or (len(ls) - i) == abs(ls[i] - new):
                return False
        return True

    def dfs(n, ls):
        # 끝 행까지 도달! return 1
        if len(ls) == n:
            return 1
        # 끝 행이 아니라면, 다음 줄을 다시 탐색
        cnt = 0
        for i in range(n):
            if check(ls, i):
                cnt += dfs(n, ls + [i])
        # 탐색 결과를 return
        return cnt

    return dfs(n, [])