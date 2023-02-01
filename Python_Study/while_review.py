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

#array와 함께

array=[273,32,103,57,52]

for d in array:
    print(d)


#반대로 반복하기

for i in range(4,0 - 1,-1):
    print("현재 반복 변수: {}".format(i))

#반대로 반복하기2

for j in reversed(range(5)):
    print("현재 반복 변수2: {}".format(j))

#while 반복문
i=0
while i<10:
    print("{}번째 반복 입니다!.".format(i))
    i+=1

#while을 활용하여 해당하는 값 제거
list_test=[1,2,1,2]
print("지우기 전",list_test)
value=2
while value in list_test:
    list_test.remove(value)

print("지운 이후",list_test)

#while 시간

#import time
#print(time.time())

#while break/continue
#i=0
#True true 대소문자 구분잘해주기 소문자로 했을때 오류났음
#while True:
#    print("{}번째 반복문입니다.".format(i))
#    i=i+1
#    input_text= input(">종료하시겠습니까?(y):")
#    if input_text in ["y","Y"]:
#        print("종료")
#        break

#continue

d=[5,10,15,20,25]

for c in d:
    if c < 10:
     continue
    print(c) #어떤 문법에 해당되는지에 따라 줄 위치 잘확인하기


