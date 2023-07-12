# 내 풀이
def solution(a, b):
    count=0
    for x in zip(a,b):
        count+=x[0]*x[1]
    return count

# 다른 사람 풀이
def solution(a, b):

    return sum([x*y for x, y in zip(a,b)])