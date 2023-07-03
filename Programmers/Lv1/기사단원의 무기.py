# 내 풀이
def solution(number, limit, power):
    count = 0
    for x in range(1, number + 1):
        num = []
        for y in range(1, int(x ** (1 / 2)) + 1):
            if x % y == 0:
                num.append(y)
                k = x / y
                num.append(int(k))
            else:
                continue
        if len(set(num)) > limit:
            count += power
        else:
            count += len(set(num))

    return count

# 다른 사람의 풀이
def cf(n): # 공약수 출력
    a = []
    for i in range(1,int(n**0.5)+1):
        if n%i == 0:
            a.append(n//i)
            a.append(i)
    return len(set(a))
def solution(number, limit, power):
    return sum([cf(i) if cf(i)<=limit else power for i in range(1,number+1)])