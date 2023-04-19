# # 풀이1
# def solution(my_str, n):
#     x=int(len(my_str)/n)
#     c=[]
#     for a in range(x+1):
#         # if a+(a+1)*n<len(my_str):
#         b=my_str[a*n:(a+1)*n]
#         c.append(b)
#         # elif a+(a+1)*n>=len(my_str):
#         #     b= my_str[a*n:len(list(my_str))]
#         #     c.append(b)
#         if c[-1]=="":
#             c.pop()
#         print(c)
#     answer = c
#     print(c)
#     return answer
#
# # 풀이2(team)
# import math
# def solution(my_str, n):
#     return [my_str[in:(i+1)n] for i in range(math.ceil(len(my_str)/n))]

# a= "abc"
# a[5:] -> ""
# a[:100000] -> "abc"