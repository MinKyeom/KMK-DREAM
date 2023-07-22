# 내 풀이
def solution(n):
    if n%2==0:
        k=int(n/2)
        return "수박"*k
    else:
        k=int(n/2)
        return "수박"*k+"수"


# 다른 사람 풀이
def water_melon(n):
    # 함수를 완성하세요.
    str = "수박"*n
    return str[:n]