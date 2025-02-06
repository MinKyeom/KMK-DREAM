"""
출처:프로그래머스,
https://school.programmers.co.kr/learn/courses/30/lessons/12899

"""

# 풀이 과정
# 1.재귀로 연속으로 숫자를 바꾸기
# 2.조합으로 생각 후 연속 된 숫자를 나눠서 위치로 숫자 찾기
# 1.재귀로 연속으로 숫자를 바꾸기
# 2.조합으로 생각 후 연속 된 숫자를 나눠서 위치로 숫자 찾기
def solution(n):
    k = ["1", "2", "4"]
    result = ""
    num = n
    count = 1  # 자릿수 파악

    while num > 0:
        num -= 3 ** (count)

        if num > 0:
            count += 1

    for a in range(1, count):
        n -= 3 ** a

    while count > 1:
        i, j = divmod(n, 3 ** (count - 1))
        if j == 0:
            result += k[i - 1]
        else:
            result += k[i]
        n = n % (3 ** (count - 1))
        count -= 1

    if count == 1:
        i, j = divmod(n - 1, 3)
        result += k[j]

    return result

# 다른 사람 풀이
def change124(n):
    num = ['1','2','4']
    answer = ""

    while n > 0:
        n -= 1
        answer = num[n % 3] + answer
        n //= 3

    return answer


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(change124(10))
