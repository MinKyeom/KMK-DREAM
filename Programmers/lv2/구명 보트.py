"""
출처:프로그래머스,
https://school.programmers.co.kr/learn/courses/30/lessons/42885
"""
# 풀이 과정
def solution(people, limit):
    from collections import deque

    answer = 0

    people.sort(reverse=True)
    people = deque(people)

    while people:
        a = people.popleft()

        if len(people) > 0:
            b = people.pop()
        else:
            b = 0

        if a + b > limit:
            people.append(b)

        answer += 1

    return answer

# 다른 사람 풀이
def solution(people, limit) :
    answer = 0
    people.sort()

    a = 0
    b = len(people) - 1
    while a < b :
        if people[b] + people[a] <= limit :
            a += 1
            answer += 1
        b -= 1
    return len(people) - answer
