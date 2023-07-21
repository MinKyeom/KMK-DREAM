# 내 풀이
def solution(n):
    k=list(str(n))
    k=list(map(int,k))

    return sum(k)

# 다른 사람 풀이
def sum_digit(number):
    '''number의 각 자릿수를 더해서 return하세요'''
    if number < 10:
        return number

    return number%10 + sum_digit(number//10)