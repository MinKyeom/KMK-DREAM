# SQLAlchemy 작업의 예약 (임시 저장소 역할)
new_user = User(name="FastAPI")
db.add(new_user)  # 아직 DB에 저장되지 않음 (세션이 기억만 함)


# 트랜잭션의 완료 (commit)
db.commit()  # 이 시점에 실제 DB에 반영되고 트랜잭션이 성공적으로 끝남

# 트랜잭션의 취소 (rollback)
try:
    db.add(item1)
    db.add(item2)
    db.commit()
except Exception:
    db.rollback()  # 에러 발생 시 item1, item2 모두 저장되지 않고 취소됨
    

# FastAPI에서 권장하는 세션/트랜잭션 패턴
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from .database import SessionLocal

app = FastAPI()

# 세션 생성 및 자동 해제를 위한 의존성 함수
def get_db():
    db = SessionLocal()  # 1. 세션 오픈 (트랜잭션 시작)
    try:
        yield db         # 2. 비즈니스 로직에 세션 전달
    finally:
        db.close()       # 3. 요청이 끝나면 무조건 세션 닫기 (자원 해제)

@app.post("/items/")
def create_item(name: str, db: Session = Depends(get_db)):
    # 하나의 트랜잭션 범위
    new_item = Item(name=name)
    db.add(new_item)
    db.commit()          # 확정
    db.refresh(new_item)
    return new_item