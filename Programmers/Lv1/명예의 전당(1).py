# 내 풀이
def solution(k, score):
    winner=[]
    result=[]
    for x in score:
        if len(result)<k:
            winner.append(x)
            result.append(min(winner))
            continue
        elif x>min(winner):
            winner.remove(min(winner))
            winner.append(x)
            result.append(min(winner))
            continue
        else:
            result.append(min(winner))
    return result

# 다른 사람 풀이
def solution(k, score):

    q = []

    answer = []
    for s in score:

        q.append(s)
        if (len(q) > k):
            q.remove(min(q))
        answer.append(min(q))

    return answer