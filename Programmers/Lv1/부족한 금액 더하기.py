# 내 풀이
def solution(price, money, count):
    a=0
    for x in range(1,count+1):
        a+=price*x
    return abs(a-money) if money<=a else 0

# 다른 사람 풀이
def solution(price, money, count):
    return max(0,price*(count+1)*count//2-money)

