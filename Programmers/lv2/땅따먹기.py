# 내 풀이
# 통째로 사고하기!!
# 하나 하나씩 골라서 생각하는게 아닌 모두 수에 최대값을 추린 후 거듭 더해준 후 그 중 최대값을!!

def solution(land):
    for i in range(1, len(land)):
        for j in range(4):
            land[i][j] += max(land[i - 1][:j] + land[i - 1][j + 1:])

    return max(land[len(land) - 1])


"""
def solution(land):

    for i in range(1,len(land)):
        for j in range(len(land[0])):
            land[i][j] += max(land[i-1][:j] + land[i-1][j+1:])

    return max(land[len(land)-1])
"""

# 다른 사람 풀이
def solution(land):

    for i in range(1, len(land)):
        for j in range(len(land[0])):
            land[i][j] = max(land[i -1][: j] + land[i - 1][j + 1:]) + land[i][j]

    return max(land[-1])