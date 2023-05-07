# 내 풀이
def solution(n):
    count=1
    while True:
        if (6*count)%n==0:
            return count
        else:count+=1

# 다른 사람 풀이
import math

def solution(n):
    return (n * 6) // math.gcd(n, 6) // 6