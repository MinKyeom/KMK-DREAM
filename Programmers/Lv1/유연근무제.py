"""
출처: 프로그래머스,
https://school.programmers.co.kr/learn/courses/30/lessons/388351?language=python3
"""
  
  # 풀이 과정_개선 중 

"""
목표: 7일 동안 늦지 않고 지정한 출근 시간에 제대로 출근한 직원
단 토,일 제외
"""

def solution(schedules, timelogs, startday):
    result = 0
    
    for num,LimitTime in enumerate(schedules):
        
        # 요일 시작
        count = startday
        
        for person in timelogs[num]:
            if person <= LimitTime+10:
                count+=1
                continue
            
            elif count == 6 or count == 7:
                count+=1
                continue
            
            else:
                break
            
        else:
            result+=1
            
    
    return result
  