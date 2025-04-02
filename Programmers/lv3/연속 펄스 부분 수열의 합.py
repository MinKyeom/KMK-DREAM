"""
출처:프로그래머스,
https://school.programmers.co.kr/learn/courses/30/lessons/161988
"""

# 풀이 과정
# 이분탐색 접근 생각(오름차순이 아니라 활용x)
# 두 개의 펄스를 만든 후 차례대로 각각 더해가다 만약 -를 간다면 0으로 초기화 후 매 순간 최댓값이 바뀌는지 체크하는 구조로 확인
def solution(sequence):
    t1 = [1, -1]  # 1,-1,1...
    t2 = [-1, 1]  # -1,1,-1...
    s = sequence

    i, j = divmod(len(s), 2)
    t1 += [1, -1] * (i - 1)
    t2 += [-1, 1] * (i - 1)

    t1 += [1] * j
    t2 += [-1] * j

    a = []
    b = []

    if len(s) == 1:
        t1 = [1]
        t2 = [-1]

    a_c = 0
    b_c = 0

    result = 0

    for k in range(len(s)):
        a_c += t1[k] * s[k]
        b_c += t2[k] * s[k]

        if a_c < 0:
            a_c = 0
        if b_c < 0:
            b_c = 0

        if result < a_c:
            result = a_c
        elif result < b_c:
            result = b_c
    return result

# 내 풀이(개선 중)
# 이분탐색 접근 생각
def solution(sequence):
    t1 = [1, -1]  # 1,-1,1...
    t2 = [-1, 1]  # -1,1,-1...
    result = []
    s = sequence

    i, j = divmod(len(s), 2)
    t1 += [1, -1] * (i - 1)
    t2 += [-1, 1] * (i - 1)

    t1 += [1] * j
    t2 += [-1] * j

    a = []
    b = []

    result = []

    if len(s) == 1:
        t1 = [1]
        t2 = [-1]

    for k in range(len(s)):
        a.append(t1[k] * s[k])
        b.append(t2[k] * s[k])

    start = 0
    end = 0

    while start < len(s) - 1:
        one = sum(a[start:end + 1])
        two = sum(b[start:end + 1])

        result.append(one)
        result.append(two)

        if start == end and end < len(s) - 1:
            end += 1
        else:
            if end < len(s) - 1:
                end += 1
            elif end == len(s) - 1:
                start += 1
                end = start

                if end == len(s) - 1:
                    result.append(a[end])
                    result.append(b[end])
                    break

    return max(result)

# 다른 사람 풀이
def solution(sequence):

    # 1 부터 연속펄스 부분 수열을 곱한값 찾기 prefix sum 만들기
    # maxV - minV
    # 각각의 리스트에서 max()
    answer = 0
    prefixS = [0]
    for i in range(len(sequence)):
        pulse = 1 if i%2 ==0  else -1
        prefixS.append(prefixS[-1]+pulse*sequence[i])


    return abs(max(prefixS) - min(prefixS))