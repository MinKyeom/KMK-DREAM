# 내 풀이
def solution(arr, query):
    result = []
    for x in range(len(query)):
        if x % 2 == 0:
            arr = arr[:query[x] + 1]
        else:
            arr = arr[query[x]:]

    answer = arr
    return answer
# 다른 사람 풀이

def solution(arr, query):
    for k, q in enumerate(query):
        if k % 2 == 0:
            arr = arr[:q + 1]
        else:
            arr = arr[q:]
    return arr