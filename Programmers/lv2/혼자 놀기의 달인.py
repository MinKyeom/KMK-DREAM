# 내 풀이
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
