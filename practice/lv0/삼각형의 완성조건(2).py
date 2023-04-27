# 내 풀이

def solution(sides):
    result = []
    for x in range(1, sides[0] + sides[1]):
        if x + sides[0] > sides[1] and x + sides[1] > sides[0]:
            result.append(x)
        else:
            continue

    return len(result)


# 다른 사람 풀이

def solution(sides):
    return sum(sides) - max(sides) + min(sides) - 1