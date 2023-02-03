a=[10,15,20]
print(min(a))
print(max(a))
print(sum(a))

#reversed

a_reversed =reversed(a)
print("reversed:",a_reversed)
print("list(reversed([10,15,20]:",list(a_reversed))

#[::-1]

print("[::-1]:",a[::-1])
print()
print()

#enumerate

b=["요소1","요소2","요소3"]
print("기본 출력")
print(b)
print()

print(" enumerate 적용")
print(enumerate(b))
print()

print("list로 다시 강제 변환")
print(list(enumerate(b)))
print()

print("반복문 추가")
for i,value in enumerate(a):
    print("{}번째 요소는 {} 입니다".format(i,value))

#dictionary items() 반복문 조합

dictionary={
    "key1":"a",
    "key2":"b",
    "key3":"c"
}

print(dictionary.items())

for key,element in dictionary.items():
    print("dictionary[{}]={}".format(key,element))

#list 내포
array=[]
for e in range(0,20,2):
    array.append(e*e)
print(array)#for문에 안걸리게 하는거 주의하기!

array_2=[f*f for f in range(0,20,2)]

print(array_2)

array_3=["사과","자두","초콜릿","바나나","체리"]
output=[fruit for fruit in array_3 if fruit !="초콜릿"]
print(output)

