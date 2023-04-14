# a=[1,2,3,4,5]
# b=101
# a.append(b)
# print(a)
# print(a.index(max(a)))
# a=[1,2,3,4,5]
# b=[1,2,3]
# for x in a:
#     if x in b:
#         continue
#
#     print(1)
from itertools import permutations
a=["a","b","c"]
b=list(permutations(a,2))

print(b)