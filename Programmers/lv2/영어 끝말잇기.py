"""
출처:프로그래머스,
https://school.programmers.co.kr/learn/courses/30/lessons/12981
"""
# 풀이 과정
def solution(n, words):
    count = 1
    all_count = 1
    check = []
    for k in range(len(words)):
        if k == 0:
            check.append(words[k])
            count += 1
            continue

        if check[-1][-1] == words[k][0] and not words[k] in check:
            check.append(words[k])
            if count < n:
                count += 1
                all_count += 1
            else:
                count = 1
                all_count += 1

        else:
            return [count, int(all_count / n) + 1]

    return [0, 0]


# 다른 사람 풀이
def solution(n, words):
    for p in range(1, len(words)):
        if words[p][0] != words[p-1][-1] or words[p] in words[:p]: return [(p%n)+1, (p//n)+1]
    else:
        return [0,0]
