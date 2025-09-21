"""
출처: 프로그래머스,
https://school.programmers.co.kr/learn/courses/30/lessons/388351?language=python3
"""
# 풀이 과정_개선 중
"""
목표: 7일 동안 늦지 않고 지정한 출근 시간에 제대로 출근한 직원
단 토,일 제외

> 100으로 나눈 나머지는 59이하 입니다의 의미 파악!!
"""
def solution(schedules, timelogs, startday):
    result = 0
    
    for num,LimitTime in enumerate(schedules):
        
        # 요일 시작
        count = startday
        
        # 10분 더했을 때 시간 60분이 넘어서 다른 판단을 해야한다!
        if (LimitTime+10)%100 > 59:
            LimitTime = LimitTime+100-60
        
        for person in timelogs[num]:    
            
            if person <= LimitTime + 10:
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

# 풀이 과정_개선 중
"""
목표: 7일 동안 늦지 않고 지정한 출근 시간에 제대로 출근한 직원
단 토,일 제외

> 100으로 나눈 나머지는 59이하 입니다의 의미 파악!!
"""

def solution(schedules, timelogs, startday):
    result = 0
    
    for num,LimitTime in enumerate(schedules):
        
        # 요일 시작
        count = startday
        
        # 10분 더했을 때 시간 60분이 넘어서 다른 판단을 해야한다!
        if (LimitTime+10)%100 >= 60:
            LimitTime = LimitTime+100-50
        
        for person in timelogs[num]:    
            
            if person <= LimitTime + 10:
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
  
# 풀이 과정_개선 중
"""
목표: 7일 동안 늦지 않고 지정한 출근 시간에 제대로 출근한 직원
단 토,일 제외

> 100으로 나눈 나머지는 59이하 입니다의 의미 파악!!
"""

def solution(schedules, timelogs, startday):
    result = 0
    
    for num,LimitTime in enumerate(schedules):
        
        # 요일 시작
        count = startday
        
        for person in timelogs[num]:
            # 10분 더했을 때 시간 60분이 넘어서 다른 판단을 해야한다!
            if (LimitTime+10)%100 >= 60:
                LimitTime = LimitTime+100-60
                
            if person <= LimitTime + 10:
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
  
  
  # 다른 사람 풀이
def solution(schedules, timelogs, startday):
    result = 0
    
    # 직원 순회
    for i in range(len(schedules)):
        schedule = convert(schedules[i]) + 10
        timelog = timelogs[i]
        cur_day = startday - 1
        
        # 출근 기록 순회
        for log in timelog:
            cur_day += 1
            
            # 토, 일은 제외
            if cur_day % 7 in [0, 6]:
                continue
            
            # 지각 체크
            if convert(log) > schedule:
                break
        else:
            result += 1
        
    return result
            
def convert(time):
    time = str(time)
    h, m = time[:-2], time[-2:]
    return int(h)*60 + int(m)