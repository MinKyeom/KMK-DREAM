# 내 풀이
def solution(s):
    num = "1234567890"
    eng = "abcdefghijklmnopqrstuvwxyz"
    eng_L = eng.upper()
    a = list(s)
    for x in a:
        if x in num:
            continue
        else:
            return False

    return True if len(s) == 4 or len(s) == 6 else False


# 다른 사람 풀이
def alpha_string46(s):
    #함수를 완성하세요

    return s.isdigit() and len(s) in [4,6]
