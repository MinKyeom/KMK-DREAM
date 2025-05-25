"""
 출처:프로그래머스,
 https://school.programmers.co.kr/learn/courses/30/lessons/284527
"""

# 풀이과정_개선 중
"""
  select max(C.SCORE) "SCORE", C.EMP_NO, B.EMP_NAME, B.POSITION, B.EMAIL
from HR_DEPARTMENT as A,HR_EMPLOYEES as B,
(select EMP_NO,YEAR ,sum(score) "SCORE"  
from HR_GRADE
group by EMP_NO,YEAR) as C
"""