# 내 풀이
def solution(n):
    a=1
    b=1
    result=0
    count=0
    while True:
        if a==b and a==n:
            count+=1
            return count
        elif a==b and a!=n:
            b+=1
        elif a!=b and (a+b)*(b-a+1)/2==n:
            count+=1
            a+=1
            b=a
        elif a!=b and (a+b)*(b-a+1)/2<n:
            b+=1
        elif a!=b and (a+b)*(b-a+1)/2>n:
            a+=1
            b=a



# 다른 사람 풀이
def expressions(num):
    return len([i  for i in range(1,num+1,2) if num % i is 0])