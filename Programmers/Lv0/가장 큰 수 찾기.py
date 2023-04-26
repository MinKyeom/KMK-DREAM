# 풀이 1
def solution(array):
    answer = []
    x = max(array)
    answer.append(x)
    y = array.index(max(array))
    answer.append(y)
    return answer

# 내 풀이 2

def solution(array):
    answer = []
    x = max(array)
    answer.append(x)
    y = array.index(x)
    answer.append(y)

    return answer
# 팀원 풀이
def solution(array):
    max_i = max((i for i in range(len(array))), key=lambda i: array[i])
    return [array[max_i], max_i]
# 다른 사람 풀이
def solution(array):
    return [max(array), array.index(max(array))]