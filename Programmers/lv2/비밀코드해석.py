"""
  출처:프로그래머스,
  https://school.programmers.co.kr/learn/courses/30/lessons/388352
"""
#풀이 과정_개선 중 
from itertools import combinations

"""
n: 가능한 자연수 개수 
q: 시도한 자연수 배열 집합
ans: 맞춘 자연수 개수 집합
> 스무고개 아이디어 생각!
"""

def solution(n, q, ans):
    a=list(combinations([1,2],2))
    
    
    return 0