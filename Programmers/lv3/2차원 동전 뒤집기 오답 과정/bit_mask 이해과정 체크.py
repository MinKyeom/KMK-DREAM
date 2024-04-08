a=7

for i in range(a):
    if a & (1<<i):
        print(1<<i, "1<<i" ,a & (1<<i),"a & (1<<i)",i,"i")
        print(i)

print("break")

# and 와 & 의미파악 비교
for j in range(5):
    if j and 1:
        print("확인",j)

# 연산 과정의 이해

# if

a = 10

if a > 0 and (a % 2) == 1:
    print("a is odd")
else:
    print("a is even")

# &

result = 7 & 2

print(result)

#         7 = 0000 0111
#      &  2 = 0000 0010
#-----------------------
# result, 2 = 0000 0010

# if 문의 이해

b=5

for k in range(5):
    if 2 & (1<<k):
        print(k,"k")