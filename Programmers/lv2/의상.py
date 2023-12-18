# 내 풀이(개선 중)
def solution(clothes):
    from itertools import combinations
    result = 0

    check = [k for k in range(len(clothes))]

    for a in range(1, len(clothes) + 1):  # 갖춰입는 옷의 종류 개수
        c = list(combinations(check, a))

        if a == 1:
            count = 0
            for b in c:
                for d in b:
                    result += len(clothes[d]) - 1

        else:
            for b in c:  # 종류 조합
                print(b)
                count = 1
                for d in b:
                    count *= len(clothes) - 1

            result += count

    print(result)
    answer = 0
    return answer

