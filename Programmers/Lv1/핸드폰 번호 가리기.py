# 내 풀이
def solution(phone_number):
    k=len(phone_number[:len(phone_number)-4])
    return "*"*k+phone_number[len(phone_number)-4:]

# 다른 사람 풀이
def hide_numbers(s):


    return "*"*(len(s)-4)+s[-4:]
    #함수를 완성해 별이를 도와주세요

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : " + hide_numbers('01033334444'));