# 내 풀이
def solution(prices):
    p = prices
    result = []
    for a in range(len(prices) - 1):
        num = p[a]
        count = 0
        flag = False
        for b in range(a + 1, len(p)):
            count += 1
            if p[b] < num:
                result.append(count)
                flag = True
                break

        if flag == False:
            result.append(count)
    result.append(0)

    return result

# 다른 사람 풀이
def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            answer[i] += 1
            if prices[i] > prices[j]: break
    return answer