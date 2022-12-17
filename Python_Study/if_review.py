#간단한 boolean 만들기:비교 연산자

print(10==100)

# not 연산자 조합하기
x=10
under_20= x<20
print("under_20:",under_20)
print("not under_20:",not under_20)

#if 조건문 기본 사용
# number =input("정수 입력:")
#number=int(number)

# if number>0:
    # print("양수 입니다.")

# if number<0:
    # print("음수 입니다.")

# if number==0:
    # print("0")

#날짜/시간 출력

import datetime #import의경우 쓰이면 글자 색이 다르지만 안쓰이면 주석으로 쓰이는 글자색이랑 동일! pycharm에서!

now=datetime.datetime.now()

print(now.year,"년")

print("{}년 {}월 {}일 {}시 {}분 {}초".format(now.year, now.month,now.day,now.hour,now.minute,now.second))

# 끝자리로 짝수 홀수 구분
# number =input("정수 입력>")

# 마지막 자리 숫자를 추출

# last_character =number[-1]

# 숫자로 변환하기

# last_number=int(last_character)

# 짝수 확인

# if last_number ==0 \
#    or last_number==2\
#    or last_number==4\
#    or last_number==6\
#    or last_number==8:
#    print("짝수 입니다.")

# 홀수 확인
# 파이썬에서 줄이 너무 길어질 때는 \기호를 입력하고 줄바꿈해서 코드를 입력한다!
#else:
#    print("홀수 입니다.") # 원래는 or로 마지막 자리 숫자를 1 3 5 7 9로 써야한다!

# if만 써서 하는 경우는 비효율적이라 만약 흑백처럼 두 가지로 구분되면 if or else
# 조건이 다양하면 elif를 쓴다

#계절 구하기

import datetime

now=datetime.datetime.now()
month=now.month

if 3<=month<=5:
    print("현재는 봄 입니다.")

elif 6<=month<=8:
    print("현재는 여름 입니다.")

elif 9<=month<=11:
    print("현재는 가을 입니다.")

else:
    print("겨울 입니다.") #해당 조건이 없다면 그냥 코드는 진행된다 오류는 안나온다 참고!


# False로 변환되는 값

print("# if 조건문에 0 넣기")

if 0:
    print("0은 True로 변환됩니다")

else:
    print("0은 False로 변환됩니다.")

print()

print("#if 조건문에 빈 문자열 넣기")
if"":
    print("빈 문자열은 True로 변환됩니다.")
else:
    print("빈 문자열은 False로 변환됩니다.")

# pass 키워드를 사용한 미구현 부분 입력

# number = input("정수 입력>")
# number =int(number)

# if number> 0:
#    pass # 아직 미구현 상태의미!
# else:
#    pass

 # raise NotlmplementError
    #number2 = input("정수 입력>")
    #number2 = int(number2)

    #if number2> 0:
        #raise NotImplementedError # 미구현 상태이나 입력시 오류 출력
    #else:
        #raise NotImplementedError
 
 



