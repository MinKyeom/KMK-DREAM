# 내 풀이
def solution(arr):
    count = 0
    while True:
        before_arr = arr.copy()
        for x in range(len(arr)):
            if arr[x] >= 50 and arr[x] % 2 == 0:
                arr[x] = arr[x] / 2

            elif arr[x] < 50 and arr[x] % 2 == 1:
                arr[x] = arr[x] * 2 + 1
        after_arr = arr.copy()
        before_arr.sort()
        after_arr.sort()
        if after_arr == before_arr:
            return count
        count += 1

# 다른 사람 풀이
def solution(arr):
    answer = 0
    old = arr
    while(True):
        new = []
        for i in old:
            if i>=50 and i%2 == 0:
                i = i/2
            elif i<50 and i%2 == 1:
                i = i*2 + 1
            new.append(int(i))
        if old == new:
            break
        else:
            old = new
            answer += 1
    return answer


