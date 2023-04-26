# 풀이
def solution(s1, s2):
    answer = 0

    for x in s2:
        if x in s1:
            answer += 1

    return answer


# 내 풀이2
def solution(s1, s2):
    x=set(s1)&set(s2)
    z=len(x)
    answer = z
    return answer

# 팀원 풀이
def solution(s1, s2):
    return len(set(s1).intersection(s2))
# 다른 사람 풀이
def solution(s1, s2):
    return len(set(s1)&set(s2));