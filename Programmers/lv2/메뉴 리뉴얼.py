"""
출처:프로그래머스,
https://school.programmers.co.kr/learn/courses/30/lessons/72411
"""
# 풀이 과정
def solution(orders, course):
    from collections import Counter
    from itertools import combinations
    # menu=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    result = []
    k = {}

    for a in orders:
        b = list(a)

        for c in course:
            d = list(combinations(b, c))

            for e in d:
                e = sorted(list(e))
                e = "".join(e)
                if e in k:
                    k[e] += 1

                else:
                    k[e] = 1

    set_menu = {}

    for f in k:
        if k[f] < 2:
            continue

        else:
            set_menu[f] = k[f]

    course_menu = []

    for g in course:
        t = []
        for h in set_menu:
            if len(h) == g:
                if len(t) == 0:
                    t.append(h)
                else:
                    if set_menu[h] > set_menu[t[-1]]:
                        t.clear()
                        t.append(h)
                    elif set_menu[h] == set_menu[t[-1]]:
                        t.append(h)

        course_menu = course_menu + t

    # course_menu=sorted(course_menu, key=len,reverse=True)
    course_menu.sort()

    for i in orders:
        last_check = []
        for j in course_menu:
            if set(i) | set(j) == set(i) and j not in result:
                last_check.append(j)

        # print(last_check)

        result = result + last_check

    result.sort()

    return result

# 다른 사람 풀이
import collections
import itertools

def solution(orders, course):
    result = []

    for course_size in course:
        order_combinations = []
        for order in orders:
            order_combinations += itertools.combinations(sorted(order), course_size)

        most_ordered = collections.Counter(order_combinations).most_common()
        result += [ k for k, v in most_ordered if v > 1 and v == most_ordered[0][1] ]

    return [ ''.join(v) for v in sorted(result) ]