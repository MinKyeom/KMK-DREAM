# 내 풀이
def solution(my_string):
    count = 0
    a = "abcdefghijklmnopqrstuvwxyz"
    b = a.upper()
    x = list(my_string)
    for c in range(len(x)):
        if x[c] in a or x[c] in b:
            continue
        else:
            count += int(x[c])

    return count


# 다른 사람 풀이

def solution(my_string):
    return sum(int(i) for i in my_string if i.isdigit())