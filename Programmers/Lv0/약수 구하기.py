# 풀이1
def solution(n):
    answer = []
    for x in range(1, n + 1):
        if n % x == 0:
            answer.append(x)

    answer.sort()
    return answer
# 풀이 2
def solution(n):
    answer=[]
    for a in range(1,n+1):
        if n%a==0:
            answer.append(a)
        else:continue

    return answer


# 팀원 풀이
def solution(n):
    return [1, *[x for x in range(2, n+1) if n % x == 0]]
    # 위의 문장 해석!
#  다른 사람 풀이

def solution(n):
    answer = [i for i in range(1, n + 1) if n % i == 0]
    return answer