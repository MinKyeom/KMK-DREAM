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

