"""
출처:프로그래머스,
https://school.programmers.co.kr/learn/courses/30/lessons/181864
"""
# 내 풀이
def solution(myString, pat):
    x = list(myString)
    for k in range(len(x)):
        if x[k] == "A":
            x[k] = "B"
        else:
            x[k] = "A"
    if pat in "".join(x):
        return 1
    else:
        return 0

    print(x)
    answer = 0
    return answer

# 다른 사람 풀이
def solution(myString, pat):
    return int(pat in myString.replace('A', 'C').replace('B', 'A').replace('C', 'B'))