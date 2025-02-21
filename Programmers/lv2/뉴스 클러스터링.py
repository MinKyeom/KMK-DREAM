"""
출처:프로그래머스,
https://school.programmers.co.kr/learn/courses/30/lessons/17677
"""
# 풀이 과정
def solution(str1, str2):
    # a,b 모두 공집합일 경우 자카드 유사도 1로 정의

    eng = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    eng = list(eng)

    str1 = list(str1.upper())
    str2 = list(str2.upper())

    a = []  # str1 집합
    b = []  # str2 집합

    u = 0
    n = 0

    for i in range(len(str1) - 1):
        new = ""
        if str1[i] in eng:
            new += str1[i]
        else:
            continue

        if str1[i + 1] in eng:
            new += str1[i + 1]
        else:
            continue

        a.append(new)

    for i in range(len(str2) - 1):
        new = ""
        if str2[i] in eng:
            new += str2[i]
        else:
            continue

        if str2[i + 1] in eng:
            new += str2[i + 1]
        else:
            continue

        if new in a:
            u += 1
            n += 1
            k = a.index(new)
            del a[k]
        else:
            u += 1

    u += len(a)

    if u == 0 and n == 0:
        return 65536
    else:
        return int((n / u) * 65536)

# 다른 사람 풀이
import re
import math

def solution(str1, str2):
    str1 = [str1[i:i+2].lower() for i in range(0, len(str1)-1) if not re.findall('[^a-zA-Z]+', str1[i:i+2])]
    str2 = [str2[i:i+2].lower() for i in range(0, len(str2)-1) if not re.findall('[^a-zA-Z]+', str2[i:i+2])]

    gyo = set(str1) & set(str2)
    hap = set(str1) | set(str2)

    if len(hap) == 0 :
        return 65536

    gyo_sum = sum([min(str1.count(gg), str2.count(gg)) for gg in gyo])
    hap_sum = sum([max(str1.count(hh), str2.count(hh)) for hh in hap])

    return math.floor((gyo_sum/hap_sum)*65536)