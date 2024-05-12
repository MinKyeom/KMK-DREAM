"""
출처: 프로그래머스 코딩 테스트 연습,
https://school.programmers.co.kr/learn/courses/30/lessons/120863
"""
# 내 풀이

def solution(polynomial):
    x = polynomial.split()
    list_x = []
    count = 0

    for a in range(len(x)):
        if "x" in x[a]:
            list_x.append(x[a])
        elif "+" in x[a]:
            continue
        else:
            count += int(x[a])

    for b in range(len(list_x)):
        if list_x[b] == "x":
            list_x[b] = 1
        else:
            list_x[b] = int(list_x[b][0:len(list_x[b]) - 1])
    if count == 0 and not sum(list_x) == 0 and not sum(list_x) == 1:
        return str(sum(list_x)) + "x"
    elif count == 0 and sum(list_x) == 0:
        return 0
    elif not count == 0 and sum(list_x) == 0:
        return str(count)
    elif not count == 0 and sum(list_x) == 1:
        return "x " + "+ " + str(count)
    elif count == 0 and sum(list_x) == 1:
        return "x"
    else:
        return str(sum(list_x)) + "x " + "+ " + str(count)



# 다른 사람 풀이

def solution(polynomial):
    xnum = 0
    const = 0
    for c in polynomial.split(' + '):
        if c.isdigit():
            const+=int(c)
        else:
            xnum = xnum+1 if c=='x' else xnum+int(c[:-1])
    if xnum == 0:
        return str(const)
    elif xnum==1:
        return 'x + '+str(const) if const!=0 else 'x'
    else:
        return f'{xnum}x + {const}' if const!=0 else f'{xnum}x'
