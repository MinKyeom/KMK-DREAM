# 내 풀이
def solution(arr):
    for x in range(len(arr)):
        if arr[x] >= 50 and arr[x] % 2 == 0:
            arr[x] = arr[x] / 2

        elif arr[x] < 50 and arr[x] % 2 == 1:
            arr[x] = arr[x] * 2

    answer = arr
    return answer
# 다른 사람 풀이
def solution(arr):
    return [num/2 if num>=50 and num%2==0 else (num*2 if num<50 and num%2==1 else num) for num in arr]