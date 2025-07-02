"""
출처:프로그래머스,
https://school.programmers.co.kr/learn/courses/30/lessons/389480
"""
# 풀이 과정

from collections import deque

def solution(info, n, m):
    q=deque( [ [0,0] ] )    
    
    check=deque(info)
    visited = set([(0,0)])
    
    result=[]
    
    while check:
        # 감당해야할 리스크
        da,db=check.popleft()
        
        # 리스크를 감당했을 때의 위험도 담는 곳
        new_q=deque([])
        
        while q:
            a,b=q.popleft()
            
            if a>=n or b>=m:
                continue
            
            elif a<n and b>=m: 
                new_q.append((a+da,b))
            
            elif a>=n and b<m:
                new_q.append((a,b+db))

            else:
                new_q.append((a+da,b))
                new_q.append((a,b+db))
                
        
        if len(new_q)==0:
            return -1
        
        if len(check)==0:
            result=deque(set(new_q))
        
        else:
            q=q+deque(set(new_q))
    final=[]
    
    for last_a,last_b in result:
        if last_a < n and last_b <m:
            final.append(last_a)
    
    return -1 if len(final) == 0 else min(final) 

# 풀이 과정_개선 중
# """
# info A도둑이 훔치면 인덱스 0이 흔적이 남는다
# info B도둑이 훔치면 인덱스 1이 흔적이 남는다

# 목표:A도둑이 경찰에 붙잡히는 최소 흔적 개수의 최솟값

# > 매 순간 둘 중 하나가 훔치면서 목적이 달성되는 순간의 A의 값을 내면 된다
# > bfs로 각 두 가지 경우를 q에 넣고 매 q마다 둘 중 하나를 잡히는 경우를 제외하면서 진행하면 된다
# > heapq로 a가 항상 최소가 되는 값부터 뽑아서 쓰는 방법도 존재한다

# 물건 모두 가져가는 상황 자체가 불가능한 경우는 -1 리턴
# """

# """
# 시간 초과 역시나...
# 모든 경우의 수가 아닌 a가 최솟값인 상황에서 q를 해주는 상황으로 구현하는거 생각 > heapq 
# 번거롭더라도 시간을 빠르게 가져가는 효율성 코드를 구현하는 방향에서 고민해보자!

# or  다이나믹 프로그래밍으로 점차 늘려가는 방식 찾기!
# """
# from collections import deque

# def solution(info, n, m):
#     q=deque( [ [0,0] ] )    
    
#     check=deque(info)
    
#     result=[]
    
#     while check:
#         # 감당해야할 리스크
#         da,db=check.popleft()
        
#         # 리스크를 감당했을 때의 위험도 담는 곳
#         new_q=deque([])
        
#         while q:
#             a,b=q.popleft()
            
#             if a>=n or b>=m:
#                 continue
            
#             elif a<n and b>=m: 
#                 new_q.append([a+da,b])
            
#             elif a>=n and b<m:
#                 new_q.append([a,b+db])
            
#             else:
#                 new_q.append([a+da,b])
#                 new_q.append([a,b+db])
        
#         if len(new_q)==0:
#             return -1
        
#         if len(check)==0:
#             result=new_q
        
#         else:
#             q=q+new_q
    
#     final=[]
    
#     for last_a,last_b in result:
#         if last_a < n and last_b <m:
#             final.append(last_a)
    
#     return -1 if len(final) == 0 else min(final) 

def solution(info, n, m):
    info = sorted (info, key = lambda x:(-x[0],x[1]))
    
    print(info)
    
    n_num,m_num = 0,0 
    
    for i,j in info:
        if m_num + j < m:
            m_num+=j
        elif n_num + i < n:
            n_num+=i
        else:
            return -1
        
    
    return n_num
# 풀이 과정_개선 중
"""
info A도둑이 훔치면 인덱스 0이 흔적이 남는다
info B도둑이 훔치면 인덱스 1이 흔적이 남는다

목표:A도둑이 경찰에 붙잡히는 최소 흔적 개수의 최솟값

> 매 순간 둘 중 하나가 훔치면서 목적이 달성되는 순간의 A의 값을 내면 된다
> bfs로 각 두 가지 경우를 q에 넣고 매 q마다 둘 중 하나를 잡히는 경우를 제외하면서 진행하면 된다
> heapq로 a가 항상 최소가 되는 값부터 뽑아서 쓰는 방법도 존재한다

물건 모두 가져가는 상황 자체가 불가능한 경우는 -1 리턴
"""

