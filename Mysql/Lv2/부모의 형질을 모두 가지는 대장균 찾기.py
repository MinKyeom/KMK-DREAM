  """
  출처:프로그래머스,
  https://school.programmers.co.kr/learn/courses/30/lessons/301647
  """
  #풀이 과정_개선 중
  """
  -- bin(): 이진법 변환 -- 
  select ID,GENOTYPE,PARENT_ID "PARENT_GENOTYPE"
  from ECOLI_DATA
  -- 한 쪽은 현재 내 컬럼 Gentype = 부모 id의 Gentype --
  -- parent_id의 gentype을 들고 오는 방법 --
  where bin(GENOTYPE)
    =
    (select
  """
  
  # 풀이 과정_개선 중
  """
  -- bin(): 이진법 변환 -- 
select bin(ID),GENOTYPE,PARENT_ID "PARENT_GENOTYPE"
from ECOLI_DATA
where (select bin(PARENT_ID) from ECOLI_DATA) 
        =
      (select bin(ID) from ECOLI_DATA)
  """