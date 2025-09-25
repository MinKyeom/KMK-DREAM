"""
출처: 프로그래머스,
https://school.programmers.co.kr/learn/courses/30/lessons/389481
"""
# 풀이 과정_개선 중
"""
조건
- 알파벳 소문자 11글자 이하
- 글자 수가 적은 주문부터 기록
- 글자 수가 적다면 사전 순서대로
"""

"""
- 일반적인 사고 11자리 모두를 구하고 필요한 숫자들을 제거한 후 원하는 알파벳의 위치를 아는 방법

아이디어
- 알파벳 개수를 각 자릿수의 숫자로 생각하고 더해주는 방식
- 26진법으로 문제 풀이 접근
"""

from collections import deque
from collections import defaultdict

def solution(n, bans):
    
    alpha = "abcdefghijklmnopqrstuvwxyz"
    alpha_num = list(alpha)
    alpha_num_dic = defaultdict(int)
    
    num_count = 0 #알파벳 넘버링
    
    for insert_alpha in alpha_num:
        alpha_num_dic[insert_alpha] = num_count
        num_count+=1

    ban_num = [] 
    
    for ban in bans:
        b = deque(list(ban))
        count = 0  # 26진법 시작
        number = 0 # 밴한 숫자의 넘버
        
        while b:
            a = b.pop() # 알파벳 추출
            a_num = alpha_num_dic[a]
            
            if a_num == 0:
                number+=1
                count+=1
                continue
            
            number+=(26**count)*a_num
            count+=1
        
        ban_num.append(number)
    
    # 시작 번호
    start = n
    end = n
    
    for i in ban_num:
        if i < start:
            end += 1 
    
    result = ""
    
    while end >= 26:
        
        end,j= divmod(end,26)
        result = alpha[j] + result
    
    print(result)
    
    return 0
 

# 풀이 과정_개선 중
"""

조건
- 알파벳 소문자 11글자 이하
- 글자 수가 적은 주문부터 기록
- 글자 수가 적다면 사전 순서대로

"""

"""

- 일반적인 사고 11자리 모두를 구하고 필요한 숫자들을 제거한 후 원하는 알파벳의 위치를 아는 방법

아이디어
- 알파벳 개수를 각 자릿수의 숫자로 생각하고 더해주는 방식
- 26진법으로 문제 풀이 접근
"""
from collections import deque
from collections import defaultdict

def solution(n, bans):
    
    alpha = "abcdefghijklmnopqrstuvwxyz"
    alpha_num = list(alpha)
    alpha_num_dic = defaultdict(int)
    
    num_count = 0 #알파벳 넘버링
    
    for insert_alpha in alpha_num:
        alpha_num_dic[insert_alpha] = num_count
        num_count+=1

    ban_num = [] 
    
    for ban in bans:
        b = deque(list(ban))
        count = 0  # 26진법 시작
        number = 0 # 밴한 숫자의 넘버
        
#         while b:
        
        
    return 0