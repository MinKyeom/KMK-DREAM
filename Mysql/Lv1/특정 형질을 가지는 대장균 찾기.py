"""
출처: 프로그래머스
https://school.programmers.co.kr/learn/courses/30/lessons/301646
"""


# 풀이 과정
# 각 형질을 2진법으로 변환 > 슬라이싱 > 해당되는 것만 출력
# CONV(1111, 2, 10) AS "2진수 1111
"""
select
count(GENOTYPE)
"COUNT"

from ECOLI_DATA

where(

    right((SELECT CONVERT(bin(GENOTYPE), CHAR)), 3)="001"

OR

right((SELECT CONVERT(bin(GENOTYPE), CHAR)), 3)="100"

OR

right((SELECT CONVERT(bin(GENOTYPE), CHAR)), 3)="101"

OR

right((SELECT CONVERT(bin(GENOTYPE), CHAR)), 3)="1"

);
"""