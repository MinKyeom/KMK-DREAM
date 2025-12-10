// src/components/Chatbot.jsx

import React, { useState, useEffect, useRef } from "react";
import { sendChatMessage } from "../api/chat"; 
import { useAuth } from "../context/AuthContext.jsx"; 
import "./Chatbot.css"; 

export default function Chatbot({ setIsChatOpen }) { 
  // 채팅 메시지 상태: [{ role: 'user'/'assistant', text: 'message' }]
  const [messages, setMessages] = useState([]);
  const [inputMessage, setInputMessage] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  
  // useAuth 훅을 사용하여 상태 변화에 반응
  const { id: currentUserId, nickname: currentUserNickname } = useAuth();
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
    
    // 1. 사용자 메시지 목록에 추가
    setMessages((prev) => [...prev, { role: "user", text: userMessage }]);
    setInputMessage(""); // 입력 필드 초기화
    setIsLoading(true); // 로딩 시작

    try {
      // 2. 챗봇 API 호출
      const botResponseText = await sendChatMessage(sessionId, userMessage);
      
      // 3. 챗봇 응답 목록에 추가
      setMessages((prev) => [
        ...prev,
        { role: "assistant", text: botResponseText },
      ]);
    } catch (error) {
      console.error("Chatbot send error:", error);
      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          text: "메시지를 처리하는 중 오류가 발생했습니다. 잠시 후 다시 시도해 주세요.",
        },
      ]);
    } finally {
      setIsLoading(false); // 로딩 종료
    }
  };
  
  // 챗봇 닫기 핸들러
  const handleClose = () => {
    setIsChatOpen(false);
  };
  

  return (
    <div className="chatbot-container">
      <div className="chatbot-header">
        <span>AI 개발 챗봇</span>
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
          placeholder="메시지를 입력하세요..."
          disabled={isLoading}
        />
        <button type="submit" className="btn-primary" disabled={isLoading}>
          전송
        </button>
      </form>
    </div>
  );
}