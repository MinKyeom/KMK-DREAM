# 내 풀이
def solution(money):
    x=int(money/5500)
    y=money%5500
    return [x,y]
# 다른 사람 풀이
def solution(money):

    answer = [money // 5500, money % 5500]
    return answer
