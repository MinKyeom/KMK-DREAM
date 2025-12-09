// src/components/Chatbot.jsx

import React, { useState, useEffect, useRef } from "react";
import { sendChatMessage } from "../api/chat"; // 1번에서 작성한 API 함수
import { getAuthUser } from "../api/auth"; // 기존 인증 유틸리티
import "./Chatbot.css"; // 3번에서 작성할 스타일시트

export default function Chatbot({ isChatOpen, setIsChatOpen }) {
  // 채팅 메시지 상태: [{ role: 'user'/'assistant', text: 'message' }]
  const [messages, setMessages] = useState([]);
  const [inputMessage, setInputMessage] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  
  // 로그인된 사용자 ID를 가져와 챗봇 세션 ID로 사용
  const { id: currentUserId } = getAuthUser();
  const sessionId = currentUserId || "guest_user"; // 비로그인 시 'guest_user' 사용

  const messagesEndRef = useRef(null);

  // 메시지가 추가될 때마다 스크롤을 맨 아래로 이동
  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  // 채팅 메시지 전송 핸들러
  const handleSend = async (e) => {
    e.preventDefault();
    if (inputMessage.trim() === "" || isLoading) return;

    const userMessage = inputMessage.trim();
    // 1. 사용자 메시지 추가 및 입력 필드 초기화
    setMessages((prev) => [...prev, { role: "user", text: userMessage }]);
    setInputMessage("");
    setIsLoading(true);

    try {
      // 2. 챗봇 API 호출
      const botResponse = await sendChatMessage(sessionId, userMessage);

      // 3. 챗봇 응답 메시지 추가
      setMessages((prev) => [...prev, { role: "assistant", text: botResponse }]);
    } catch (error) {
      // API 통신 오류 발생 시 오류 메시지 표시
      setMessages((prev) => [
        ...prev,
        { role: "assistant", text: "오류: 챗봇과 통신 중 문제가 발생했습니다." },
      ]);
      console.error("Chatbot response error:", error);
    } finally {
      setIsLoading(false);
    }
  };

  // isChatOpen 상태가 false이면 아무것도 렌더링하지 않음 (App.jsx에서 처리)
  if (!isChatOpen) return null;

  return (
    <div className="chatbot-container">
      <div className="chatbot-header">
        <span>
          <span role="img" aria-label="robot">🤖</span> Blog Assistant
        </span>
        <button className="chatbot-close-btn" onClick={() => setIsChatOpen(false)}>
          &times;
        </button>
      </div>

      <div className="chatbot-messages">
        {messages.length === 0 && (
          <div className="chatbot-welcome">
            안녕하세요! 블로그 챗봇입니다.<br/>
            궁금한 점을 물어보거나, 관심사/공부 내용을 저장해 보세요.
            <br/><br/>
            {currentUserId 
              ? `👤 ${currentUserId} 님으로 세션이 시작됩니다.`
              : `**비회원** 세션입니다. 로그인 시 기록이 유지됩니다.`
            }
          </div>
        )}
        {messages.map((msg, index) => (
          <div key={index} className={`message-bubble ${msg.role}`}>
            {msg.text}
          </div>
        ))}
        {isLoading && (
          <div className="message-bubble assistant loading">
            <span className="dot">.</span><span className="dot">.</span><span className="dot">.</span>
          </div>
        )}
        <div ref={messagesEndRef} />
      </div>

      <form className="chatbot-input-form" onSubmit={handleSend}>
        <input
          type="text"
          value={inputMessage}
          onChange={(e) => setInputMessage(e.target.value)}
          placeholder="메시지를 입력하세요..."
          disabled={isLoading}
        />
        <button type="submit" disabled={isLoading} className="btn-primary">
          전송
        </button>
      </form>
    </div>
  );
}