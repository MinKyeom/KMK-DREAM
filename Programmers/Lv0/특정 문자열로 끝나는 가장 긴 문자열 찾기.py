# 내 풀이
def solution(myString, pat):
    result = []
    for x in range(len(myString)):
        x = myString.find(pat, x)
        result.append(x)

    if len(result) == 0:
        return 0
    else:
        x = max(result)
        return myString[:x + len(pat)]
# 다른 사람 풀이
solution=lambda x,y:x[:x.rindex(y)+len(y)]