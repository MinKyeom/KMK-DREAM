# 내 풀이(개선 중)
def solution(n):
    from itertools import combinations
    result = 1

    if n % 2 == 1:
        flag = False
    else:
        flag = True

    k = int(n / 2)
    print(k)

    #     for a in range(1,k+1):
    #         result+=len(list(combinations(n-a,a)))

    return result

# 다른 사람 풀이