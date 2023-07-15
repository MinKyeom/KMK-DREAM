# 내 풀이
def solution(answers):
    num_1 = "12345"
    num_2 = "21232425"
    num_3 = "3311224455"
    result_1 = 0
    result_2 = 0
    result_3 = 0
    k = len(answers)
    if k < 5:
        num_1 = num_1[0:k]
    if k < 8:
        num_2 = num_2[0:k]
    if k < 10:
        num_3 = num_3[0:k]

    for x in range(k):
        if k > 5 and x % 5 == 0:
            p = num_1[0:1]
            num_1 = num_1 + p
        elif k > 5:
            f = (x % 5)
            p = num_1[f:f + 1]
            num_1 = num_1 + p

        if k > 8 and x % 8 == 0:
            q = num_2[0:1]
            num_2 = num_2 + q
        elif k > 8:
            e = (x % 8)
            q = num_2[e:e + 1]
            num_2 = num_2 + q
        if k > 10 and x % 10 == 0:
            r = num_3[0:1]
            num_3 = num_3 + r
        elif k > 10:
            g = (x % 10)
            q = num_3[g:g + 1]
            num_3 = num_3 + q

    a = list(num_1)
    b = list(num_2)
    c = list(num_3)

    for x in range(len(answers)):
        if answers[x] == int(a[x]):
            result_1 += 1
        if answers[x] == int(b[x]):
            result_2 += 1
        if answers[x] == int(c[x]):
            result_3 += 1
    k = [[result_1, 1], [result_2, 2], [result_3, 3]]
    k.sort(reverse=True)
    result = []
    check = []

    for v, w in k:
        if len(result) == 0:
            result.append(w)
            check.append(v)
        if max(check) == v:
            result.append(w)
        else:
            continue
    result = list(set(result))
    result.sort()

    return result

# 다른 사람 풀이
def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result
