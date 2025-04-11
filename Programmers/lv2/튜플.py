"""
출처:프로그래머스,
https://school.programmers.co.kr/learn/courses/30/lessons/64065
"""
# 풀이 과정
def solution(s):
    from collections import deque

    s = s[1:len(s) - 1]
    k = deque(list(s))

    before = []

    while k:
        a = k.popleft()

        if a == "{":
            check = []
            num = ""

            while k:
                b = k.popleft()

                if b == ",":
                    check.append(num)
                    num = ""

                elif b == "}":
                    check.append(num)
                    before.append(check)
                    break

                else:
                    num += b

    before.sort(key=len)

    result = []

    for t in before:
        for v in t:
            if not int(v) in result:
                result.append(int(v))

    return result

# 다른 사람 풀이
def solution(s):

    s = Counter(re.findall('\d+', s))
    return list(map(int, [k for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True)]))

import re
from collections import Counter