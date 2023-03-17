#정상적인 출력예
# A,B=map(int,input().split())
# print(A*B)


#error 발생예
# A,B=int(input().split())
# print(A*B)
#→error 발생:
# int() argument must be a string, 
# a bytes-like object or a number, not 'list'

#error 발생예
# a,b=input().split()
# print(a*b)
#→TypeError: can't multiply sequence by non-int of type 'str'