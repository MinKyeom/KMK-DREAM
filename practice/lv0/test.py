# def solution(num_list, n):
#     num=[]
#     num_new=[]
#     count=0
#     while True:
#         for a in range(n):
#             if len(num_list)==0:
#                 break
#             x=num_list.pop(0)
#             num.append(x)
#         print(num)
#         num_new.append(num)
#         print(num_new)
#         num.clear()
#         if len(num_list)==0:
#             return num_new
#

# a=[[1,2],[5,6],[7,9]]
# print(a[0:2])


# a=[[1,2]]
# b=[]
# b.append(a)
#
# print(b,"시작")
#
# a.clear()
# a=[[1,2]]
#
# b.append(a)
#
# print(b)
#
# a=[]
# b.append(a)
#
# print(b)

# a=[1,2,3,4,5]
# a=[]
# print(a)


a=4567899
print(set(list(str(a))))
b=set(list(str(a)))
c={"이"}
print(len(b|c))



