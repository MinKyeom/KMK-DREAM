# 풀이1
# def solution(num, total):
#     c = 0
#     sol = []
#     for x in range(num):
#         c += x
#     a = (total - c) / num
#     for y in range(num):
#         z = a + y
#         sol.append(z)
#
#     return sol



# team sol
# def solution(num, total):
#     answer = []
#     default_s = num*(num+1)//2
#
#     p1 = 1
#     p2 = num
#     while default_s != total:
#         if total > default_s:
#             default_s -= p1
#             p1 +=1
#             p2 +=1
#             default_s += p2
#         else:
#             default_s -= p2
#             p1 -=1
#             p2 -=1
#             default_s += p1
#
#     else:
#         answer.extend(range(p1, p2+1))
#
#     return answer



# return [(total - (num * (num - 1) // 2)) // num + i for i in range(num)]