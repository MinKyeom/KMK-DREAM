#zip
a=[1,2,3,4,5]
b=["사과","딸기","메론"]

for x in zip(a,b):
    print(x)

print()

# 비슷한 표현

for y in range(3):
    new=(a[y],b[y])
    print(new) #양측의 데이터를 하나씩 짝지어준다
