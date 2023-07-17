# 내 풀이
def solution(arr1, arr2):
    result = []
    for x in range(len(arr1)):
        check = []
        for y in range(len(arr1[0])):
            a = arr1[x][y] + arr2[x][y]
            check.append(a)
        result.append(check)

    return result
# 다른 사람 풀이
def sumMatrix(A,B):
    answer = [[c + d for c, d in zip(a,b)] for a, b in zip(A,B)]
    return answer

print(sumMatrix([[1,2], [2,3]], [[3,4],[5,6]]))
