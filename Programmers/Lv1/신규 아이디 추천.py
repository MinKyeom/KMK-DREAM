# 내 풀이
def solution(new_id):
    check = "0123456789abcdefghijklmnopqrstuvwxyz-_."
    check_eng = "abcdefghijklmnopqrstuvwxyz"
    check_eng_big = check_eng.upper()
    check_eng = check_eng + check_eng_big
    result = []
    k = list(new_id)

    for x in range(len(k)):
        if k[x] in check_eng:
            k[x] = k[x].lower()

        if not k[x] in check:
            continue
        else:
            result.append(k[x])

    r_2 = "".join(result)

    while True:
        if ".." in r_2:
            r_2 = r_2.replace("..", ".")
        else:
            break

    r_2 = list(r_2)
    r_3 = []

    for g in range(len(r_2)):
        if g == 0 or g == len(r_2) - 1:
            if r_2[g] == ".":
                continue
            else:
                r_3.append(r_2[g])
        else:
            r_3.append(r_2[g])

    final = "".join(r_3)

    if len(final) <= 2:
        l = 3 - len(final)
        c = final[len(final) - 1:]
        for y in range(l):
            final = final + c
        return final if len(final) != 0 else "aaa"

    elif len(final) >= 16:
        return final[0:15] if final[14:15] != "." else final[0:14]

    else:
        return final

# 다른 사람 풀이
import re

def solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st
