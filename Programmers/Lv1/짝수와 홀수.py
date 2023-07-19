# 내 풀이
def solution(num):
    if num%2==0:
        return "Even"
    else:
        return "Odd"

# 다른 사람 풀이
def evenOrOdd(num):
    #함수를 완성하세요
    if num%2:
        return "Odd"

    return "Even"

#아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : " + evenOrOdd(3))
print("결과 : " + evenOrOdd(2))