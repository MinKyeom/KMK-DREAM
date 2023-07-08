# 내 풀이
def solution(X, Y):
    # x=list(X)
    # y=list(Y)
    # z=set(x)&set(y)
    # z=list(z)
    # z.sort(reverse=True)
    a = ""

    for w in range(9, -1, -1):
        a = a + str(w) * min(list(X).count(str(w)), list(Y).count(str(w)))

    if a == '':
        return '-1'
    elif len(a) == a.count('0'):
        return '0'
    else:
        return a

# 다른 사람 풀이
def solution(X, Y):
    answer = ''

    for i in range(9,-1,-1) :
        answer += (str(i) * min(X.count(str(i)), Y.count(str(i))))

    if answer == '' :
        return '-1'
    elif len(answer) == answer.count('0'):
        return '0'
    else :
        return answer
