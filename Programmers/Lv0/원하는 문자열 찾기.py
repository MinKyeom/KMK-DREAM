# 내 풀이
def solution(myString, pat):
    myString = myString.lower()
    pat = pat.lower()

    if pat in myString:
        return 1
    else:
        return 0
# 다른 사람 풀이

def solution(myString, pat):
    return int(pat.lower() in myString.lower())

