# 내 풀이

def solution(arr, queries):
    for s,e,k in queries:
        num=[x for x in range(s,e+1)]
        for z in num:
            if z%k==0 and z<len(arr):
                    arr[z]=arr[z]+1
    return arr

# 다른 사람 풀이

def solution(arr, queries):
    for s, e, k in queries:
        for i in range(s, e+1):
            if i%k == 0:
                arr[i] += 1
    return arr

