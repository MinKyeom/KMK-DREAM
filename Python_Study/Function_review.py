#기본적인 함수

def print_2_times():
    print("안녕하세요")
    print("안녕하세요")

print_2_times() #들여쓰기 위치 확인!!

# 매개변수의 기본

def print_n_times(value,n):
    for i in range(n):
        print(value)

print_n_times("안녕하세요",6)


