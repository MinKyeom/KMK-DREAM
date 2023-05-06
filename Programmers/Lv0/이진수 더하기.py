# 풀이1
#여러가지 이진법 확인 한 후 풀이 가능했었음!
def solution(bin1, bin2):
    answer=0
    x="0b"+bin1
    y="0b"+bin2
    z=x+"+"+y
    a=bin(eval(z))
    b=str(a).split("0b")
    print(b[1])
    return b[1]


# 이진수 기본 상식 공부


# 풀이 2
def solution(bin1, bin2):
    answer = bin(int(bin1,2) + int(bin2,2))[2:]
    return answer
# a=0b10+0b11
# a="0b"+"101"
# b
# print(b)

