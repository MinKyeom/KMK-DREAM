"""
출처: 프로그래머스,
https://school.programmers.co.kr/learn/courses/30/lessons/12904
"""

# 풀이 과정
def solution(s):
    k = s[::-1]

    result = 0

    for start in range(len(s)):
        for end in range(start + 1, len(s) + 1):
            k = s[start:end]
            if k == k[::-1]:
                result = max(result, len(k))

    return result

# 다른 사람 풀이
def longest_palindrom(s):
    for i in range(len(s),0,-1):
        for j in range(len(s)-i+1):
            if s[j:j+i] == s[j:j+i][::-1]:
                return i