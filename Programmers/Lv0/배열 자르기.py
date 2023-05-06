# 내 풀이
def solution(numbers, num1, num2):
    result = []
    for x in range(num1, num2 + 1):
        result.append(numbers[x])

    return result

# 다른 사람 풀이

def solution(numbers, num1, num2):
    return numbers[num1:num2+1]