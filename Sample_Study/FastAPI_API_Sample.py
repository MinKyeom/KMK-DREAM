from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

# 1. FastAPI 인스턴스 생성
app = FastAPI()

# 간단한 데이터 모델 정의 (요청 본문 검증용)
class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None

# 2. GET 요청 (기본 홈 경로)
@app.get("/")
def read_root():
    return {"message": "안녕하세요! FastAPI 세계에 오신 것을 환영합니다."}

# 3. GET 요청 (경로 매개변수 및 쿼리 매개변수 사용)
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "query_param": q}

# 4. POST 요청 (데이터 생성)
@app.post("/items/")
def create_item(item: Item):
    return {"message": "아이템이 성공적으로 생성되었습니다.", "data": item}
  
@app.get("/health/")
def health_check():
  return {"message": "health"}