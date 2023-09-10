# 내 풀이
def solution(k, ranges):
    count = 0
    fun = [[0, k]]

    while True:
        if k == 1:
            break
        count += 1
        if k % 2 == 0:
            k = k / 2
            fun.append([count, k])
        else:
            k = k * 3 + 1
            fun.append([count, k])
    result = []

    for a, b in ranges:
        s = 0

        if count + b < a:
            result.append(-1)
            continue

        for c in range(a, count + b):
            if a > count + b:
                result.append(-1)
                break
            if c >= len(fun) - 1 or c < 0:
                result.append(-1)
                break
            elif c <= len(fun) - 2:
                if c < 0:
                    s = -1
                    result.append(-1)
                    break
                k = ((abs(fun[c + 1][1] + fun[c][1])) / 2)
                s += k
        if s != -1:
            result.append(s)

    return result

# 다른 사람 풀이

def solution(k, ranges):
    answer = []
    arr = [k]
    while k > 1:
        if not k % 2: k //= 2
        else: k = k*3+1
        arr.append(k)
    area = [0]
    for i in range(len(arr)-1):
        area.append(area[-1]+(arr[i]+arr[i+1])/2)
    for a, b in ranges:
        if a >= len(area) or b-1 < -len(area): answer.append(-1)
        elif area[b-1]-area[a] < 0: answer.append(-1)
        else: answer.append(area[b-1]-area[a])
    return answer