# 내 풀이
def solution(numbers):
    for a in range(len(numbers)):
        numbers[a] = numbers[a] * 2

    return numbers
# 다른 사람 풀이
def solution(numbers):
    return [num*2 for num in numbers]