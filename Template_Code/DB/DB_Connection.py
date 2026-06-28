from contextlib import contextmanager
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base

# 1. DB 연결 URL 설정 (사용자 환경에 맞게 수정)
# 형식: dialect+driver://username:password@host:port/database
DATABASE_URL = "mysql+pymysql://user:password@localhost:3306/my_database"

# 2. SQLAlchemy Engine 및 Session 생성 (커넥션 풀 포함)
engine = create_engine(
    DATABASE_URL,
    pool_size=10,         # 풀에 유지할 기본 커넥션 개수
    max_overflow=20,      # 풀이 넘칠 때 추가로 허용할 최대 커넥션 개수
    pool_recycle=3600,    # 커넥션 자동 재사용 시간 (초)
    pool_pre_ping=True    # 커넥션 사용 전 유효성 체크 (끊김 방지)
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# 3. 안전한 세션 관리를 위한 Context Manager (이용 후 자동 반환)
@contextmanager
def get_db():
    session = SessionLocal()
    try:
        yield session
        session.commit()  # 정상 종료 시 커밋
    except Exception as e:
        session.rollback() # 에러 발생 시 롤백
        print(f"Database error occurred: {e}")
        raise
    finally:
        session.close()   # 사용 완료 후 커넥션 풀로 반환

# 4. 실제 사용 예시
if __name__ == "__main__":
    # Context Manager를 사용하여 안전하게 쿼리 실행
    with get_db() as db:
        query = text("SELECT 1")
        result = db.execute(query).fetchone()
        print(f"Connection Success! Result: {result[0]}")