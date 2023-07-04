# 내 풀이
def solution(food):
    answer_1 = ''
    answer_2 = ""
    for x in range(1, len(food)):
        if not food[x] % 2 == 0:
            food[x] = food[x] - 1
        else:
            continue
    count = 1
    for y in range(1, len(food)):
        k = food[y]
        for z in range(int(k / 2)):
            answer_1 = answer_1 + str(count)
        count += 1
    answer_2 = answer_1[::-1]
    result = answer_1 + str(0) + answer_2

    return result

# 다른 사람 풀이
def solution(food):
    answer ="0"
    for i in range(len(food)-1, 0,-1):
        c = int(food[i]/2)
        while c>0:
            answer = str(i) + answer + str(i)
            c -= 1
    return answer
