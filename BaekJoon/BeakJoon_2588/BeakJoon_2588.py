# 내 풀이
a=int(input())
b=list((input()))
c="".join(b)
d=int(c)
map(int,b)
print(a*int(b[2]))
print(a*int(b[1]))
print(a*int(b[0]))
print(a*d)

# 다른 사람들의 풀이
A = int(input())  # 첫번째 입력받은 문자 : 숫자로 변환
B = input()       # 두번째 입력받은 문자 : 문자열 그대로 둠

# 문자열의 인덱스를 이용해서 두번째 입력 받은 문자를 하나씩 숫자로 반환하고 A와 곱한다.
AxB2 = A * int(B[2])
AxB1 = A * int(B[1])
AxB0 = A * int(B[0])
AxB = A * int(B)

print(AxB2, AxB1, AxB0, AxB, sep='\n')