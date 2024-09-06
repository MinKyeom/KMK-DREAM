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

# 다른 사람 풀이
from collections import deque


def get_adjacent(current, words):
    for word in words:
        if len(current) != len(word):
            continue

        count = 0
        for c, w in zip(current, word):
            if c != w:
                count += 1

        if count == 1:
            yield word


def solution(begin, target, words):
    dist = {begin: 0}
    queue = deque([begin])

    while queue:
        current = queue.popleft()

        for next_word in get_adjacent(current, words):
            if next_word not in dist:
                dist[next_word] = dist[current] + 1
                queue.append(next_word)

    return dist.get(target, 0)