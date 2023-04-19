# 리턴값에 한 번에 쓰는 연습 

# 풀이 1
def solution(n, t):
    a=n*(2**t)
    answer = a
    return answer

# 풀이 2

def solution(n, t):
    return n * 2 ** t