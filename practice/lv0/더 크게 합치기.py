# 내 풀이

def solution(a, b):
    x=str(a)+str(b)
    y=str(b)+str(a)
    if int(x)>=int(y):
        return int(x)
    else:return int(y)

# 다른 사람 풀이
def solution(a, b):
    return int(max(f"{a}{b}", f"{b}{a}"))