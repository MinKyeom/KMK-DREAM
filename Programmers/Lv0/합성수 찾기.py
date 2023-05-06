# 내 풀이
def solution(n):
    num_list = []
    result = []
    count = 0
    for a in range(1, n + 1):
        num_list.append(a)

    for b in num_list:
        count = 0
        for c in range(1, b + 1):
            if b % c == 0:
                count += 1
            if count == 3:
                result.append(b)
                break
    return len(result)

# 다른 사람 풀이
def solution(n):
    output = 0
    for i in range(4, n + 1):
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                output += 1
                break
    return output