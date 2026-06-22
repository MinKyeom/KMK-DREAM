import pandas as pd
from sqlalchemy import create_engine

source_engine = create_engine('postgresql://user:pass@source_host/db')
target_engine = create_engine('postgresql://user:pass@target_host/dw')

# 1. Extract: 소스 데이터 추출
df = pd.read_sql("SELECT id, name, amount FROM orders", source_engine)

# 2. Load: 가공하지 않고 타겟 저장소의 임시 테이블(Staging Table)에 그대로 적재
df.to_sql('stg_orders', target_engine, if_exists='replace', index=False)

# 3. Transform: 타겟 데이터 웨어하우스의 연산 능력을 활용해 SQL로 데이터 변환 및 최종 적재
with target_engine.begin() as conn:
    transform_query = """
        INSERT INTO fact_orders (id, name, amount)
        SELECT id, UPPER(name), amount 
        FROM stg_orders;
    """
    conn.execute(transform_query)