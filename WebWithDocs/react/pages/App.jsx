import React, { useState } from "react"; 
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import { getAuthUser, logoutUser } from "../api/auth";
import { useTheme } from "../context/ThemeContext.jsx";

// ⭐ 1. 새로 추가된 메인 페이지 컴포넌트 임포트
import HomePage from "./HomePage.jsx"; 
import Chatbot from "../components/Chatbot.jsx"; 

// 기존 컴포넌트 임포트
import PostList from "./Post/PostList.jsx";
import PostDetail from "./Post/PostDetail.jsx";
import WritePost from "./Post/WritePost.jsx";
import SignUp from "./Auth/SignUp.jsx";
import SignIn from "./Auth/SignIn.jsx";

// 간단한 헤더 컴포넌트 (상단바 URL 및 글로벌 토글)
const Header = () => { 
  const auth = getAuthUser();
  const { isDarkMode, toggleTheme } = useTheme();

  const handleLogout = () => {
    logoutUser();
    window.location.href = "/"; // 로그아웃 후 홈으로 이동
  };

  return (
    <header>
      <h1 style={{ margin: 0 }}>
        <Link to="/">React Blog</Link>
      </h1>
      <nav style={{ display: "flex", alignItems: "center" }}>
        {/* ⭐ 상단바에 블로그 정보 찾아가기 링크 추가 */}
        <Link to="/post" className="btn-secondary">
          블로그 정보 찾아가기
        </Link>
        
        {auth.isAuthenticated ? (
          <>
            <span style={{ margin: "0 10px", color: "var(--color-text-sub)" }}>
              {auth.id} 님
            </span>
            <Link to="/write">
              <button className="btn-primary">새 글 작성</button>
            </Link>
            <button onClick={handleLogout} className="btn-secondary">
              로그아웃
            </button>
          </>
        ) : (
          <>
            <Link to="/signup">
              <button className="btn-secondary">회원가입</button>
            </Link>
            <Link to="/signin">
              <button className="btn-primary">로그인</button>
            </Link>
          </>
        )}
        {/* 글로벌 테마 토글 버튼 */}
        <button onClick={toggleTheme} className="btn-secondary">
          {isDarkMode ? "🌞" : "🌙"}
        </button>
      </nav>
    </header>
  );
};

export default function App() {
  // ⭐ 챗봇 상태 관리
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
            {/* ⭐ 메인 페이지 (/)는 새로운 HomePage로 */}
            <Route path="/" element={<HomePage />} /> 
            {/* ⭐ 기존 PostList는 /post 경로로 변경 */}
            <Route path="/post" element={<PostList />} /> 

            {/* 나머지 경로는 유지 */}
            <Route path="/post/:id" element={<PostDetail />} />
            <Route path="/write" element={<WritePost />} /> 
            <Route path="/post/edit/:id" element={<WritePost isEdit={true} />} />
            <Route path="/signup" element={<SignUp />} />
            <Route path="/signin" element={<SignIn />} />
          </Routes>
        </main>

        {/* 챗봇 플로팅 버튼 및 팝업 (모든 페이지의 우측 하단에 고정) */}
        {/* Chatbot.css의 .chatbot-float-btn 스타일을 사용하여 우측 하단에 고정 */}
        {!isChatOpen && (
          <button className="chatbot-float-btn" onClick={toggleChat} title="챗봇 열기">
            💬
          </button>
        )}
        {isChatOpen && (
          <Chatbot isChatOpen={isChatOpen} setIsChatOpen={setIsChatOpen} />
        )}
      </div>
    </Router>
  );
}