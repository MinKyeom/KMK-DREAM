# 풀이 1

def solution(numbers):
    answer = 0
    list = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for x in range(len(list)):
        numbers = numbers.replace(list[x], str(x))

    answer = int(numbers)

    return answer

# 풀이 2

def solution(numbers):
    for num, eng in enumerate(["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
        numbers = numbers.replace(eng, str(num))
    return int(numbers)