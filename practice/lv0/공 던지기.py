# 내 풀이
def solution(numbers, k):
    count=0
    x=0
    while True:
        if x>len(numbers)-1:
            x=(x)%len(numbers)
            x=x
            a=numbers[x]
            if count+1==k:
                    return a
            count+=1
            x+=2
        else:
            a=numbers[x]
            if count+1==k:
                return a
            count+=1
            x+=2
        print(a)
# 나머지와 수의 배치 개념 곰곰히 생각해보기!


# 다른 사람 풀이

def solution(numbers, k):
    return numbers[2 * (k - 1) % len(numbers)]

