# 내 풀이
def solution(todo_list, finished):
    result = []
    for x in range(len(finished)):
        if finished[x] == False:
            result.append(todo_list[x])

    return result
# 다른 사람 풀이
def solution(todo_list, finished):
    return [work for idx, work in enumerate(todo_list) if not finished[idx]]