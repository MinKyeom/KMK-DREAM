# 내 풀이
def solution(n):
    a = str(n)
    b = list(a)
    count = 0

    for x in range(len(b)):
        count += int(b[x])

    answer = count
    return answer

# 다른 사람들 풀이 best

def solution(n):
    answer = sum(list(map(int,list(str(n)))))
    return answer