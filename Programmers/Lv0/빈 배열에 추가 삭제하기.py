# 내 풀이
def solution(arr, flag):
    result=[]
    for x in range(len(arr)):
        if flag[x]==True:
            for k in range(arr[x]*2):
                result.append(arr[x])
        else:
            result=result[:len(result)-arr[x]]
    answer = result
    return answer
# 다른 사람 풀이
    def solution(arr, flag):
        X = []
        for i, f in enumerate(flag):
            if f:
                X += [arr[i]] * (arr[i] * 2)
            else:
                for _ in range(arr[i]):
                    X.pop()
        return X

