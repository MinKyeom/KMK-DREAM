# 내 풀이
def solution(intStrs, k, s, l):
    num=[]
    for x in intStrs:
        if int(x[s:s+l])>k:
            num.append(int(x[s:s+l]))
        else:continue
    return num
# 다른 사람 풀이
def solution(intStrs, k, s, l):
    return [int(intstr[s:s+l]) for intstr in intStrs if int(intstr[s:s+l]) > k]
