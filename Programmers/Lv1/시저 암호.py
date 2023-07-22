# 내 풀이
def solution(s, n):
    eng = "abcdefghijklmnopqrstuvwxyz"
    eng_L = eng.upper()

    k = list(s)
    print(k)
    for x in range(len(k)):
        if k[x] in eng:
            a = eng.find(k[x])
            print(a, "check2")
            if a + n > len(eng) - 1:
                b = (a + n) - (len(eng) - 1) - 1
                k[x] = eng[b:b + 1]
            else:
                k[x] = eng[a + n:a + n + 1]
        elif k[x] in eng_L:
            a = eng_L.find(k[x])
            print(a, "check")
            if a + n > len(eng) - 1:
                b = (a + n) - (len(eng) - 1) - 1
                k[x] = eng_L[b:b + 1]
            else:
                k[x] = eng_L[a + n:a + n + 1]

    return "".join(k)

# 다른 사람 풀이
def caesar(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
        elif s[i].islower():
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))

    return "".join(s)
    # 주어진 문장을 암호화하여 반환하세요.


