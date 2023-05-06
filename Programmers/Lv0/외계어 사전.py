# 내 풀이
def solution(spell, dic):
    num=[]
    for x in dic:
        for y in spell:
            if y in list(x):
                num.append(y)
        if len(num)==len(spell):
            return  1
        else:num.clear()
    return 2

# 다른 사람 풀이

def solution(spell, dic):
    spell = set(spell)
    for s in dic:
        if not spell-set(s):
            return 1
    return 2