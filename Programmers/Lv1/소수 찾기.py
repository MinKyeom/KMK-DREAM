# 내 풀이
def solution(n):
    result = 0
    for y in range(2, n + 1):
        count = 0
        k = int(y ** (1 / 2))
        for z in range(1, k + 1):
            if y % z == 0:
                count += 1
            elif count >= 2:
                break
        if count == 1:
            result += 1

    return result

# 다른 사람 풀이
def solution(n):
    num=set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)