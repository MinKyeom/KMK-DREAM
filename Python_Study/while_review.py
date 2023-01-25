a=range(10)
print(a)
print(list(a))
print(list(range(0,5)))

print(list(range(0,10,2)))
print(list(range(0,10,3)))

b=range(0,10+1)
print(list(b))

n=10

c=range(0,int(n/2))

print(list(c))

#for 반복문과 함께

for i in range(5):
    print(str(i)+"= 반복 변수")
print()

for i in range(5,10):
    print(str(i)+"=반복 변수")