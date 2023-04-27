#풀이1
def solution(n):
    x=1
    y=1
    while y<=n:
        if not x==0 and x%3==0 or str(x).count(str(3))>=1:
            x+=1
            continue
        if y==n:
            return x
        x+=1
        y+=1


# 다른 사람 풀이

def solution(n):
    answer = 0
    for _ in range(n):
        answer += 1
        while answer % 3 == 0 or '3' in str(answer):
            answer += 1
    return answer