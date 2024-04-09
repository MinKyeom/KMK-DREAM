# a=7
#
# # 1이 있을 경우 겹치는 경우 if문에 해당되여 넘어간다!
# for i in range(a):
#     if a & (1<<i):
#         print("겹침")
#         print(1<<i, "1<<i" ,a & (1<<i),"a & (1<<i)",i,"i")
#         print(bin(a))
#         print(bin(1<<i))
#
#     else:
#         print("안겹침")
#         print(bin(i))
#         print(bin(1<<i))
# print("break")
#
# # and 와 & 의미파악 비교
# for j in range(5):
#     if j and 1:
#         print("확인",j)
#
# # 연산 과정의 이해
#
# # if
#
# a = 10
#
# if a > 0 and (a % 2) == 1:
#     print("a is odd")
# else:
#     print("a is even")
#
# # &
#
# result = 7 & 2
#
# print(result,"result")
#
# #         7 = 0000 0111
# #      &  2 = 0000 0010
# #-----------------------
# # result, 2 = 0000 0010
#
# # if 문의 이해
#
# b=5
#
# for k in range(5):
#     if 2 & (1<<k):
#         print(k,"k")
#
#
# if 2&4:
#     print("Zzz")
# print(bin(2))
# print(bin(4))

# 비트 연산자를 활용한 체크

a=2

# &
if 9&3: #5:101  3:11 겹치는게 하나라도 있다면 참
    print("Ture1")
else:
    print("False1")

if a&8: #a:10 8:100
    print("True2")
else:
    print("False2")
# |
if 5|0: #어느 하나라도 1이 있다면 참
    print("True3")
else:
    print("False3")
if a|1:
    print("Ture4")
else:
    print("False4")
#^
if 3^2: #하나라도 다르면 참
    print("True5")
else:
    print("False5")
