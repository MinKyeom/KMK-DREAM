"""
출처: 프로그래머스
https://school.programmers.co.kr/learn/courses/30/lessons/68646
"""
# 내 풀이(개선 중)
"""
맨 끝에 두 개는 항상 살아남음 

"""
def solution(a):
    result = []

    if len(a) >= 3:
        for i in range(1, len(a) - 1):
            num = a[i]

            # 좌
            count_left = 0
            for l in range(i):
                if a[l] < num:
                    count_left += 1
                    if count_left >= 2:
                        break
            # 우
            count_right = 0
            for r in range(i + 1, len(a)):
                if a[r] < num:
                    count_right += 1
                    if count_right >= 2:
                        break

            if count_left == 0 and count_right >= 1:
                result.append(num)
            elif count_right == 0 and count_left >= 1:
                result.append(num)
            elif count_right == 0 and count_left == 0:
                result.append(num)

    return len(set(result)) + 2

# 내 풀이(개선 중)
"""
맨 끝에 두 개는 항상 살아남음 

"""
def solution(a):
    result = []

    if len(a) >= 3:
        for i in range(1, len(a) - 1):
            num = a[i]
            left = float("inf")
            right = float("inf")

            # 좌
            for l in range(i):
                left = min(left, a[l])

            # 우
            for r in range(i + 1, len(a)):
                right = min(right, a[r])

            if right < num and left < num:
                continue
            else:
                result.append(num)

    return len(set(result)) + 2