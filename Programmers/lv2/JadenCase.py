# 내 풀이
def solution(s):
    k = list(s)
    for a in range(len(k)):
        if a > 0 and k[a - 1] == " ":
            if k[a] == " ":
                continue
            elif k[a].isdigit == True:
                l = 1
            else:
                k[a] = k[a].upper()
        elif a == 0 and k[a].isdigit() != True:
            k[a] = k[a].upper()
        else:
            k[a] = k[a].lower()

    return "".join(k)

# 다른 사람 풀이
def Jaden_Case(s):
    # 함수를 완성하세요
    return s.title()

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(Jaden_Case("3people unFollowed me for the last week"))
