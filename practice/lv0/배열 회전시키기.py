# 내 풀이
def solution(numbers, direction):
    result = []
    for x in range(len(numbers)):
        result.append(0)
    for a in range(len(numbers)):
        if direction == "right":
            print(1)
            if a + 1 == len(numbers):
                result[0] = numbers[len(numbers) - 1]
            else:
                result[a + 1] = numbers[a]
        elif direction == "left":
            result[a - 1] = numbers[a]

    return result

# 다른 사람 풀이

def solution(numbers, direction):
    return [numbers[-1]] + numbers[:-1] if direction == 'right' else numbers[1:] + [numbers[0]]