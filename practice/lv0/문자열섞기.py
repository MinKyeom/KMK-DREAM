# 내 풀이
def solution(str1, str2):
    x = list(str1)
    y = list(str2)
    z = []
    for a in range(len(str1)):
        z.append(x[a])
        z.append(y[a])

    answer = "".join(z)

    return answer

# 다른 사람 풀이

def solution(str1, str2):
    answer = ''
    for i in range(0,len(str1)):
        answer = answer + str1[i] + str2[i]
    return answer