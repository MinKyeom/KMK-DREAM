# 내 풀이
def solution(array, height):
    array.append(height)
    array.sort()
    array.reverse()
    return array.index(height)
# 다른 사람 풀이
def solution(array, height):
    array.append(height)
    array.sort(reverse=True)
    return array.index(height)

