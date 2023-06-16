# 내 풀이
def solution(names):
    result = []
    for x in range(len(names)):
        if (x + 1) % 5 == 1:
            result.append(names[x])

    answer = result
    return answer

# 다른 사람 풀이
def solution(names):
    answer1 = names[:1]
    answer2 = names[5:6]
    answer3 = names[10:11]
    answer4 = names[15:16]
    answer5 = names[20:21]
    answer6 = names[25:26]
    answer7 = names[30:31]
    answer = answer1 +answer2+answer3+answer4+answer5+answer6+answer7
    return answer