# 내 풀이
def solution(array):
    array.sort()
    print(array)
    x=int(len(array)/2)
    return array[x]

# 다른 사람 풀이

def solution(array):
    return sorted(array)[len(array) // 2]