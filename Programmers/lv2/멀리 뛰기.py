# 내 풀이(개선 중)
def solution(n):
    i = n  # 1숫자 공의 개수
    r = 0  # 2숫자 공의 개수
    c = r + i
    check = int(n // 2)
    result = 0

    while r <= check:

        # print(i,r,result)

        if r == 0:
            result += 1
            r += 1
            i -= 2
        else:
            check_r = r
            check_c = (i + r)
            cal_a = 1  # 분자
            cal_b = 1  # 분모
            for k in range(r):
                cal_a *= check_c
                cal_b *= check_r
                check_c -= 1
                check_r -= 1

            result += int(cal_a // cal_b)
            r += 1
            i -= 2

    return int(result) % 1234567
# 다른 사람 풀이

def jumpCase(num):
    a, b = 1, 2
    for i in range(2,num):
        a, b = b, a+b
    return b

#아래는 테스트로 출력해 보기 위한 코드입니다.
print(jumpCase(4))
