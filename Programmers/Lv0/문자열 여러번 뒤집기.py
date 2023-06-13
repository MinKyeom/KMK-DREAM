# 내 풀이
def solution(my_string, queries):
    for x, y in queries:
        count = 0
        sub_string = list(my_string[x:y + 1])
        sub_string.reverse()
        for z in range(x, y + 1):
            my_string = list(my_string)
            my_string[z] = sub_string[count]
            count += 1
            my_string = "".join(my_string)

    return my_string

# 다른 사람 풀이
def solution(my_string, queries):
    answer=list(my_string)
    for s,e in queries:
        answer[s:e+1]=answer[s:e+1][::-1]
    return ''.join(answer)