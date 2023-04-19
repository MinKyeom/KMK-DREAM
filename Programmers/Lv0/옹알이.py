# 풀이1
# from itertools import permutations
#
# babbling=["aya", "yee", "u", "maa", "wyeoo"]
#
# def solution(babbling):
#     word = []
#     result = 0
#     speak = ["aya", "ye", "woo", "ma"]
#     for x in range(1, len(speak) + 1):
#         for y in permutations(speak, x):
#             word.append("".join(y))
#     for z in babbling:
#         if z in babbling:
#             result += 1
#
#     return result
#
# a= solution(babbling)
#
# print(a)


# 풀이2
# def solution(babbling):
#     c = 0
#     for b in babbling:
#         for w in [ "aya", "ye", "woo", "ma" ]:
#             if w * 2 not in b: #연속된 문자열을 골라내기 위함
#                 b = b.replace(w, ' ')
#         if len(b.strip()) == 0:
#             c += 1
#     return c


# 풀이3
from itertools import permutations
def solution(babbling):
    #
    answer = 0
    speak = ["aya", "ye", "woo", "ma"]
    arr = []
    for i in range(1, len(speak)+1):
        for perm in permutations(speak, i):
            arr.append("".join(list(perm)))

    for b in babbling:
        if b in arr:
            answer+=1

    return answer