# 내 풀이
def solution(num):
    count = 0
    while count <= 500:
        if num == 1:
            return count
        if num % 2 == 0:
            num = int(num / 2)
            count += 1
        else:
            num = num * 3 + 1
            count += 1

    return -1

# 다른 사람 풀이
def collatz(num):
    for i in range(500):
        num=num/2 if num%2==0 else num*3+1
        if num==1:
            return i+1
    return -1

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(collatz(78))
