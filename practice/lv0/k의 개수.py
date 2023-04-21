# 풀이 1
def solution(i, j, k):
    answer = 0
    num = []
    for x in range(i, j + 1):
        num.append(str(x))

    a = "".join(num)

    return a.count(str(k))

# 풀이 2

def solution(i, j, k):
    answer = sum([ str(i).count(str(k)) for i in range(i,j+1)])
    return answer