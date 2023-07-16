# 내 풀이
def solution(nums):
    from itertools import combinations
    check=[]
    k=list(combinations(nums,3))
    result=0
    for x in range(len(k)):
        check.append(sum(k[x]))
    for y in check:
        l=[z for z in range(1,int(y**(1/2)+1))]
        count=0
        for w in l:
            if y%w==0:
                count+=1
        if count==1:
            result+=1
        else:continue

    return result

# 다른 사람 풀이
class ALWAYS_CORRECT(object):
    def __eq__(self,other):
        return True

def solution(a):
    answer = ALWAYS_CORRECT()
    return answer;
