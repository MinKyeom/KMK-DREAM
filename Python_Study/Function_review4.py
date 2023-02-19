tuple_test=(10,20,30)

print(tuple_test[0])

#리스트와 튜플의 특이한 사용
[a,b]=[10,20]
(c,d)=(10,20)
print()
print()
print(a)
print(b)
print(c)
print(d)

#괄호가 없는 튜플

tuple_test2=10,20,30,40
print(tuple_test2)
print(type(tuple_test2))
print()
print()
#변수의 값을 교환하는 튜플

e,f=10,20

print("e:",e)
print("f:",f)

print("교환 후")

e,f=f,e

print("e:",e)
print("f:",f)



