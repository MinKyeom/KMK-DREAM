"""
출처: 프로그래머스 코딩 테스트 연습,
https://school.programmers.co.kr/learn/courses/30/lessons/120890
"""
# 풀이 1

def solution(array, n):
    answer = 0
    num = []
    num_abs = []
    for x in range(len(array)):
        a = abs(array[x] - n)
        if len(num) == 0:
            num.append(array[x])
            num_abs.append(a)

        elif len(num) == 1:
            if num_abs[0] > a:
                num.pop()
                num.append(array[x])
                num_abs.pop()
                num_abs.append(a)
            elif num_abs[0] == a:
                if array[x] < num[0]:
                    num.pop()
                    num.append(array[x])
                    num_abs.pop()
                    num_abs.append(a)

            elif num_abs[0] <= a:
                continue
    answer = num[0]


# 풀이 2

solution=lambda a,n:sorted(a,key=lambda x:(abs(x-n),x))[0]



