# 내 풀이
def solution(s):
    a=s.count("p")
    b=s.count("P")
    c=s.count("y")
    d=s.count("Y")
    return True if (a+b)==(c+d) else False

# 다른 사람 풀이
def numPY(s):
    # 함수를 완성하세요
    return s.lower().count('p') == s.lower().count('y')
