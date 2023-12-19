# 내 풀이
# 선택하지 않는 경우의 수 추가 후 그걸 제외!!
def solution(clothes):
    from itertools import combinations
    from collections import deque

    result = 1

    check = {}

    n = []  # 옷 종류 분류

    # dic 내의 종류별 옷 분류

    for c in clothes:
        if c[-1] not in check:
            check[c[-1]] = 1
            n.append(c[-1])

        else:
            check[c[-1]] += 1

    # print(check)

    final = []  # 확인 할 조합 수

    #     for a in range(1,len(n)+1):
    #         new=map(list,list(combinations(n,a)))
    #         final+=new

    #     final=deque(final)

    #     while final:
    #         num=final.pop()

    #         if len(num)==1:
    #             result+=check[num[0]]
    #         else:
    #             count=1
    #             for b in num:
    #                 count*=check[b]

    #             result+=count

    for t in check:
        result *= (check[t] + 1)

    return result - 1

# 다른 사람 풀이
def solution(clothes):
    from collections import Counter
    from functools import reduce
    cnt = Counter([kind for name, kind in clothes])
    answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1
    return answer