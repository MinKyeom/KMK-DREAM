// src/pages/App.jsx (수정)

import React from "react";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import { getAuthUser, logoutUser } from "../api/auth";
// ✨ ThemeContext.jsx로 경로 수정
import { useTheme } from "../context/ThemeContext.jsx";

// 페이지 컴포넌트 임포트 (이 파일들에도 JSX가 있다면 .jsx로 변경해야 합니다)
import PostList from "./Post/PostList";
import PostDetail from "./Post/PostDetail";
import WritePost from "./Post/WritePost";
import SignUp from "./Auth/SignUp";
import SignIn from "./Auth/SignIn";

// 간단한 헤더 컴포넌트
const Header = () => {
  const auth = getAuthUser();
  const { isDarkMode, toggleTheme } = useTheme(); // ✨ 테마 훅 사용

  const handleLogout = () => {
    logoutUser();
    window.location.href = "/";
  };

  return (
    <header>
      <h1 style={{ margin: 0 }}>
        <Link to="/">React Blog</Link>
      </h1>
      <nav style={{ display: "flex", alignItems: "center" }}>
        {auth.isAuthenticated && (
          <Link to="/write" style={{ marginRight: "20px", fontWeight: "bold" }}>
            글쓰기
          </Link>
        )}

        {auth.isAuthenticated ? (
          <>
            <span style={{ marginRight: "15px" }}>
              환영합니다. (ID: {auth.id})
            </span>
            <button onClick={handleLogout} className="btn-secondary">
              로그아웃
            </button>
          </>
        ) : (
          <>
            <Link to="/signin" style={{ marginRight: "15px" }}>
              로그인
            </Link>
            <Link to="/signup">회원가입</Link>
          </>
        )}

        {/* ✨ 테마 토글 버튼 추가 */}
        <button onClick={toggleTheme} className="theme-toggle-button">
          {isDarkMode ? "🌞 라이트 모드 전환" : "🌙 다크 모드 전환"}
        </button>
      </nav>
    </header>
  );
};

export default function App() {
  return (
    <Router>
      <div className="App">
        <Header />
        <main>
          <Routes>
            <Route path="/" element={<PostList />} />
            <Route path="/post/:id" element={<PostDetail />} />
            <Route path="/write" element={<WritePost />} />
            <Route path="/edit/:id" element={<WritePost isEdit={true} />} />
            <Route path="/signup" element={<SignUp />} />
            <Route path="/signin" element={<SignIn />} />
          </Routes>
        </main>
      </div>
    </Router>
  );
}