"""
시간 초과 역시나...
모든 경우의 수가 아닌 a가 최솟값인 상황에서 q를 해주는 상황으로 구현하는거 생각 > heapq 
번거롭더라도 시간을 빠르게 가져가는 효율성 코드를 구현하는 방향에서 고민해보자!

or  다이나믹 프로그래밍으로 점차 늘려가는 방식 찾기!
"""
from collections import deque

def solution(info, n, m):
    q=deque( [ [0,0] ] )    
    
    check=deque(info)
    
    result=[]
    
    while check:
        # 감당해야할 리스크
        da,db=check.popleft()
        
        # 리스크를 감당했을 때의 위험도 담는 곳
        new_q=deque([])
        
        while q:
            a,b=q.popleft()
            
            if a>=n or b>=m:
                continue
            
            elif a<n and b>=m: 
                new_q.append([a+da,b])
            
            elif a>=n and b<m:
                new_q.append([a,b+db])
            
            else:
                new_q.append([a+da,b])
                new_q.append([a,b+db])
        
        if len(new_q)==0:
            return -1
        
        if len(check)==0:
            result=new_q
        
        else:
            q=q+new_q
    
    final=[]
    
    for last_a,last_b in result:
        if last_a < n and last_b <m:
            final.append(last_a)
    
    return -1 if len(final) == 0 else min(final) 

# 풀이과정_개선 중 

"""
info A도둑이 훔치면 인덱스 0이 흔적이 남는다
info B도둑이 훔치면 인덱스 1이 흔적이 남는다

목표:A도둑이 경찰에 붙잡히는 최소 흔적 개수의 최솟값

> 매 순간 둘 중 하나가 훔치면서 목적이 달성되는 순간의 A의 값을 내면 된다
> bfs로 각 두 가지 경우를 q에 넣고 매 q마다 둘 중 하나를 잡히는 경우를 제외하면서 진행하면 된다
> heapq로 a가 항상 최소가 되는 값부터 뽑아서 쓰는 방법도 존재한다

물건 모두 가져가는 상황 자체가 불가능한 경우는 -1 리턴
"""

from collections import deque

def solution(info, n, m):
    q=deque( [ [0,0] ] )    
    
    check=deque(info)
    
    result=[]
    
    while check:
        # 감당해야할 리스크
        da,db=check.popleft()
        
        # 리스크를 감당했을 때의 위험도 담는 곳
        new_q=deque([])
        
        while q:
            a,b=q.popleft()
            
            if a>=n or b>=m:
                continue
            
            elif a<n and b>=m: 
                new_q.append([a+da,b])
            
            elif a>=n and b<m:
                new_q.append([a,b+db])
            else:
                new_q.append([a+da,b])
                new_q.append([a,b+db])
        
        if len(check)==0:
            result=new_q
        else:
            q=q+new_q
    
    final=[]
    
    for last_a,last_b in result:
        if last_a < n and last_b <m:
            final.append(last_a)
    
    return -1 if len(final) == 0 else min(final) 
    
# 풀이과정_개선 중
  """
info A도둑이 훔치면 인덱스 0이 흔적이 남는다
info B도둑이 훔치면 인덱스 1이 흔적이 남는다

목표:A도둑이 경찰에 붙잡히는 최소 흔적 개수의 최솟값

> 매 순간 둘 중 하나가 훔치면서 목적이 달성되는 순간의 A의 값을 내면 된다
> bfs로 각 두 가지 경우를 q에 넣고 매 q마다 둘 중 하나를 잡히는 경우를 제외하면서 진행하면 된다
> heapq로 a가 항상 최소가 되는 값부터 뽑아서 쓰는 방법도 존재한다

물건 모두 가져가는 상황 자체가 불가능한 경우는 -1 리턴
"""
from collections import deque

def solution(info, n, m):
    q=deque([ [0,0] ])    
    check=deque([info])
    
    result=[]
    
    while check:
        # 감당해야할 리스크
        da,db=check.popleft()
        
        # 리스크를 감당했을 때의 위험도 담는 곳
        new_q=[]
        print(da,db)
        break
        while q:
            a,b=q.popleft()
            
            if a>=n or b>=m:
                continue
            else:
                continue
    
    return -1 if len(result) = 0 else min(result)