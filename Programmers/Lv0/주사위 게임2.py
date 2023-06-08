# 내 풀이
def solution(a, b, c):
    x = [a, b, c]
    if len(x) == len(set(x)):
        return a + b + c
    elif len(x) == len(set(x)) + 1:
        return (a + b + c) * (a ** 2 + b ** 2 + c ** 2)

    else:
        return (a + b + c) * (a ** 2 + b ** 2 + c ** 2) * (a ** 3 + b ** 3 + c ** 3)



# 다른 사람 풀이

def solution(a, b, c):
    check=len(set([a,b,c]))
    if check==1:
        return 3*a*3*(a**2)*3*(a**3)
    elif check==2:
        return (a+b+c)*(a**2+b**2+c**2)
    else:
        return (a+b+c)