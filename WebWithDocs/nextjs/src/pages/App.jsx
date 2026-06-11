// src/pages/App.jsx (새 디자인 적용)

import React, { useState } from "react"; 
import { BrowserRouter as Router, Routes, Route, Link, NavLink } from "react-router-dom"; 
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
      // 로그아웃 성공 후 인증 상태 갱신
      refreshAuth(); 
      alert("로그아웃되었습니다.");
    } catch (error) {
      console.error("로그아웃 오류:", error);
      alert("로그아웃에 실패했습니다. 다시 시도해 주세요.");
    }
  };

  return (
    <header>
      <div>
        {/* 로고: Brunch/Leedo 스타일의 깔끔한 타이틀 */}
        <Link to="/" style={{ color: 'inherit', textDecoration: 'none' }}>
            <h1>Developer's Blog</h1> 
        </Link>
        
        <nav style={{ display: 'flex', alignItems: 'center' }}>
          {/* NavLink 사용으로 활성화된 링크에 스타일 적용 가능 */}
          <NavLink to="/" end>Home</NavLink>
          <NavLink to="/post">Post</NavLink>
          {isAuthenticated && (
            <NavLink to="/write">Write</NavLink>
          )}

          {/* 인증 상태에 따른 버튼 */}
          {isAuthenticated ? (
            <>
              <span style={{ marginLeft: '20px', color: 'var(--color-text-sub)', fontSize: '0.95em' }}>
                {nickname}님
              </span>
              <button 
                onClick={handleLogout} 
                className="btn-link-primary" 
                style={{ marginLeft: '10px' }}
              >
                Logout
              </button>
            </>
          ) : (
            <NavLink to="/signin" className="btn-primary" style={{ marginLeft: '20px', padding: '8px 15px' }}>
              Login
            </NavLink>
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
        
        {/* ⭐ 챗봇 플로팅 버튼 (위치 고정 유지) */}
        <button 
          className="chatbot-float-btn" 
          onClick={toggleChat}
          title={isChatOpen ? "챗봇 닫기" : "챗봇 열기"}
        >
          {isChatOpen ? '✖️' : '🤖'}
        </button>
      </div>
    </Router>
  );
}