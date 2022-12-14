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
number =input("정수 입력>")

# 마지막 자리 숫자를 추출

last_character =number[-1]

# 숫자로 변환하기

last_number=int(last_character)

# 짝수 확인

if last_number ==0 \
    or last_number==2\
    or last_number==4\
    or last_number==6\
    or last_number==8:
    print("짝수 입니다.")

# 홀수 확인
# 파이썬에서 줄이 너무 길어질 때는 \기호를 입력하고 줄바꿈해서 코드를 입력한다!
else:
    print("홀수 입니다.") # 원래는 or로 마지막 자리 숫자를 1 3 5 7 9로 써야한다!








