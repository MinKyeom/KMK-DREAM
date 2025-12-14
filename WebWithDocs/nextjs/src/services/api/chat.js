// src/services/api/chat.js

import axios from "axios";

// 챗봇 FastAPI 서버 URL (FastAPI 서버가 8000번 포트에서 실행된다고 가정)
const CHAT_API_URL = "http://localhost:8000/chat";

/**
 * 챗봇과 대화 요청을 전송하는 함수
 * @param {string} session_id - 사용자의 고유 ID (인증된 경우 localStorage의 currentUserId 사용)
 * @param {string} message - 사용자 입력 메시지
 * @returns {Promise<string>} 챗봇의 응답 메시지 문자열
 */
export const sendChatMessage = async (session_id, message) => {
  try {
    const response = await axios.post(CHAT_API_URL, {
      session_id, // FastAPI에서 세션/기억 관리에 사용
      message,
    });
    // FastAPI app.py에서 {response: "..."} 형태로 응답
    return response.data.response;
  } catch (error) {
    console.error("챗봇 API 통신 오류:", error);
    // 사용자에게 친화적인 오류 메시지를 반환합니다.
    return "챗봇 서버에 연결할 수 없거나, 통신 오류가 발생했습니다.";
  }
};