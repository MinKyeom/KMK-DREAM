"""
출처: 프로그래머스,
https://school.programmers.co.kr/learn/courses/30/lessons/120908
"""
# 풀이 과정
def solution(str1, str2):
    if str2 in str1:
        return 1
    else:return 2


# 풀이 1

# () 아예 못품

# def solution(str1, str2):
#     if not str1.find(str2)==-1:
#         return 1
#     else:
#         return 2

#풀이 2 (team)

# def solution(str1, str2):
#     return 1 if str1.find(str2) >= 0 else 2


"""
짧막한 오답

output="abcdef"
s="cde"
g="zzz"

x=output.find(g)
# y=output.index(g)
print(x)

print()

# print(y)

# find : 못찾으면 :-1 반환 , index:는 오류가 나오면 not found가 나온다
"""
