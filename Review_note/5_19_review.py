"""
# 부분 집합 개념
"""

s="banana"
k=[]

for i in range(len(s)):
    for j in range(i+1,len(s)+1):
        k.append(s[i:j])

print(k)
print(len(k))