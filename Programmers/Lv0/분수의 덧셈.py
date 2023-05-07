# 내 풀이
def solution(numer1, denom1, numer2, denom2):
    x=denom1*denom2
    y=(numer1*denom2)+(numer2*denom1)
    z=max(x,y)
    count=2
    while count<=z:
        if x%count==0 and y%count==0:
            x=x/count
            y=y/count
        else:count+=1
    return [y,x]

# 다른 사람 풀이
import math

def solution(denum1, num1, denum2, num2):
    denum = denum1 * num2 + denum2 * num1
    num = num1 * num2
    gcd = math.gcd(denum, num)
    return [denum//gcd, num//gcd]