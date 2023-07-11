# 내 풀이
def solution(absolutes, signs):
    count=0
    for x in range(len(signs)):
        if signs[x]==True:
            count+=absolutes[x]
        else:
            count-=absolutes[x]
    return count

# 다른 사람 풀이
def solution(absolutes, signs):
    return sum(absolutes if sign else -absolutes for absolutes, sign in zip(absolutes, signs))
