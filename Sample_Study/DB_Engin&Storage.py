"""
예시 쿼리

SELECT user_id, SUM(amount) AS total_spent
FROM orders
WHERE order_date >= '2026-01-01'
GROUP BY user_id
HAVING total_spent >= 100000
ORDER BY total_spent DESC;
  
"""

"""
# 쿼리 엔진의 역할

# 쿼리 엔진의 내부 논리 흐름 (추상화된 코드)

def query_engine_process():
  
    # 1. 구문 분석 및 권한 체크
    parse_and_validate_sql(sql)
    
    # 2. 최적화 (Optimizer): 인덱스를 쓸지, 풀 스캔을 할지 결정
    execution_plan = find_best_way_to_fetch_data() 
    
    # 3. 스토리지 엔진에게 "데이터 가져와!"라고 요청 (가장 중요)
    # 쿼리 엔진은 'order_date' 조건만 주고 raw 데이터를 받아옵니다.
    raw_rows = storage_engine.fetch_rows(condition="order_date >= '2026-01-01'")
    
    # 4. 가져온 데이터를 바탕으로 본격적인 '연산' 시작 (메모리/CPU 작업)
    grouped_data = {}
    for row in raw_rows:
        # GROUP BY user_id 연산
        grouped_data[row.user_id] = grouped_data.get(row.user_id, 0) + row.amount
        
    # 5. HAVING 조건 필터링 (10만 원 이상만 남기기)
    filtered_data = {k: v for k, v in grouped_data.items() if v >= 100000}
    
    # 6. ORDER BY 연산 (정렬)
    sorted_result = sorted(filtered_data.items(), key=lambda x: x[1], reverse=True)
    
    return sorted_result
    
"""


"""
위의 쿼리 엔진 코드 중 storage_engine.fetch_rows()가 호출되는 순간 스토리지 엔진이 일하기 시작합니다. 
디스크(SSD)에서 데이터를 실제로 꺼내오는 물리적인 작업입니다.
스토리지 엔진(예: InnoDB)의 내부 코드는 대략 이런 식으로 움직입니다.

# 스토리지 엔진의 내부 논리 흐름 (추상화된 코드)

def fetch_rows(condition):
    results = []
    
    # 1. 디스크 버퍼(Buffer Pool) 메모리에 원하는 데이터 블록이 이미 있는지 확인
    # (디스크 읽기는 느리니까 메모리부터 확인하는 창고지기의 노하우)
    cached_blocks = check_memory_buffer_cache("orders_table")
    
    # 2. 메모리에 없으면 실제 파일 시스템(디스크)에서 파일 읽기
    if not cached_blocks:
        # 파일 시스템의 특정 이진(Binary) 파일에서 16KB 단위 블록들을 읽어옴
        raw_bytes = disk_drive.read_file(path="/var/lib/mysql/data/orders.ibd", block_size="16KB")
        cached_blocks = deserialize_bytes_to_rows(raw_bytes)
        add_to_buffer_pool(cached_blocks)
        
    # 3. 인덱스(B+Tree 구조)를 태워서 조건에 맞는 데이터만 빠르게 추려냄
    for row in cached_blocks:
        if row.order_date >= '2026-01-01':
            # 트랜잭션 격리 수준(MVCC)을 확인하여 현재 이 사용자가 봐도 되는 버전의 데이터인지 검증
            if is_visible_to_current_transaction(row):
                results.append(row)
                
    # 4. 쿼리 엔진에게 날것(Raw)의 데이터 포인터 또는 배열을 반환
    return results

핵심 특징: 스토리지 엔진은 SUM이 뭔지, ORDER BY로 어떻게 정렬하는지 모릅니다. 
오직 파일에서 바이트(Byte) 데이터를 읽어와 유효한 레코드로 변환하고, 데이터가 깨지지 않게 잠금(Locking)과 트랜잭션을 관리하는 데 집중합니다.    
"""


"""
종합 요약 

쿼리 엔진SQL 해석 > 실행 계획 수립 > 스토리지 엔진 호출    즉 "어떻게 가져올지 전략 짜기"

스토리지 엔진디스크 파일 열기 > 16KB 블록 읽기 > 로우(Row) 형태로 변환 즉 "디스크에서 진짜 데이터 꺼내오기"

쿼리 엔진 받은 데이터 합산(SUM) > 그룹화(GROUP BY) > 정렬(ORDER BY) 즉 "가져온 데이터로 요리(연산)하기"

"""