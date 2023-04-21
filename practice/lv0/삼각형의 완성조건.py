# 풀이1
def solution(sides):
    answer = 0
    a = sides[0] + sides[1]
    b = sides[1] + sides[2]
    c = sides[0] + sides[0]
    if a <= sides[2]:
        return 2
    if b <= sides[0]:
        return 2

    if c <= sides[1]:
        return 2

    return 1

# 풀이 2



def solution(sides):
    return 1 if max(sides) < (sum(sides) - max(sides)) else 2