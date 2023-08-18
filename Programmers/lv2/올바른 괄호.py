# 내 풀이
def solution(s):
    count_1 = 0
    count_2 = 0
    s = list(s)

    if s[0] == "(" and s[len(s) - 1] == ")":
        while s:
            k = s.pop()
            print(k)
            if k == ")":
                count_1 += 1
            else:
                count_2 += 1

            if count_2 > count_1:
                return False

        return True


    else:
        return False

# 다른 사람 풀이
def is_pair(s):
    pair = 0
    for x in s:
        if pair < 0: break
        pair = pair + 1 if x == "(" else pair - 1 if x == ")" else pair
    return pair == 0