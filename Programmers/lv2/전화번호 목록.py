# 내 풀이
def solution(phone_book):
    p = phone_book

    p.sort()

    for a in range(len(p) - 1):
        if p[a] in p[a + 1][0:len(p[a])]:
            return False

        else:
            continue

    return True

# 다른 사람 풀이
def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True
