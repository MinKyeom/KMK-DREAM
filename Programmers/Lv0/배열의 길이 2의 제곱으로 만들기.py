# 내 풀이
def solution(arr):
    x=len(arr)
    count=0
    while True:
        if x>=2**count and x<2**(count+1):
            if x==2**count:
                return arr
            count+=1
            break
        else:count+=1
    k=2**(count)-x
    for l in range(k):
        arr.append(0)
    return arr

# 다른 사람 풀이
def solution(arr):
    a = 1
    b = len(arr)
    while a < b :
        a *= 2
    return arr + [0] * (a-b)


"""
2의 거듭제곱 확인 방법 O(1)로 해야 겨우 O(n)
logn으로 확인하면 그걸 n번 반복 -> o(nlogn)
길이 1000개 -> 가장 빠른방법은 각각 하드코딩하기 겨우 10개

"""
