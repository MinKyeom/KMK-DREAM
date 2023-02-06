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


#괄호로 문자열 연결하기

test=(
    "이렇게 입력해도 "
    "하나의 문자열로 연결되어"
    "생성 됩니다."
)

#출력합니다.
print("test: ",test)

# 쉼표로 연결하기

test_2=(
    "이렇게 입력하면",
    "하나의 문자열로 연결되지",
    "않습니다."
)
print("test_2:",test_2)

#여러 줄 문자열과 if 구문을 조합 했을 때의 문제해결

#n= int(input("정수 입력:"))

#if n%2 ==0:
#    print(("{}은(는) 짝수 입니다").format(n))

#else:
#    print(("{}은 짝수가 아닙니다.").format(n))


# 문자열의 join() 함수

print("::".join(["1","2","3","4","5","6"])) # 문자열이라는 사실!!

#여러 줄 문자열과 if 구문을 조합했을 떄의 문제 해결
#n_2=int(input("정수 입력:"))
#if n_2%2 ==0:
#    print("\n".join([
#        "입력한 문자열은 {} 입니다.",
#        "{}는(은) 짝수입니다."
#    ]).format(n_2,n_2))
#else:
#    print("\n".join([
#        "입력한 문자열은 {}입니다.",
#        "{}는(은) 홀수 입니다."
#    ]).format(n_2,n_2))

#reversed() 함수와 이터레이터

n_3=[1,2,3,4,5,6]
r_n=reversed(n_3)
print(r_n)
print(next(r_n))
print(next(r_n))
print(next(r_n))
print(next(r_n))
print(next(r_n))


