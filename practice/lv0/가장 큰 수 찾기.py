# 풀이 1
def solution(array):
    answer = []
    x = max(array)
    answer.append(x)
    y = array.index(max(array))
    answer.append(y)
    return answer

# 다른 사람 풀이
def solution(array):
    return [max(array), array.index(max(array))]