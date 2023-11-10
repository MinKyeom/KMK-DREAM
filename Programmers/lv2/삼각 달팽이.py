# 내 풀이 (개선 중)
# 처음 배열을 false를 활용한 후 해당 상황에 맞는 값을 false 체크 후 없으면 채워 넣고 삼각형 완성!
def solution(n):
    result = [[] for a in range(n)]
    count = 0
    all_count = n  # 순회에 따른 숫자를 넣을 개수
    sam_count = 0  # 삼각형 순회 횟수
    sam = 0  # 0 삼각형 좌변 1 삼각형 밑변 2 삼각형 우변
    down = n - 1  # 삼각형 밑변 위치(변화 체크)

    while count <= int((n * (n + 1)) / 2):

        if sam == 0:  # 좌변
            for a in range(sam_count, all_count):
                count += 1
                result[a].append(count)

            sam_count += 1
            all_count -= 1
            sam = 1

        elif sam == 1:  # 밑변
            for b in range(all_count):
                count += 1
                result[down].append(count)

            down -= 1
            sam_count += 1
            all_count -= 1
            sam = 2

        elif sam == 2:
            k = int(sam_count / 3) + 1
            for c in range(down, k - 1, -1):
                count += 1
                result[c].append(count)

            sam_count += 1
            all_count -= 1
            sam = 0
            break

    print(result)

    return result

# 다른 사람 풀이
