"""
출처: 프로그래머스 코딩 테스트 연습,
https://school.programmers.co.kr/learn/courses/30/lessons/120912
"""
# 풀이1
def solution(array):
    b=list(map(str,array))
    c=[]
    count=0
    for x in b:
        d=list(x)
        c=c+d
    for y in range(len(c)):
        if c[y]=="7":
            count+=1
    answer = count
    return answer

# 풀이2

def solution(array):
    # answer = 0
    # for x in array:
    #     xx = str(x)
    #     for y in xx:
    #         if y == "7":
    #             answer+=1
    # return answer
    return str(array).count("7")