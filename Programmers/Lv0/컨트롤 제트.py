# 내 풀이
def solution(s):
    x = s.split()
    count = []

    for a in x:
        if not a == "Z":
            count.append(int(a))
        elif a == "Z":
            count.pop()

    answer = sum(count)
    return answer


# 다른 사람 풀이

def solution(s):
    answer = 0
    for i in range(len(s := s.split(" "))):
        answer += int(s[i]) if s[i] != "Z" else -int(s[i-1])
    return answer