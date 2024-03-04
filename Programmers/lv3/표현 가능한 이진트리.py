# 내 풀이(개선 중)
# 이진트리 표현가능:1  불가능:0
# 이진수를 보고 트리 모양 결정 후 더미 위치가 문제가 안되는지 체크 후
# 기본 트리 모양을 찾은 후 비교할 트리와 비교
# 높이를 기준으로 나머지를 통해 더미 여부 확인
# 더미가 아니어야 될 위치에 더미가 된다면 0 그렇지 않다면 1
def solution(numbers):
    n = numbers
    result = []
    for i in n:
        k = bin(i)[2:]
        t = len(k)
        count = 0
        check = 0

        while t > 0:
            check += 2 ** count
            t = t - 2 ** count
            count += 1
        h = count + 1  # 트리 높이
        print(check)
        break

    answer = []
    return answer