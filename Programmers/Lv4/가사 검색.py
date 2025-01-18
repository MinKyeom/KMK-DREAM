"""
출처:프로그래머스,
https://school.programmers.co.kr/learn/courses/30/lessons/60060
"""

# 풀이 과정_개선 중
from collections import defaultdict


def check(w, song, k, new):
    # 접두사
    if w[0] == "?":
        if new == song[k:]:
            return True
        else:
            return False

    # 접미사
    else:
        if new == song[:len(song) - k]:
            return True

        else:
            return False


def solution(words, queries):
    words_check = defaultdict(set)

    for q in queries:
        words_check[q] = set([])

    for w in words_check.keys():
        k = w.count("?")

        if w[0] == "?":
            new = w[k:]

        else:
            new = w[:len(w) - k]

        for song in words:
            if song in words_check[w]:
                continue

            if len(w) == len(song) and check(w, song, k, new):
                words_check[w].add(song)

            else:
                continue

    result = []

    for q in queries:
        result.append(len(words_check[q]))

    return result