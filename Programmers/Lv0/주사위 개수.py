# 내 풀이
def solution(box, n):
    x = int(box[0] / n)
    y = int(box[1] / n)
    z = int(box[2] / n)

    answer = x * y * z
    return answer

# 다른 사람 풀이

def solution(box, n):
    x, y, z = box
    return (x // n) * (y // n) * (z // n )