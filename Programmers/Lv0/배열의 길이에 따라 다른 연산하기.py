# 내 풀이
def solution(arr, n):
    if len(arr) % 2 == 1:
        for x in range(len(arr)):
            if x % 2 == 0:
                arr[x] = arr[x] + n
    else:
        for x in range(len(arr)):
            if x % 2 == 1:
                arr[x] = arr[x] + n

    answer = arr
    return answer

# 다른 사람 풀이
def solution(arr, n):
    N=len(arr)
    if N%2:
        for i in range(0,N,2): arr[i]+=n
    else:
        for i in range(1,N,2): arr[i]+=n
    return arr