# 내 풀이
def solution(n):
    ans = 0
    check = n
    while check >= 1:
        if check % 2 == 0:
            check = int(check / 2)
        else:
            check -= 1
            ans += 1

    return ans
# 다른 사람 풀이

def solution(n):
    return bin(n).count('1')