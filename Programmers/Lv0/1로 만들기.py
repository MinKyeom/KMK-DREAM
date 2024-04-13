"""
출처: 프로그래머스 코딩 테스트 연습,
https://school.programmers.co.kr/learn/courses/30/lessons/181880
"""
# 내 풀이
def solution(num_list):
    count = 0
    for x in range(len(num_list)):
        while True:
            if num_list[x] % 2 == 0 and not num_list[x] == 1:
                num_list[x] = num_list[x] / 2
                count += 1
            elif num_list[x] % 2 == 1 and not num_list[x] == 1:
                num_list[x] = (num_list[x] - 1) / 2
                count += 1

            if num_list[x] == 1:
                break

    return count

# 다른 사람 풀이

def solution(num_list):
    return sum(len(bin(i)) - 3 for i in num_list)