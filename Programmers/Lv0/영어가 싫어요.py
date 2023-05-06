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
    num=["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    count=0
    for x in num:
        numbers=numbers.replace(x,str(count))
        count+=1
    answer = int(numbers)
    return answer

# 팀원 풀이
import re
def solution(numbers):
    num_str = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    pattern = re.compile("|".join(num_str))
    num_map = {s: str(i) for s, i in zip(num_str, range(10))}
    return int("".join((num_map[x.group()] for x in re.finditer(pattern, numbers))))

# 다른 사람 풀이 2
def solution(numbers):
    for num, eng in enumerate(["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
        numbers = numbers.replace(eng, str(num))
    return int(numbers)