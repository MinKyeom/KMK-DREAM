// src/pages/App.jsx

import React, { useState } from "react"; 
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import { logoutUser } from "../api/auth"; 
import { useTheme } from "../context/ThemeContext.jsx";
import { useAuth } from "../context/AuthContext.jsx"; 
import PostList from "./Post/PostList.jsx";
import PostDetail from "./Post/PostDetail.jsx";
import WritePost from "./Post/WritePost.jsx";
import SignUp from "./Auth/SignUp.jsx";
import SignIn from "./Auth/SignIn.jsx";
import HomePage from "./HomePage.jsx";
import Chatbot from "../components/Chatbot.jsx";
import "../App.css"; 
import "../components/Chatbot.css"; 

// ⭐ 전역 테마 토글 컴포넌트
const HeaderThemeToggle = () => {
  const { isDarkMode, toggleTheme } = useTheme();
  
  return (
    <button 
      onClick={toggleTheme} 
      className="global-theme-toggle"
      title={isDarkMode ? "라이트 모드 전환" : "다크 모드 전환"}
    >
      {/* 감성적인 아이콘 사용 */}
      {isDarkMode ? "☀️" : "🌙"}
    </button>
  );
};

// 간단한 헤더 컴포넌트: 버튼 위치 및 아이콘 통일
const Header = () => { 
  const { isAuthenticated, nickname, refreshAuth } = useAuth();
  
  const handleLogout = async () => {
    try {
      await logoutUser();
      alert("로그아웃 되었습니다.");
      refreshAuth(); 
    } catch (error) {
      console.error("로그아웃 오류:", error);
      alert("로그아웃 중 오류가 발생했습니다.");
    }
  };

  return (
    <header>
      <div>
        {/* 블로그 로고 */}
        <h1>
          <Link to="/">DevBlog</Link>
        </h1>
        
        {/* 네비게이션 및 인증/테마 토글 */}
        <nav>
          <Link to="/">홈</Link>
          <Link to="/post">포스트</Link>
          
          {isAuthenticated ? (
            <>
              <span style={{color: 'var(--color-accent)', fontWeight: 600}}>
                 {nickname}님
              </span>
              <button onClick={handleLogout} className="btn-secondary btn-sm" style={{ padding: '8px 15px'}}>
                <span role="img" aria-label="logout">🚪</span> 로그아웃
              </button>
            </>
          ) : (
            <>
              <Link to="/signin" className="btn-secondary btn-sm" style={{ padding: '8px 15px'}}>
              <span role="img" aria-label="signin">🔑</span> 로그인
              </Link>
              <Link to="/signup" className="btn-primary btn-sm" style={{ padding: '8px 15px'}}>
              <span role="img" aria-label="signup">👤</span> 회원가입
              </Link>
            </>
          )}

          {/* 전역 테마 토글 버튼 (우측 끝에 배치) */}
          <HeaderThemeToggle /> 
        </nav>
      </div>
    </header>
  );
};

export default function App() {
  // 챗봇 상태 관리
  const [isChatOpen, setIsChatOpen] = useState(false);

  const toggleChat = () => {
    setIsChatOpen(prev => !prev);
  };

  return (
    <Router>
      <div className="App">
        {/* Header는 AuthContext에 접근하여 상태를 업데이트합니다. */}
        <Header /> 
        
        <main>
          <Routes>
            <Route path="/" element={<HomePage />} /> 
            <Route path="/post" element={<PostList />} /> 
            <Route path="/post/:id" element={<PostDetail />} />
            <Route path="/write" element={<WritePost />} /> 
            <Route path="/post/edit/:id" element={<WritePost isEdit={true} />} />
            <Route path="/signup" element={<SignUp />} />
            <Route path="/signin" element={<SignIn />} />
          </Routes>
        </main>

        {/* 챗봇 플로팅 버튼 및 팝업 (우측 하단 고정) */}
        {isChatOpen && (
            // isChatOpen 상태가 true일 때만 팝업 표시
            <Chatbot setIsChatOpen={setIsChatOpen} />
        )}
        
        <button 
            className="chatbot-float-btn"
            onClick={toggleChat}
            title={isChatOpen ? "챗봇 닫기" : "챗봇 열기"}
        >
          {isChatOpen ? <span role="img" aria-label="close">✖️</span> : <span role="img" aria-label="chat">🤖</span>}
        </button>
        
      </div>
    </Router>
  );
}