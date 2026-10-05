# 함수 정의
def number_input():
    output=input("반지름 길이는?")
    return float(output)

def get_circumference(radius):
    return 2*3.14*radius

def get_circle_area(radius):
    return 3.14*radius*radius

#코드 본문
radius=number_input()
print(get_circumference(radius))
print(get_circle_area(radius))