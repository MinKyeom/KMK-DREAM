# 정수 실수 구분

print(type(27))

print(type(27.52))

# 간단한 연산 표현

print("1+2=",1+2)

# 나머지 연산자

print("5%2=",5%2)

#제곱연산자 2의 4제곱 2**4
print("2**4",2**4)

#사용자 입력

String1= input("이름을 입력하세요")

print(String1)

# format

string_a="{}".format(10)

print(string_a)
print(type(string_a))

#format 변환

format_a="{}만원".format(5000)
format_b="파이썬 열공하여 첫 연봉 {}만 원 만들기".format(5000)
format_c="{} {} {}".format(3000, 4000, 5000) #앞에 부분들을 띄워줘야 프린트 문에서도 결과값이 띄워짐

print(format_a)
print(format_b)
print(format_c)

#정수를 특정 칸에 출력하기

output_a= "{:d}".format(52)

#특정 칸에 출력하기

output_b="{:5d}".format(52) #5칸

#빈칸을 0으로 채우기

output_c="{:05d}".format(52)

print(output_a)
print(output_b)
print(output_c) #이해한 부분 괄호안의 숫자 포함 :d앞의 숫자 칸 0을 쓸 경우 빈칸을 0으로 채워 구분 편함!

#float 자료형 기본

float_output_a="{:f}".format(52.273)
float_output_b="{:15f}".format(52.273)

print(float_output_a)
print(float_output_b)

#대소문자 바꾸기

upper_a ="hello"
print(upper_a.upper()) #같은 방식으로 lower은 소문자!

#공백제거
strip_a="""
    안녕하세요
문자열의 함수를 알아봅시다
"""
print(strip_a)
print()
print(strip_a.strip()) # rstrip,lstrip도 존재한다

# 문자열 구성확인

print("TrainA10".isalnum())

