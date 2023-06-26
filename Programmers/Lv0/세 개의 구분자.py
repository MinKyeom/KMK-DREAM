# 내 풀이
def solution(myStr):
    x = myStr.replace("a", " ")
    y = x.replace("b", " ")
    z = y.replace("c", " ")
    sub = z.split(" ")
    result = []
    for x in range(len(sub)):
        if sub[x] == "":
            continue
        else:
            result.append(sub[x])

    return result if len(result) >= 1 else ["EMPTY"]
# 다른 사람 풀이

def solution(myStr):
    answer = [x for x in myStr.replace('a', ' ').replace('b', ' ').replace('c', ' ').split() if x]
    return answer if answer else ['EMPTY']