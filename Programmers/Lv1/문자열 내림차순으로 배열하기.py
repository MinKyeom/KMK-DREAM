# 내 풀이
def solution(s):
    eng = "abcdefghijklmnopqrstuvwxyz"
    k = list(s)
    eng_s = []
    eng_b = []
    for x in range(len(k)):
        if k[x] in eng:
            eng_s.append(k[x])
        else:
            eng_b.append(k[x])
    eng_s.sort(reverse=True)
    eng_b.sort(reverse=True)

    return "".join(eng_s) + "".join(eng_b)
# 다른 사람 풀이
def solution(s):
    return ''.join(sorted(s, reverse=True))
