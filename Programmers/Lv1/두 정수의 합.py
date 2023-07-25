# 내 풀이
def solution(a, b):
    if a>b:
        k=[x for x in range(b,a+1)]
    elif a<b:
        k=[x for x in range(a,b+1)]
    elif a==b:
        return a
    return sum(k)

# 다른 사람 풀이
def adder(a, b):
    if a > b:
        a, b = b, a
    return sum(range(a, b + 1))

print( adder(3, 5))