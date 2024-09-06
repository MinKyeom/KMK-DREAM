"""
출처:프로그래머스
https://school.programmers.co.kr/learn/courses/30/lessons/43163
"""
# 내 풀이
from collections import deque
import copy


def solution(begin, target, words):
    english = list("abcdefghijklmnopqrstuvwxyz")
    words = set(words)

    if target not in words:
        return 0
    elif len(target) != len(begin):
        return 0

    max_count = len(begin)
    result = []
    q = deque([(begin, 0)])
    check = set([])
    check.add(begin)

    while q:
        start, count = q.popleft()
        check.add(start)

        if start == target:
            result.append(count)

        change_words = list(start)

        for change in range(len(begin)):
            for eng in english:
                new = copy.deepcopy(change_words)
                new[change] = eng
                new_words = str("".join(new))

                if not new_words in check and new_words in words:
                    q.append((new_words, count + 1))

    return min(result)