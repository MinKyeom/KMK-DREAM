#풀이 1
def solution(my_string):
    answer = ''
    a = list(my_string)

    for x in range(len(a)):
        if a[x] == my_string.lower()[x]:
            a[x] = my_string.upper()[x]

        else:
            a[x] = my_string.lower()[x]
    answer = "".join(a)
    return answer

#다른 사람 풀이

def solution(my_string):
    return my_string.swapcase()