
# 출처: 프로그래머스 
# Link: https://school.programmers.co.kr/learn/courses/30/lessons/451808

"""
조건:
숫자가 비밀번호에 포함되어 있지 않다면 : OUT
숫자가 비밀번호에 포함되어 있지만, 위치가 틀렸다면 : BALL
숫자가 비밀번호에 포함되어 있고, 위치까지 정확하다면 : STRIKE
기회 n번

목표: 비밀번호 맞추기

체크사항: 임의의 함수가 변수로 주어지는 조건에 대하여 이해 방향성 고민
> submit를 호출한 횟수마다 어딘가에 횟수로 기록됨
> submit에 호출 시 xS yB로 출력됨
# 내부 로직을 만들어서 횟수를 최대로 줄이는 방향성으로 코드를 만들고 submit을 호출하는 방향성

의문사항: 정해진 n이 극도로 적어지면 찾는 게 가능한가?
정답이 정해져 있으면 만약 그 해당 번호만 넣어버리고 호출하면 정답인가?
어떻게 return i를 호출하는데 결과가 True,False로 나오는건가
submit을 호출해서 return 받는 게 아닌데 어떻게 true false가 나오는건가

"""
# 풀이 개선 중
"""
조건:
숫자가 비밀번호에 포함되어 있지 않다면 : OUT
숫자가 비밀번호에 포함되어 있지만, 위치가 틀렸다면 : BALL
숫자가 비밀번호에 포함되어 있고, 위치까지 정확하다면 : STRIKE
기회 n번

목표: 비밀번호 맞추기

체크사항: 임의의 함수가 변수로 주어지는 조건에 대하여 이해 방향성 고민
> submit를 호출한 횟수마다 어딘가에 횟수로 기록됨
> submit에 호출 시 xS yB로 출력됨
# 내부 로직을 만들어서 횟수를 최대로 줄이는 방향성으로 코드를 만들고 submit을 호출하는 방향성

의문사항: 정해진 n이 극도로 적어지면 찾는 게 가능한가?
정답이 정해져 있으면 만약 그 해당 번호만 넣어버리고 호출하면 정답인가?
어떻게 return i를 호출하는데 결과가 True,False로 나오는건가
submit을 호출해서 return 받는 게 아닌데 어떻게 true false가 나오는건가

"""

from itertools import permutations

def solution(n, submit):
#     num = ["1","2","3","4","5","6","7","8","9"]
    
#     check_list = list(permutations(num,4))

#     print("".join(check_list[0]))
    
#     check_list = list(map(list,check_list))
    
    baseball_number = [] 
    
    """
    숫자를 찾고 0을 활용해 매 숫자마다 위치를 찾는 방식으로 하면 9*4 36회 가능
    
    생각 방향 및 의문 사항
    들어갈 숫자를 찾기
    숫자의 정확한 위치 찾기
    
    두 개를 동시에 같이 가능한가?
    """
    
    """
    1234,2345,3456,4567,5678,6789
    """
    
    for check in range(1,10):
        num = str(check)*4
        
        if submit(int(num)) != "0S 0B":
            baseball_number.append(str(check))
        
        if len(baseball_number) ==4:
            break
    
    check_list = list(permutations(baseball_number,4)) # 호출횟수 포함 안됨
    
    # baseball_number에 숫자 일단 정해짐 
    # 하나를 정하고 위치를 찾으면 나머지는 3자리 중에서 하나를 정하면 3(첫 번째가 최악이여도 3번 안에 위치 나옴)
    # 두 번째는 2번 안에 결과 그 다음은 1번 안에 결과 도출
    
    result = ["0","0","0","0"]
    
    # 첫번째 숫자 정함
    start = baseball_number[0]
    
    flag = False
    
    case1 = start+"000"
    if flag ==False and submit(int(case1)) == "1S 0B":
        result[0]= start
        flag = True
        
    case2 = "0"+start+"00" 
    if flag==False and submit(int(case2)) == "1S 0B":
        result[1] = start
        flag = True
        
    case3 = "00"+start+"0"    
    if flag == False and submit(int(case3)) == "1S 0B":
        result[2] = start
        flag = True
    
    if flag == False:
        result[3] = start
    
    new_check = baseball_number[1:3]
    
    for check in new_check:
        for r in range(len(result)):
            if result[r] !="0":
                # 새로운 숫자 배정 가정
                result[r] = check
            else:
                continue
                
#     for ball in check_list:
#         go = "".join(ball)
        
#         if submit(int(go)) == "4S 0B":
#             return int(go)
    
    # for i in range(1000, 10000):
    #     if submit(i) == "4S 0B": return i
    
    
    return 0


# 풀이 개선_중
from itertools import permutations

def solution(n, submit):
#     num = ["1","2","3","4","5","6","7","8","9"]
    
#     check_list = list(permutations(num,4))

#     print("".join(check_list[0]))
    
#     check_list = list(map(list,check_list))
    
    baseball_number = [] 
    
    """
    숫자를 찾고 0을 활용해 매 숫자마다 위치를 찾는 방식으로 하면 9*4 36회 가능
    
    생각 방향 및 의문 사항
    들어갈 숫자를 찾기
    숫자의 정확한 위치 찾기
    서로 다른 수 
    
    두 개를 동시에 같이 가능한가?
    """
    
    """
    1234,2345,3456,4567,5678,6789
    """
    
    for check in range(1,10):
        num = str(check)*4
        
        if submit(int(num)) != "0S 0B":
            baseball_number.append(str(check))
        
        if len(baseball_number) ==4:
            break
    
    check_list = list(permutations(baseball_number,4)) # 호출횟수 포함 안됨
    
    for ball in check_list:
        go = "".join(ball)
        
        if submit(int(go)) == "4S 0B":
            return int(go)
    
    # for i in range(1000, 10000):
    #     if submit(i) == "4S 0B": return i
    
    
    return 0