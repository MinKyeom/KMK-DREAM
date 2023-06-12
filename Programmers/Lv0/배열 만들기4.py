# 내 풀이
def solution(arr):
    stk = []
    i=0
    while i<len(arr):
        if len(stk)==0:
            stk.append(arr[i])
            i+=1
        else:
            if stk[-1]<arr[i]:
                stk.append(arr[i])
                i+=1
            else:
                stk.pop()
    return stk

# 다른 사람 풀이
    def solution(arr):
        stk = []
        for i in range(len(arr)):
            while stk and stk[-1] >= arr[i]:
                stk.pop()
            stk.append(arr[i])
        return stk