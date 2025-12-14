// src/components/Chatbot/Chatbot.jsx
"use client"; // ⭐ 클라이언트 컴포넌트 선언

import React, { useState, useEffect, useRef } from "react";
import { sendChatMessage } from "../../services/api/chat"; // API 경로 수정
import { useAuth } from "../../providers/AuthProvider"; // Provider 경로 수정
import "./Chatbot.css"; // CSS 경로 수정

export default function Chatbot({ setIsChatOpen }) { 
  // 채팅 메시지 상태: [{ role: 'user'/'assistant', text: 'message' }]
  const [messages, setMessages] = useState([]);
  const [inputMessage, setInputMessage] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  
  // useAuth 훅을 사용하여 상태 변화에 반응
  const { id: currentUserId, nickname: currentUserNickname } = useAuth();
  // 비로그인 시 'guest_user' 사용을 원칙으로 유지
  const sessionId = currentUserId || "guest_user"; 

  const messagesEndRef = useRef(null);
  
  // 메시지가 추가될 때마다 스크롤을 맨 아래로 이동
  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  // 챗봇 팝업 닫기
  const handleClose = () => {
    setIsChatOpen(false);
  };

  // 채팅 메시지 전송 핸들러
  const handleSend = async (e) => {
    e.preventDefault();
    if (inputMessage.trim() === "" || isLoading) return;

    const userMessage = inputMessage.trim();
    
    // 1. 사용자 메시지 목록에 추가
    setMessages((prev) => [...prev, { role: "user", text: userMessage }]);
    setInputMessage(""); // 입력창 초기화
    setIsLoading(true);

    try {
      // 2. 챗봇 API 호출
      const botResponse = await sendChatMessage(sessionId, userMessage); // chat.js 함수 사용
      
      // 3. 챗봇 응답 메시지 목록에 추가
      setMessages((prev) => [...prev, { role: "assistant", text: botResponse }]);
    } catch (error) {
      // API 오류 발생 시
      setMessages((prev) => [...prev, { role: "assistant", text: "오류: 메시지를 처리할 수 없습니다." }]);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="chatbot-container">
      {/* 헤더 */}
      <div className="chatbot-header">
        <h3>Dev Blog 챗봇</h3>
        <button className="close-btn" onClick={handleClose}>
          &times;
        </button>
      </div>

      {/* 메시지 목록 */}
      <div className="chatbot-messages">
        {messages.length === 0 && (
          <div className="chatbot-welcome">
            안녕하세요! 블로그 챗봇입니다.<br/>
            궁금한 점을 물어보거나, 관심사/공부 내용을 저장해 보세요.
            <br/><br/>
            {currentUserId 
              ? `👤 **${currentUserNickname || currentUserId}** 님으로 세션이 시작됩니다.` 
              : `**비회원** 세션입니다. 로그인 시 기록이 유지됩니다.`
            }
          </div>
        )}
        {messages.map((msg, index) => (
          // 마크다운 문법 대신 간단한 문자열 렌더링을 위해 Pre-wrap 스타일 사용
          <div key={index} className={`message-bubble ${msg.role}`}>
            {msg.text}
          </div>
        ))}
        {isLoading && (
          <div className="message-bubble assistant loading">
            <span className="dot">.</span><span className="dot">.</span><span className="dot">.</span>
          </div>
        )}
        {/* 스크롤 위치를 잡아주는 Ref */}
        <div ref={messagesEndRef} />
      </div>

      {/* 입력 폼 */}
      <form className="chatbot-input-form" onSubmit={handleSend}>
        <input
          type="text"
          value={inputMessage}
          onChange={(e) => setInputMessage(e.target.value)}
          placeholder={isLoading ? "응답을 기다리는 중..." : "메시지를 입력하세요..."}
          disabled={isLoading}
        />
        <button type="submit" className="btn-primary" disabled={isLoading}>
          전송
        </button>
      </form>
    </div>
  );
}