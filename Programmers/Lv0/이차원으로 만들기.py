# 내 풀이
def solution(num_list, n):
    count=0
    num_new=[]
    result=[]
    for a in range(len(num_list)):
        x=num_list[a]
        num_new.append(x)
        count+=1
        if not count==n and a==len(num_list)-1:
            result.append(num_new)
        if count==n:
            result.append(num_new)
            num_new=[]
            count=0
    return result

# .clear()로 했을 때 오류가 많이 나는 이유 생각해보기 clear의 기능 제대로 공부하기!