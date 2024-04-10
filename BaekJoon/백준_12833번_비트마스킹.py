# 중간에 시간 초과 난 부분(메모리 수 1억)
# xor 비트마스킹 특징상 같은 숫자를 xor 할 시 반복된다는 것을 확인!

a,b,c=list(map(int,input().split()))

if c%2==1:
    print(a^b)
else:
    print(a)