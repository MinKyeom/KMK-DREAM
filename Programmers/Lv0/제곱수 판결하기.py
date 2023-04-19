# 프로그래머스 다른 사람 풀이도 볼 수 있다 맞추면

# 풀이1

def solution(n):
    answer=0
    for a in range(1000000+1):
        b=a*a
        if b==n:
            answer=1
            break
        else:
            answer=2
    return answer

# 풀이2

import math
def solution(n):
    nn = int(math.sqrt(n))
    return 2 - (nn*nn == n)


