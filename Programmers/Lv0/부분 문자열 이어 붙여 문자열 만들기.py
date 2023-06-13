# 내 풀이
def solution(my_strings, parts):
    result = []
    count = 0
    while True:
        result.append(my_strings[count][parts[count][0]:parts[count][1] + 1])
        if count == len(parts) - 1:
            break
        count += 1

    return "".join(result)

# 다른 사람 풀이
def solution(my_strings, parts):
    answer = ""
    for i, (s, e) in enumerate(parts):
        answer += my_strings[i][s:e+1]
    return answer
