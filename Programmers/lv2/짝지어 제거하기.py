"""
출처:프로그래머스,
https://school.programmers.co.kr/learn/courses/30/lessons/12973
"""
# 풀이 과정
def solution(s):
    from collections import deque

    k = deque(list(s))
    c = 0
    check = []

    while k:
        a = k.popleft()
        if check:
            if check[-1] == a:
                check.pop()
                while check:
                    if len(check) >= 2:
                        if check[-1] == check[-2]:
                            check.pop()
                            check.pop()
                        else:
                            break
                    else:
                        break
            else:
                check.append(a)

        else:
            check.append(a)

    return 1 if len(check) == 0 else 0

# 다른 사람 풀이
def solution(s):
    temp = ["",s[0]]

    for i in s[1:]:
        if temp[-1]!=i:
            temp.append(i)
        else:
            temp.pop()

    return 1 if len(temp)==1 else 0
