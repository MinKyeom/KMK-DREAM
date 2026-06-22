

import pandas as pd
from sqlalchemy import create_engine

# 1. Extract: 소스 DB 또는 파일에서 원시 데이터 추출
source_engine = create_engine('postgresql://user:pass@source_host/db')
df = pd.read_sql("SELECT id, name, amount FROM orders", source_engine)

# 2. Transform: 파이썬(Pandas) 메모리 내에서 데이터 정제 및 변환
# 이름을 대문자로 변경하는 작업 수행
df['name'] = df['name'].str.upper()

# 3. Load: 타겟 데이터 웨어하우스에 정제된 데이터 적재
target_engine = create_engine('postgresql://user:pass@target_host/dw')
df.to_sql('fact_orders', target_engine, if_exists='append', index=False)