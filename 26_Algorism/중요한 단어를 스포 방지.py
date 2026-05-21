# 풀이과정
# 소문자와 숫자로만 구성됨
"""
프로그래머스:중요한 단어를 스포 방지
https://school.programmers.co.kr/learn/courses/30/lessons/468370?language=python3
"""
def solution(message, spoiler_ranges):
    test = message.split(" ")
    
    for start,end in spoiler_ranges:
        print(message[start:end+1])
    answer = 0
    return answer