import os
import sqlite3
import json
from fastapi import FastAPI
from pydantic import BaseModel
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage # 💡 추가된 임포트

# --- DB 설정 ---
DB_PATH = os.path.join(os.path.dirname(__file__), "../data/user.db")
os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS user_info (
            id INTEGER PRIMARY KEY,
            key TEXT,
            value TEXT,
            is_private INTEGER DEFAULT 0
        )
    """)
    conn.commit()
    conn.close()

init_db()

# --- FastAPI 앱 ---
app = FastAPI()

# --- 상태 및 인증 ---
memory_state = {
    "saving_mode": False,
    "user_verified": False,
    "awaiting_access_code": False,
}
USER_VERIFY_CODE = "abcd"   # 본인 인증 코드
ACCESS_CODE = "1234"        # 개인 정보 접근 코드

class ChatPayload(BaseModel):
    message: str

# --- 프롬프트 파일 로드 ---
# ⚠️ 파일 경로가 정확한지 확인해 주세요.
prompt_path = os.path.join(os.path.dirname(__file__), "prompts/user_info_prompt.txt")
try:
    with open(prompt_path, "r", encoding="utf-8") as f:
        prompt_template = f.read()
except FileNotFoundError:
    print(f"오류: 프롬프트 파일이 없습니다. 경로: {prompt_path}")
    prompt_template = "Please extract the key-value pairs from the user message: {user_message}. Respond only in JSON format, including an 'is_private' boolean key."


# --- LLM 초기화 ---
llm = ChatOllama(model="qwen2.5:1.5b", temperature=0.7)

# --- DB 유틸 함수 ---
def parse_and_save(parsed_json: dict, is_private: bool):
    if not isinstance(parsed_json, dict):
        raise ValueError(f"parsed_json must be dict, got {type(parsed_json)}")
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    for k, v in parsed_json.items():
        if isinstance(v, list):
            for item in v:
                cur.execute(
                    "INSERT INTO user_info (key, value, is_private) VALUES (?, ?, ?)",
                    (k, item, int(is_private))
                )
        else:
            cur.execute(
                "INSERT INTO user_info (key, value, is_private) VALUES (?, ?, ?)",
                (k, v, int(is_private))
            )
    conn.commit()
    conn.close()

def query_info(key: str, private: bool):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute(
        "SELECT value FROM user_info WHERE key=? AND is_private=?",
        (key, int(private))
    )
    rows = cur.fetchall()
    conn.close()
    return [r[0] for r in rows]

# --- FastAPI 엔드포인트 ---
@app.post("/chat")
def chat_endpoint(data: ChatPayload):
    msg = data.message.strip()

    # 1️⃣ 저장 모드 시작
    if msg == "내 정보를 저장하고 싶어":
        memory_state["saving_mode"] = True
        memory_state["user_verified"] = False
        return {"response": "좋아요! 먼저 본인을 증명해주세요."}

    # 2️⃣ 본인 인증
    if memory_state["saving_mode"] and not memory_state["user_verified"]:
        if msg == USER_VERIFY_CODE:
            memory_state["user_verified"] = True
            return {"response": "본인 인증 완료! '나는 ~~'으로 정보를 입력해주세요."}
        else:
            return {"response": "본인 인증 실패."}

    # 3️⃣ 저장 모드 진행
    if memory_state["saving_mode"] and memory_state["user_verified"]:
        if msg.startswith("나는"):
            prompt = prompt_template.replace("{user_message}", msg)
            try:
                # 💡 수정된 부분: llm.invoke 사용
                response_message = llm.invoke([HumanMessage(content=prompt)])
                text = response_message.content

                # JSON 파싱 시도
                try:
                    parsed_json = json.loads(text.strip())
                except json.JSONDecodeError:
                    return {"response": f"LLM 출력 JSON 파싱 오류: {text}"}

                is_priv = parsed_json.pop("is_private", False)
                parse_and_save(parsed_json, is_priv)
                memory_state["saving_mode"] = False # 저장 후 모드 종료 (선택적)
                memory_state["user_verified"] = False
                return {"response": "정보가 저장되었습니다. 저장 모드를 종료합니다."}

            except Exception as e:
                # 이제는 'str' object has no attribute 'content' 오류 대신 실제 LLM 호출 오류가 표시될 것입니다.
                return {"response": f"LLM 호출 오류: {e}"}
        
        elif msg in ["끝", "저장 완료"]:
            memory_state["saving_mode"] = False
            memory_state["user_verified"] = False
            return {"response": "정보 저장 완료."}

    # 4️⃣ 공개 정보 조회
    if "좋아" in msg or "취미" in msg:
        vals = query_info("interest", False)
        if vals:
            return {"response": f"나는 {', '.join(vals)} 좋아해요."}
    if "공부" in msg:
        vals = query_info("study", False)
        if vals:
            return {"response": f"요즘 {', '.join(vals)} 공부 중이에요."}

    # 5️⃣ 개인 정보 접근 요청
    if "특정 정보" in msg or "접근" in msg:
        memory_state["awaiting_access_code"] = True
        return {"response": "접근 코드를 입력해주세요."}

    if memory_state.get("awaiting_access_code", False):
        if msg == ACCESS_CODE:
            vals_interest = query_info("interest", True)
            vals_study = query_info("study", True)
            parts = []
            if vals_interest:
                parts.append("좋아하는 것: " + ", ".join(vals_interest))
            if vals_study:
                parts.append("공부 중: " + ", ".join(vals_study))
            memory_state["awaiting_access_code"] = False
            return {"response": "개인 정보: " + "; ".join(parts)}
        else:
            return {"response": "코드가 틀렸어요."}

    return {"response": "무슨 말인지 잘 모르겠어요."}

# --- 서버 실행 ---
if __name__ == "__main__":
    import uvicorn
    # ⚠️ 테스트 환경에서 상태 관리가 꼬이는 것을 방지하기 위해 workers=1을 권장합니다.
    uvicorn.run(app, host="0.0.0.0", port=8001, workers=1)