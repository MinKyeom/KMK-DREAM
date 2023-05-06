# 내 풀이
def solution(numbers):
    numbers.sort()
    return numbers[len(numbers)-1]*numbers[len(numbers)-2]

# 다른 사람 풀이

def solution(numbers):
    numbers.sort()
    return numbers[-2] * numbers[-1]