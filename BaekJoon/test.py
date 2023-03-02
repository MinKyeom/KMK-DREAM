# a=[(1,2),(2,3)]
#
# for x,y in a:
#     print(x)
#     print(y)
#     print()


# a=[(1,2)]
#
# print(len(a))
a=[]
for x in range(2):
    a.append(list(map(int,input().split())))


print(a)
print(sum(a))

