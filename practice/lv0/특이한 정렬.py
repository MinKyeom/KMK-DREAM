# 풀이1
# 이차원 정렬에서 첫 번째 정렬 두번째 값 정렬 방법 구분!
def solution(numlist, n):
    abslist = []
    answer = []
    for a in numlist:
        x = abs(n - a)
        abslist.append([x, a])
    abslist.sort(key=lambda x: (x[0], -x[1]))

    for y, z in abslist:
        answer.append(z)
    return answer
#풀이2

def solution(numlist, n):
    answer = sorted(numlist,key = lambda x : (abs(x-n), n-x))
    return answer
