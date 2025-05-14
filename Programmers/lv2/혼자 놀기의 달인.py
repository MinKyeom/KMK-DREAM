"""
출처:프로그래머스,
https://school.programmers.co.kr/learn/courses/30/lessons/131130
"""

# 풀이 과정
def solution(cards):
    result = []
    for k in range(len(cards)):  # k는 처음 박스 번호
        box_1 = []
        a = cards[k]
        while True:
            if not cards[a - 1] in box_1:
                box_1.append(cards[a - 1])
                a = cards[a - 1]
            else:
                score_1 = len(box_1)
                break

        check_2 = set(cards) - set(box_1)

        if score_1 == len(cards):
            result.append(0)
            continue

        for t in check_2:
            box_2 = []
            box_2.append(t)
            while True:
                if not cards[t - 1] in box_1 and not cards[t - 1] in box_2:
                    box_2.append(cards[t - 1])
                    t = cards[t - 1]
                else:
                    score_2 = len(box_2)
                    break
            result.append(score_1 * score_2)

    return max(result)

# 다른 사람 풀이
def solution(cards):
    answer = []
    for i in range(len(cards)):
        tmp = []
        while cards[i] not in tmp:
            tmp.append(cards[i])
            i = cards[i] - 1
        answer.append([] if sorted(tmp) in answer else sorted(tmp))
    answer.sort(key=len)

    return len(answer[-1]) * len(answer[-2])

# 다른 사람 풀이
def solution(cards):
    temp_group = []
    temp_all_nums = []

    for x in cards:
        if x in temp_all_nums:
            continue
        temp_box = [x]
        temp_value = x
        while True:
            temp_value = cards[temp_value-1]
            if temp_value in temp_box:
                break
            temp_box.append(temp_value)
        temp_all_nums += temp_box
        temp_group.append(temp_box)    

    points = sorted(list(map(len, temp_group)), reverse = True)
    if len(temp_group[0]) == len(cards):
        return 0
    point = points[0] * points[1]

    return point
