# 내 풀이
def solution(arr):
    i = 0
    stk = []
    while i < len(arr):
        for x in arr:
            if len(stk) == 0:
                stk.append(x)
                i += 1
            elif len(stk) > 0 and stk[-1] == x:
                stk.pop()
                i += 1
            else:
                stk.append(x)
                i += 1

    answer = stk
    return answer if len(stk) > 0 else [-1]
# 다른 사람 풀이
def solution(arr):
    stk = []
    for i in range(len(arr)):
        if stk and stk[-1] == arr[i]:
            stk.pop()
        else:
            stk.append(arr[i])

    return stk or [-1]
