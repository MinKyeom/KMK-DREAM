# 내 풀이
def solution(n):
    a = str(n)
    b = list(a)
    count = 0

    for x in range(len(b)):
        count += int(b[x])

    answer = count
    return answer

# 내 풀이2
def solution(n):
    a=list(str(n))
    print(a)
    result=0
    for x in range(len(a)):
        result+=int(a[x])
    answer = result
    return answer


# 팀원 풀이
def solution(n):
    return sum(map(int, iter(str(n))))

# 다른 사람들 풀이 best

def solution(n):
    answer = sum(list(map(int,list(str(n)))))
    return answer