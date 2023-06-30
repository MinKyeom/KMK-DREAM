# 내 풀이
def solution(arr1, arr2):
    if len(arr1) == len(arr2):
        if sum(arr1) == sum(arr2):
            return 0
        elif sum(arr1) > sum(arr2):
            return 1
        else:
            return -1
    else:
        if len(arr1) > len(arr2):
            return 1
        else:
            return -1

    return answer

# 다른 사람 풀이
def solution(arr1, arr2):
    x, y = len(arr1), len(arr2)
    if x != y:
        return 1 if x > y else -1
    elif x == y:
        sum_x, sum_y = sum(arr1), sum(arr2)
        if sum_x > sum_y:
            return 1
        elif sum_x < sum_y:
            return -1
        else:
            return 0
