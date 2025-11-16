"""
출처:프로그래머스,
https://school.programmers.co.kr/learn/courses/30/lessons/451808?language=python3
"""
# 풀이 과정_개선 중
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
    
    for check in range(1,10):
        num = str(check)*4
        
        if submit(int(num)) != "0S 0B":
            baseball_number.append(str(check))
        
        if len(baseball_number) ==4:
            break
    
    check_list = list(permutations(baseball_number,4))
    
    for ball in check_list:
        go = "".join(ball)
        
        if submit(int(go)) == "4S 0B":
            return int(go)
    
    # for i in range(1000, 10000):
    #     if submit(i) == "4S 0B": return i
    
    
    return 0

# 풀이 과정_개선 중
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
    num = ["1","2","3","4","5","6","7","8","9"]
    
    check_list = list(permutations(num,4))

    print("".join(check_list[0]))
    
    check_list = list(map(list,check_list))
    
    
    # for i in range(1000, 10000):
    #     if submit(i) == "4S 0B": return i
    
    
    return 0

# 풀이 과정_개선 중 

"""
조건:
숫자가 비밀번호에 포함되어 있지 않다면 : OUT
숫자가 비밀번호에 포함되어 있지만, 위치가 틀렸다면 : BALL
숫자가 비밀번호에 포함되어 있고, 위치까지 정확하다면 : STRIKE

목표: 비밀번호 맞추기

체크사항: 임의의 함수가 변수로 주어지는 조건에 대하여 이해 방향성 고민
> submit를 호출한 횟수마다 어딘가에 횟수로 기록됨
> submit에 호출 시 xS yB로 출력됨
# 내부 로직을 만들어서 횟수를 최대로 줄이는 방향성으로 코드를 만들고 submit을 호출하는 방향성
"""

from itertools import permutations

def solution(n, submit):
    num = ["1","2","3","4","5","6","7","8","9"]
    
    check_list = list(permutations(num,4))

    print("".join(check_list[0]))
    
    check_list = list(map(list,check_list))
    
    
    # for i in range(1000, 10000):
    #     if submit(i) == "4S 0B": return i
    
    
    return 0
  

# 풀이 과정
"""
조건:
숫자가 비밀번호에 포함되어 있지 않다면 : OUT
숫자가 비밀번호에 포함되어 있지만, 위치가 틀렸다면 : BALL
숫자가 비밀번호에 포함되어 있고, 위치까지 정확하다면 : STRIKE

목표: 비밀번호 맞추기
"""
def solution(n, submit):
    
    for i in range(1000, 10000):
        if submit(i) == "4S 0B": return i
    
    return 0