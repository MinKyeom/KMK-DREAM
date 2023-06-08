# 내 풀이
def solution(arr, queries):
    for x,y in queries:
        arr[x],arr[y]=arr[y],arr[x]
    return arr
# 다른 사람 풀이
def solution(arr, queries):
    for a,b in queries:
        arr[a],arr[b]=arr[b],arr[a]
    return arr
